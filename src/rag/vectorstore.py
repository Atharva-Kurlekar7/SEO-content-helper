import os
import pickle
import numpy as np
import hnswlib
from sentence_transformers import SentenceTransformer
from src.config import load_config

config = load_config()

class VectorStore:
    """Vector storage for embeddings."""
    
    def __init__(self, embeddings=None):
        if embeddings:
            self.embeddings = embeddings
        else:
            # Use SentenceTransformer
            self.embeddings = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None
        self.texts = []
        self.metadatas = []
        self.index_path = os.path.join('data', 'embeddings', 'hnsw_index.bin')
        self.data_path = os.path.join('data', 'embeddings', 'hnsw_data.pkl')
        
    def save(self):
        """Save the vector store to disk."""
        if self.index:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(self.index_path), exist_ok=True)
            
            # Save the HNSW index
            self.index.save_index(self.index_path)
            
            # Save texts and metadata
            with open(self.data_path, 'wb') as f:
                pickle.dump((self.texts, self.metadatas), f)
    
    def load(self):
        """Load the vector store from disk."""
        if os.path.exists(self.index_path) and os.path.exists(self.data_path):
            # Load data
            with open(self.data_path, 'rb') as f:
                self.texts, self.metadatas = pickle.load(f)
            
            # Get embedding dimension
            sample_embedding = self.embeddings.encode(["Sample text"])
            dim = sample_embedding.shape[1]
            
            # Create and load index
            self.index = hnswlib.Index(space='cosine', dim=dim)
            self.index.load_index(self.index_path, max_elements=len(self.texts))
            
            return True
        return False
    
    def add_texts(self, texts, metadatas=None):
        """Add texts to the vector store."""
        if not metadatas:
            metadatas = [{} for _ in texts]
        
        # Store texts and metadata
        start_idx = len(self.texts)
        self.texts.extend(texts)
        self.metadatas.extend(metadatas)
        
        # Create embeddings
        embeddings = self.embeddings.encode(texts)
        
        # Initialize or update index
        if self.index is None:
            dim = embeddings.shape[1]
            self.index = hnswlib.Index(space='cosine', dim=dim)
            self.index.init_index(max_elements=max(1000, len(texts)*2), ef_construction=200, M=16)
            self.index.set_ef(50)
            
        # Add embeddings to index
        self.index.add_items(embeddings, list(range(start_idx, start_idx + len(texts))))
        
        # Save after adding new texts
        self.save()
    
    def similarity_search(self, query, k=3):
        """Perform similarity search."""
        if not self.index:
            if not self.load():
                return []
        
        # Create query embedding
        query_embedding = self.embeddings.encode([query])[0]
        
        # Search using HNSW
        labels, distances = self.index.knn_query(query_embedding, k=k)
        
        # Create Document objects for results
        from langchain.schema import Document
        
        results = []
        for idx in labels[0]:
            if idx < len(self.texts):
                doc = Document(
                    page_content=self.texts[idx],
                    metadata=self.metadatas[idx] if idx < len(self.metadatas) else {}
                )
                results.append(doc)
        
        return results
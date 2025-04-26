from src.rag.vectorstore import VectorStore
from sentence_transformers import SentenceTransformer  # For creating embeddings
from src.config import load_config

config = load_config()

class Retriever:
    """Content retrieval mechanisms for RAG."""
    
    def __init__(self):
        # Use SentenceTransformer instead of OpenAI
        self.embeddings = SentenceTransformer('all-MiniLM-L6-v2')
        self.vector_store = VectorStore(self.embeddings)
    
    def retrieve_relevant_knowledge(self, query, k=3):
        """Retrieve relevant knowledge for a query."""
        docs = self.vector_store.similarity_search(query, k=k)
        
        # Extract text from docs
        knowledge = [doc.page_content for doc in docs]
        
        return knowledge
    
    def retrieve_with_filter(self, query, filter_dict, k=3):
        """Retrieve with metadata filtering."""
        if not self.vector_store.vector_store:
            if not self.vector_store.load():
                return []
        
        # Create query embedding
        query_embedding = self.embeddings.encode([query])[0]
        
        # Since FAISS doesn't support direct filtering, we'll need to retrieve more results
        # and then filter them manually
        docs = self.vector_store.vector_store.similarity_search_by_vector(query_embedding, k=k*3)
        
        # Filter docs based on metadata
        filtered_docs = []
        for doc in docs:
            match = True
            for key, value in filter_dict.items():
                if key not in doc.metadata or doc.metadata[key] != value:
                    match = False
                    break
            if match:
                filtered_docs.append(doc)
            
            if len(filtered_docs) >= k:
                break
        
        # Extract text from docs
        knowledge = [doc.page_content for doc in filtered_docs[:k]]
        
        return knowledge
    
    def retrieve_for_title(self, title):
        """Retrieve knowledge specifically for title optimization."""
        query = f"YouTube SEO title optimization: {title}"
        return self.retrieve_with_filter(query, {"category": "title"}, k=2)
    
    def retrieve_for_description(self, description_snippet):
        """Retrieve knowledge specifically for description optimization."""
        query = f"YouTube SEO description optimization: {description_snippet[:100]}"
        return self.retrieve_with_filter(query, {"category": "description"}, k=2)
    
    def retrieve_for_tags(self, tags_snippet):
        """Retrieve knowledge specifically for tags optimization."""
        query = f"YouTube SEO tags optimization: {tags_snippet}"
        return self.retrieve_with_filter(query, {"category": "tags"}, k=2)
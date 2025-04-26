import os
import markdown
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.config import load_config

config = load_config()

class SEOKnowledgeBase:
    def __init__(self):
        self.knowledge_base_dir = os.path.join('data', 'seo_best_practices')
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.documents = []
        self.texts = []
        self.tfidf_matrix = None
        
    def load_documents(self):
        """Load SEO best practices documents."""
        documents = []
        
        # Create directory if it doesn't exist
        os.makedirs(self.knowledge_base_dir, exist_ok=True)
        
        files = os.listdir(self.knowledge_base_dir)
        if not files:
            self._create_default_knowledge()
            files = os.listdir(self.knowledge_base_dir)
            
        for filename in files:
            if filename.endswith('.md'):
                file_path = os.path.join(self.knowledge_base_dir, filename)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Convert markdown to plain text
                    html = markdown.markdown(content)
                    soup = BeautifulSoup(html, 'html.parser')
                    text = soup.get_text()
                    
                    # Create a document
                    document = {
                        'content': text,
                        'metadata': {"source": filename}
                    }
                    documents.append(document)
        
        return documents
    
    def create_vector_store(self):
        """Create a vector store from the knowledge base documents."""
        documents = self.load_documents()
        
        # Split texts into chunks (simplified chunking)
        chunks = []
        for doc in documents:
            text = doc['content']
            # Split by paragraphs
            paragraphs = text.split('\n\n')
            for i, para in enumerate(paragraphs):
                if para.strip():
                    chunks.append({
                        'content': para,
                        'metadata': {**doc['metadata'], 'chunk': i}
                    })
        
        # Store document chunks
        self.documents = chunks
        
        # Extract texts for vectorization
        self.texts = [doc['content'] for doc in chunks]
        
        # Create TF-IDF matrix
        self.tfidf_matrix = self.vectorizer.fit_transform(self.texts)
        
        return self.tfidf_matrix
    
    def get_relevant_knowledge(self, query, k=3):
        """Retrieve relevant knowledge based on a query."""
        if self.tfidf_matrix is None:
            self.create_vector_store()
            
        if len(self.documents) == 0:
            return ["No knowledge base available."]
        
        # Transform query using the same vectorizer
        query_vec = self.vectorizer.transform([query])
        
        # Calculate similarity
        similarity = cosine_similarity(query_vec, self.tfidf_matrix)[0]
        
        # Get top k indices
        top_indices = similarity.argsort()[-k:][::-1]
        
        # Return content from most similar chunks
        return [self.documents[idx]['content'] for idx in top_indices]
    
    def _create_default_knowledge(self):
        """Create default knowledge files if none exist."""
        os.makedirs(self.knowledge_base_dir, exist_ok=True)
        
        # Default title best practices
        title_content = """# YouTube Title SEO Best Practices

## Length and Format
- Keep titles between 60-70 characters to ensure they don't get cut off in search results
- Use numbers (e.g., "7 Ways to..." or "Top 10...") when appropriate
- Include the current year for time-sensitive content

## Keyword Optimization
- Place the most important keywords at the beginning of the title
- Research trending keywords in your niche using tools like TubeBuddy or VidIQ
- Use exact match search terms that people would type into YouTube search

## Engagement Factors
- Create curiosity gaps to encourage clicks (without being clickbait)
- Use emotional triggers (amazing, shocking, surprising, etc.) when appropriate
- Test different title formats to see what resonates with your audience

## Title Types That Perform Well
- How-to titles ("How to [Solve a Problem]")
- List titles ("10 Ways to [Achieve Something]")
- Question titles ("Is [Something] Worth It?")
- Tutorial titles ("[Topic] Tutorial for Beginners")
- Comparison titles ("[Product A] vs [Product B]")
"""
        
        # Default description best practices
        description_content = """# YouTube Description SEO Best Practices

## First 3 Lines (Above the Fold)
- Include primary keywords in the first 1-2 sentences
- Hook viewers with a compelling reason to watch the entire video
- Include a clear call-to-action (subscribe, like, comment)

## Keyword Optimization
- Use your main keyword 2-3 times naturally throughout the description
- Include related keywords and phrases
- Add hashtags (3-5 is optimal) at the end of the description

## Length and Structure
- Write at least 200-300 words for a comprehensive description
- Use paragraphs, not walls of text
- Include timestamps for longer videos to improve user experience

## Links and Calls-to-Action
- Include links to related content (use full URLs with https://)
- Add social media links
- Include links to products mentioned (affiliate links where appropriate)
- Add subscription link with a clear call-to-action

## Additional Elements
- Include a brief summary of what viewers will learn
- Add your upload schedule
- Include disclaimer text if needed (affiliate links, sponsorships)
- Add relevant playlists
- Include copyright information
"""
        
        # Default tags best practices
        tags_content = """# YouTube Tags SEO Best Practices

## Tag Selection
- Use 10-15 tags per video for optimal reach
- Start with your primary keyword as the first tag
- Include a mix of broad and specific tags
- Use multi-word phrases that viewers might search for
- Include common misspellings of your keywords

## Tag Research
- Research trending tags using tools like TubeBuddy or VidIQ
- Look at competitors' tags (use browser extensions to view them)
- Use YouTube's search suggestions for tag ideas
- Include both singular and plural versions of keywords

## Tag Structure
- Place more specific tags near the beginning
- Include exact phrases from your title
- Use some broad category tags
- Include brand names or product names mentioned in your video

## Tag Updates
- Refresh tags on older videos to include trending terms
- Remove underperforming tags after analyzing video performance
- Align tags with current search trends in your niche
- Test different tag combinations to see what works best
"""
        
        # Write the files
        with open(os.path.join(self.knowledge_base_dir, 'title_practices.md'), 'w', encoding='utf-8') as f:
            f.write(title_content)
            
        with open(os.path.join(self.knowledge_base_dir, 'description_practices.md'), 'w', encoding='utf-8') as f:
            f.write(description_content)
            
        with open(os.path.join(self.knowledge_base_dir, 'tags_practices.md'), 'w', encoding='utf-8') as f:
            f.write(tags_content)
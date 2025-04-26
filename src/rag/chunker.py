from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter

class Chunker:
    """Text chunking strategies for RAG."""
    
    @staticmethod
    def chunk_by_character(text, chunk_size=1000, chunk_overlap=200):
        """Split text into chunks by character count."""
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        
        return text_splitter.split_text(text)
    
    @staticmethod
    def chunk_by_markdown(text, chunk_size=1000, chunk_overlap=200):
        """Split markdown text into chunks, preserving structure."""
        text_splitter = RecursiveCharacterTextSplitter(
            separators=["\n## ", "\n### ", "\n#### ", "\n", " ", ""],
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        
        return text_splitter.split_text(text)
    
    @staticmethod
    def chunk_description(description, chunk_size=500, chunk_overlap=50):
        """Split YouTube description into meaningful chunks."""
        # For descriptions, we want to preserve paragraph structure
        text_splitter = RecursiveCharacterTextSplitter(
            separators=["\n\n", "\n", ". ", ", ", " ", ""],
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        
        return text_splitter.split_text(description)
    
    @staticmethod
    def chunk_tags(tags):
        """Process tags for analysis."""
        # For tags, we might want to group related tags
        # This is a simple implementation that returns the tags as is
        return tags
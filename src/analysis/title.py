from src.prompt_engineering.handlers import handle_title_analysis
from src.youtube.extractor import extract_keywords

def analyze_title(title):
    """Analyze a YouTube video title for SEO effectiveness."""
    if not title:
        return "<p>No title provided for analysis.</p>"
    
    # Extract potential keywords from the title
    keywords = extract_keywords(title)
    
    # Get analysis from prompt engineering handler
    analysis = handle_title_analysis(title)
    
    return analysis
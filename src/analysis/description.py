from src.prompt_engineering.handlers import handle_description_analysis
from src.youtube.extractor import extract_keywords

def analyze_description(description):
    """Analyze a YouTube video description for SEO effectiveness."""
    if not description:
        return "<p>No description provided for analysis.</p>"
    
    # Extract potential keywords from the description
    keywords = extract_keywords(description)
    
    # Get analysis from prompt engineering handler
    analysis = handle_description_analysis(description)
    
    return analysis
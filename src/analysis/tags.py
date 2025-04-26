from src.prompt_engineering.handlers import handle_tags_analysis

def analyze_tags(tags):
    """Analyze YouTube video tags for SEO effectiveness."""
    if not tags or len(tags) == 0:
        return "<p>No tags provided for analysis.</p>"
    
    # Get analysis from prompt engineering handler
    analysis = handle_tags_analysis(tags)
    
    return analysis
import re

def clean_text(text):
    """Clean text by removing special characters and normalizing whitespace."""
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Replace multiple whitespace with a single space
    text = re.sub(r'\s+', ' ', text)
    
    # Trim leading and trailing whitespace
    text = text.strip()
    
    return text

def count_words(text):
    """Count the number of words in a text."""
    if not text:
        return 0
    
    # Split by whitespace and count non-empty words
    words = text.split()
    return len(words)

def truncate_text(text, max_length=100, add_ellipsis=True):
    """Truncate text to a maximum length."""
    if not text or len(text) <= max_length:
        return text
    
    truncated = text[:max_length]
    
    # Try to truncate at a word boundary
    last_space = truncated.rfind(' ')
    if last_space > 0:
        truncated = truncated[:last_space]
    
    if add_ellipsis:
        truncated += '...'
    
    return truncated

def extract_urls(text):
    """Extract URLs from text."""
    url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    return re.findall(url_pattern, text)

def extract_hashtags(text):
    """Extract hashtags from text."""
    hashtag_pattern = r'#(\w+)'
    return re.findall(hashtag_pattern, text)
def extract_keywords(text):
    """Extract potential keywords from text content."""
    # This is a simple implementation
    # In a real-world scenario, you might use NLP libraries like spaCy
    
    # Remove special characters and convert to lowercase
    cleaned_text = ''.join(c if c.isalnum() or c.isspace() else ' ' for c in text).lower()
    
    # Split into words
    words = cleaned_text.split()
    
    # Filter out short words and common words
    common_words = {'the', 'and', 'is', 'in', 'to', 'of', 'a', 'for', 'on', 'with', 'as', 'by', 'at', 'an', 'this', 'that', 'it', 'from'}
    keywords = [word for word in words if len(word) > 3 and word not in common_words]
    
    # Count occurrences
    keyword_count = {}
    for keyword in keywords:
        if keyword in keyword_count:
            keyword_count[keyword] += 1
        else:
            keyword_count[keyword] = 1
    
    # Sort by count
    sorted_keywords = sorted(keyword_count.items(), key=lambda x: x[1], reverse=True)
    
    # Return top keywords
    return [keyword for keyword, count in sorted_keywords[:20]]
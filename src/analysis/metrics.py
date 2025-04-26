def analyze_title_metrics(title):
    """Analyze metrics for a YouTube video title."""
    metrics = {}
    
    # Length analysis
    title_length = len(title)
    metrics['length'] = title_length
    metrics['length_score'] = _calculate_length_score(title_length, 40, 60)
    
    # Word count analysis
    words = title.split()
    word_count = len(words)
    metrics['word_count'] = word_count
    metrics['word_count_score'] = _calculate_score(word_count, 5, 10)
    
    # Capitalization analysis
    capital_words = sum(1 for word in words if word[0].isupper())
    metrics['capitalization_ratio'] = capital_words / word_count if word_count > 0 else 0
    
    # Numbers in title
    has_number = any(char.isdigit() for char in title)
    metrics['has_number'] = has_number
    
    # Special characters
    special_chars = sum(1 for char in title if not char.isalnum() and not char.isspace())
    metrics['special_chars'] = special_chars
    
    return metrics

def analyze_description_metrics(description):
    """Analyze metrics for a YouTube video description."""
    metrics = {}
    
    # Length analysis
    description_length = len(description)
    metrics['length'] = description_length
    metrics['length_score'] = _calculate_length_score(description_length, 500, 2000)
    
    # Word count analysis
    words = description.split()
    word_count = len(words)
    metrics['word_count'] = word_count
    metrics['word_count_score'] = _calculate_score(word_count, 100, 300)
    
    # Paragraph count
    paragraphs = description.split('\n\n')
    metrics['paragraph_count'] = len(paragraphs)
    
    # Links count
    http_count = description.lower().count('http')
    metrics['link_count'] = http_count
    
    # First paragraph analysis
    first_paragraph = paragraphs[0] if paragraphs else ''
    metrics['first_paragraph_length'] = len(first_paragraph)
    
    return metrics

def analyze_tags_metrics(tags):
    """Analyze metrics for YouTube video tags."""
    metrics = {}
    
    # Tag count
    tag_count = len(tags)
    metrics['tag_count'] = tag_count
    metrics['tag_count_score'] = _calculate_score(tag_count, 8, 15)
    
    # Average tag length
    avg_length = sum(len(tag) for tag in tags) / tag_count if tag_count > 0 else 0
    metrics['avg_tag_length'] = avg_length
    
    # Single word vs multi-word tags
    single_word_tags = sum(1 for tag in tags if ' ' not in tag)
    multi_word_tags = tag_count - single_word_tags
    metrics['single_word_ratio'] = single_word_tags / tag_count if tag_count > 0 else 0
    metrics['multi_word_ratio'] = multi_word_tags / tag_count if tag_count > 0 else 0
    
    return metrics

def _calculate_score(value, min_optimal, max_optimal, min_score=0, max_score=100):
    """Calculate a score based on a value and optimal range."""
    if value < min_optimal:
        # Below optimal range
        return min_score + ((value / min_optimal) * (max_score - min_score))
    elif value > max_optimal:
        # Above optimal range
        factor = max(0, 1 - ((value - max_optimal) / max_optimal))
        return min_score + (factor * (max_score - min_score))
    else:
        # Within optimal range
        return max_score

def _calculate_length_score(length, min_optimal, max_optimal):
    """Calculate a score based on text length."""
    return _calculate_score(length, min_optimal, max_optimal)
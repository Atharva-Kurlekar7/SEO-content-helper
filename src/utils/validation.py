import re

def is_valid_youtube_url(url):
    """Validate if a URL is a valid YouTube URL."""
    youtube_patterns = [
        r'^https?://(?:www\.)?youtube\.com/watch\?v=[\w-]+(?:&\S*)?$',
        r'^https?://(?:www\.)?youtu\.be/[\w-]+(?:\?\S*)?$',
        r'^https?://(?:www\.)?youtube\.com/embed/[\w-]+(?:\?\S*)?$'
    ]
    
    for pattern in youtube_patterns:
        if re.match(pattern, url):
            return True
    
    return False

def validate_title(title):
    """Validate a YouTube video title."""
    if not title:
        return False, "Title cannot be empty."
    
    if len(title) > 100:
        return False, "Title is too long. YouTube titles are limited to 100 characters."
    
    return True, "Title is valid."

def validate_description(description):
    """Validate a YouTube video description."""
    if not description:
        return False, "Description cannot be empty."
    
    if len(description) > 5000:
        return False, "Description is too long. YouTube descriptions are limited to 5000 characters."
    
    return True, "Description is valid."

def validate_tags(tags):
    """Validate YouTube video tags."""
    if not tags:
        return False, "No tags provided."
    
    if len(tags) > 500:
        return False, "Too many tags. YouTube allows up to 500 characters for all tags combined."
    
    # Check combined length
    combined_length = sum(len(tag) for tag in tags) + len(tags) - 1  # Adding commas
    if combined_length > 500:
        return False, "Tags are too long. YouTube allows up to 500 characters for all tags combined."
    
    return True, "Tags are valid."
import re
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from src.config import load_config

config = load_config()
youtube_api_key = config.get('YOUTUBE_API_KEY')

def extract_video_id(youtube_url):
    """Extract the video ID from a YouTube URL."""
    # Regular expression to match YouTube URLs and extract video ID
    patterns = [
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([^&\s]+)',
        r'(?:https?:\/\/)?(?:www\.)?youtu\.be\/([^\?\s]+)',
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/embed\/([^\?\s]+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, youtube_url)
        if match:
            return match.group(1)
    
    return None

def get_video_metadata(youtube_url):
    """Get metadata for a YouTube video."""
    video_id = extract_video_id(youtube_url)
    
    if not video_id:
        return None
    
    try:
        youtube = build('youtube', 'v3', developerKey=youtube_api_key)
        
        # Get video details
        response = youtube.videos().list(
            part='snippet,statistics',
            id=video_id
        ).execute()
        
        if not response['items']:
            return None
        
        snippet = response['items'][0]['snippet']
        statistics = response['items'][0]['statistics']
        
        return {
            'title': snippet.get('title', ''),
            'description': snippet.get('description', ''),
            'tags': snippet.get('tags', []),
            'published_at': snippet.get('publishedAt', ''),
            'channel_title': snippet.get('channelTitle', ''),
            'view_count': statistics.get('viewCount', 0),
            'like_count': statistics.get('likeCount', 0),
            'comment_count': statistics.get('commentCount', 0)
        }
    
    except HttpError as e:
        print(f"An HTTP error occurred: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
import unittest
from src.youtube.api import extract_video_id, get_video_metadata
from src.config import load_config

class TestYouTubeAPI(unittest.TestCase):
    """Tests for YouTube API integration."""
    
    def test_extract_video_id_watch_url(self):
        """Test extracting video ID from watch URL."""
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        video_id = extract_video_id(url)
        self.assertEqual(video_id, "dQw4w9WgXcQ")
    
    def test_extract_video_id_short_url(self):
        """Test extracting video ID from youtu.be URL."""
        url = "https://youtu.be/dQw4w9WgXcQ"
        video_id = extract_video_id(url)
        self.assertEqual(video_id, "dQw4w9WgXcQ")
    
    def test_extract_video_id_embed_url(self):
        """Test extracting video ID from embed URL."""
        url = "https://www.youtube.com/embed/dQw4w9WgXcQ"
        video_id = extract_video_id(url)
        self.assertEqual(video_id, "dQw4w9WgXcQ")
    
    def test_extract_video_id_invalid_url(self):
        """Test extracting video ID from invalid URL."""
        url = "https://www.example.com"
        video_id = extract_video_id(url)
        self.assertIsNone(video_id)
    
    def test_get_video_metadata(self):
        """Test getting video metadata."""
        # Note: This test requires a valid API key
        config = load_config()
        if not config.get('YOUTUBE_API_KEY'):
            self.skipTest("No YouTube API key available")
        
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        metadata = get_video_metadata(url)
        
        self.assertIsNotNone(metadata)
        self.assertIn('title', metadata)
        self.assertIn('description', metadata)
        self.assertIn('tags', metadata)

if __name__ == '__main__':
    unittest.main()
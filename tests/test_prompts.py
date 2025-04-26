import unittest
from src.prompt_engineering.templates import (
    TITLE_ANALYSIS_TEMPLATE,
    DESCRIPTION_ANALYSIS_TEMPLATE,
    TAGS_ANALYSIS_TEMPLATE
)

class TestPromptTemplates(unittest.TestCase):
    """Tests for prompt templates."""
    
    def test_title_template_format(self):
        """Test that title template formats correctly."""
        title = "Test Title for YouTube Video"
        formatted = TITLE_ANALYSIS_TEMPLATE.format(title=title)
        
        self.assertIn(title, formatted)
        self.assertIn("YouTube video title", formatted)
        self.assertIn("SEO effectiveness", formatted)
    
    def test_description_template_format(self):
        """Test that description template formats correctly."""
        description = "This is a test description for a YouTube video."
        formatted = DESCRIPTION_ANALYSIS_TEMPLATE.format(description=description)
        
        self.assertIn(description, formatted)
        self.assertIn("YouTube video description", formatted)
        self.assertIn("SEO effectiveness", formatted)
    
    def test_tags_template_format(self):
        """Test that tags template formats correctly."""
        tags = "tag1, tag2, tag3"
        formatted = TAGS_ANALYSIS_TEMPLATE.format(tags=tags)
        
        self.assertIn(tags, formatted)
        self.assertIn("YouTube video tags", formatted)
        self.assertIn("SEO effectiveness", formatted)

if __name__ == '__main__':
    unittest.main()
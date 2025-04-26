import unittest
from src.analysis.metrics import (
    analyze_title_metrics,
    analyze_description_metrics,
    analyze_tags_metrics
)

class TestAnalysis(unittest.TestCase):
    """Tests for analysis modules."""
    
    def test_title_metrics(self):
        """Test title metrics calculation."""
        title = "This is a Test YouTube Video Title for SEO Analysis"
        metrics = analyze_title_metrics(title)
        
        self.assertIn('length', metrics)
        self.assertIn('length_score', metrics)
        self.assertIn('word_count', metrics)
        self.assertEqual(metrics['word_count'], 10)
    
    def test_description_metrics(self):
        """Test description metrics calculation."""
        description = "This is a test description.\n\nIt has multiple paragraphs.\n\nCheck out https://example.com for more info."
        metrics = analyze_description_metrics(description)
        
        self.assertIn('length', metrics)
        self.assertIn('paragraph_count', metrics)
        self.assertIn('link_count', metrics)
        self.assertEqual(metrics['paragraph_count'], 3)
        self.assertEqual(metrics['link_count'], 1)
    
    def test_tags_metrics(self):
        """Test tags metrics calculation."""
        tags = ["test", "youtube", "video analysis", "seo", "optimization"]
        metrics = analyze_tags_metrics(tags)
        
        self.assertIn('tag_count', metrics)
        self.assertIn('avg_tag_length', metrics)
        self.assertIn('single_word_ratio', metrics)
        self.assertIn('multi_word_ratio', metrics)
        self.assertEqual(metrics['tag_count'], 5)
        self.assertGreater(metrics['single_word_ratio'], 0.5)

if __name__ == '__main__':
    unittest.main()
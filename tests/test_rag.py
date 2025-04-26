import unittest
import os
import shutil
from src.rag.knowledge_base import SEOKnowledgeBase

class TestRAG(unittest.TestCase):
    """Tests for RAG system."""
    
    def setUp(self):
        """Set up test environment."""
        # Create a test directory for knowledge base
        self.test_dir = os.path.join('data', 'test_seo_best_practices')
        os.makedirs(self.test_dir, exist_ok=True)
        
        # Create a test file
        test_content = "# Test SEO Best Practices\n\n- Practice 1\n- Practice 2\n- Practice 3"
        with open(os.path.join(self.test_dir, 'test_practices.md'), 'w', encoding='utf-8') as f:
            f.write(test_content)
    
    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_load_documents(self):
        """Test loading documents from knowledge base."""
        # Override the knowledge base dir for testing
        kb = SEOKnowledgeBase()
        kb.knowledge_base_dir = self.test_dir
        
        documents = kb.load_documents()
        
        self.assertEqual(len(documents), 1)
        self.assertIn("Test SEO Best Practices", documents[0].page_content)
        self.assertIn("Practice 1", documents[0].page_content)
    
    def test_create_default_knowledge(self):
        """Test creating default knowledge base."""
        temp_dir = os.path.join('data', 'temp_test_kb')
        
        # Create a KB instance with the temp directory
        kb = SEOKnowledgeBase()
        kb.knowledge_base_dir = temp_dir
        
        try:
            # Call the method to create default knowledge
            kb._create_default_knowledge()
            
            # Check that files were created
            self.assertTrue(os.path.exists(os.path.join(temp_dir, 'title_practices.md')))
            self.assertTrue(os.path.exists(os.path.join(temp_dir, 'description_practices.md')))
            self.assertTrue(os.path.exists(os.path.join(temp_dir, 'tags_practices.md')))
            
            # Check content of one file
            with open(os.path.join(temp_dir, 'title_practices.md'), 'r', encoding='utf-8') as f:
                content = f.read()
                self.assertIn("YouTube Title SEO Best Practices", content)
        
        finally:
            # Clean up
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)

if __name__ == '__main__':
    unittest.main()
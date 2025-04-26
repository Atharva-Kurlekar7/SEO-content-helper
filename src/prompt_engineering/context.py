class ContextManager:
    """Manages context for prompt engineering."""
    
    def __init__(self):
        self.context = {}
        
    def add_to_context(self, key, value):
        """Add a new key-value pair to the context."""
        self.context[key] = value
        
    def get_from_context(self, key):
        """Get a value from the context by key."""
        return self.context.get(key)
    
    def clear_context(self):
        """Clear the context."""
        self.context = {}
        
    def get_full_context(self):
        """Get the full context."""
        return self.context
# src/transformers/base.py

class BaseTransformer:
    def transform(self, data):
        raise NotImplementedError
    
    def validate_output(self, output):
        """
        Base validation: every transformer must implement this 
        to ensure the output matches its specific standard.
        """
        raise NotImplementedError

# Example: NIEM-specific validation
class NIEMTransformer(BaseTransformer):
    def transform(self, data):
        # XML construction logic...
        return xml_string
        
    def validate_output(self, output):
        # Check for mandatory NIEM namespace declarations
        return "xmlns:nc" in output and output.startswith("<")
        

from .base import BaseTransformer

class UDCTransformer(BaseTransformer):
    def transform(self, data):
        return f"UDC:{data['spoke_mappings']['UDC']}"

    def validate_output(self, output):
        # Ensure the string contains valid UDC separators and structure
        # Basic check for non-empty code after the prefix
        code = output.split("UDC:")[1]
        return len(code) > 0 and not any(char in code for char in [' ', '$', '@'])


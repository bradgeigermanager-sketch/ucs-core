import re
from .base import BaseTransformer

class LCCTransformer(BaseTransformer):
    def transform(self, data):
        return f"LCC:{data['spoke_mappings']['LCC']}"

    def validate_output(self, output):
        # Regex for LCC pattern: 1-2 letters + number (optional decimal)
        pattern = r"^LCC:[A-Z]{1,3}\d+(\.\d+)?$"
        return bool(re.match(pattern, output))


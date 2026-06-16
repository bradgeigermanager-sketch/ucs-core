# src/transformers/lbc.py
import re
from .base import BaseTransformer

class LBCTransformer(BaseTransformer):
    def transform(self, data):
        return f"BBK:{data['spoke_mappings']['LBC']}"

    def validate_output(self, output):
        # Regex to check for standard LBC alphanumeric patterns (e.g., 65.05)
        pattern = r"^BBK:[A-Z0-9.]+$"
        return bool(re.match(pattern, output))

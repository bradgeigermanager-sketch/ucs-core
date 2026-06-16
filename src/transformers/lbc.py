# src/transformers/lbc.py
class LBCTransformer(BaseTransformer):
    def transform(self, data):
        # Specific logic for LBC faceted strings
        return f"BBK:{data['spoke_mappings']['LBC']}"

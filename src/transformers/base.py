# src/transformers/base.py
class BaseTransformer:
    def transform(self, data):
        raise NotImplementedError("Subclasses must implement transform()")

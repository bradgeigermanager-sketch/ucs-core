from .base import BaseTransformer

class MeSHTransformer(BaseTransformer):
    def transform(self, data):
        return f"MeSH:{data['spoke_mappings']['MeSH']}"

    def validate_output(self, output):
        # MeSH IDs often look like D000001
        code = output.split("MeSH:")[1]
        return bool(re.match(r"^[A-Z]\d{6}$", code))


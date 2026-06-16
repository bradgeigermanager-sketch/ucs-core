import json

class CatalogEngine:
    def __init__(self, mappings_path):
        with open(mappings_path, 'r') as f:
            self.bridge = json.load(f)

    def map_to_hub(self, system, code):
        return self.bridge.get(system, {}).get(code, "ERR_NO_MAPPING")

    def translate(self, from_sys, code, to_sys):
        hub_id = self.map_to_hub(from_sys, code)
        if hub_id == "ERR_NO_MAPPING": return None
        
        # Reverse mapping from Hub to target system
        target = self.bridge.get(to_sys, {})
        for s_code, h_id in target.items():
            if h_id == hub_id:
                return s_code
        return None

 class TransformerFactory:
    _transformers = {
        "NIEM": NIEMTransformer(),
        "LBC": LBCTransformer()
    }

    @classmethod
    def get_transformer(cls, system_type):
        return cls._transformers.get(system_type)

# Usage:
transformer = TransformerFactory.get_transformer("NIEM")
xml_output = transformer.transform(hub_object)

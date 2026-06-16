import json
import logging

class CatalogEngine:
    """
    Core engine for the Universal Cataloging System (UCS).
    Manages Hub-to-Spoke translations and data integrity.
    """
    def __init__(self, mappings_path):
        self.mappings_path = mappings_path
        self.bridge = self._load_mappings()

    def _load_mappings(self):
        try:
            with open(self.mappings_path, 'r') as f:
                return json.load(f).get('mappings', {})
        except FileNotFoundError:
            logging.error(f"Mapping file not found at {self.mappings_path}")
            return {}

    def map_to_hub(self, system, code):
        """Normalizes an external spoke code to a central Hub ID."""
        return self.bridge.get(system, {}).get(code, "ERR_NO_MAPPING")

    def translate(self, from_sys, code, to_sys):
        """
        Translates a code from one spoke to another via the Hub.
        Returns None if mapping path is broken.
        """
        hub_id = self.map_to_hub(from_sys, code)
        if hub_id == "ERR_NO_MAPPING":
            return None
        
        # Reverse lookup: Hub -> Target Spoke
        target_system = self.bridge.get(to_sys, {})
        for spoke_code, h_id in target_system.items():
            if h_id == hub_id:
                return spoke_code
        return None

# 


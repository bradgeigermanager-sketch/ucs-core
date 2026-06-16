# src/transformers/niem.py
import xml.etree.ElementTree as ET
from .base import BaseTransformer

class NIEMTransformer(BaseTransformer):
    def transform(self, data):
        # Logic to wrap data in NIEM-conformant structure
        return f"<nc:Organization xmlns:nc='http://niem.gov/niem/niem-core/5.0'>{data['hub_id']}</nc:Organization>"

    def validate_output(self, output):
        try:
            root = ET.fromstring(output)
            # Ensure the mandatory NIEM namespace is present
            return "nc" in root.tag or "xmlns:nc" in output
        except ET.ParseError:
            return False


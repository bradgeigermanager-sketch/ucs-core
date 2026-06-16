import xml.etree.ElementTree as ET

class NIEMTransformer:
    def __init__(self, hub_data):
        self.data = hub_data

    def to_niem_xml(self):
        """Transforms a Hub object into a NIEM-conformant XML block."""
        root = ET.Element("EducationExchange", {"xmlns:nc": "http://niem.gov/niem/niem-core/5.0"})
        org = ET.SubElement(root, "nc:Organization")
        id_element = ET.SubElement(org, "nc:OrganizationIdentification")
        id_element.text = self.data['hub_id']
        return ET.tostring(root, encoding='unicode')


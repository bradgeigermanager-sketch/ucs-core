import unittest
from src.validators import validate_manifest

class TestMatchingValidator(unittest.TestCase):

    def test_valid_manifest(self):
        """Test a perfectly formed manifest."""
        data = {
            "hub_id": "HUB-123",
            "entry_metadata": {
                "source_system": "LBC",
                "original_code": "65.05"
            }
        }
        self.assertTrue(validate_manifest(data))

    def test_invalid_structure(self):
        """Test a manifest missing the required hub_id."""
        data = {
            "entry_metadata": {
                "source_system": "LBC",
                "original_code": "65.05"
            }
        }
        self.assertFalse(validate_manifest(data))

    def test_invalid_source_system(self):
        """Test a manifest with a non-supported system."""
        data = {
            "hub_id": "HUB-123",
            "entry_metadata": {
                "source_system": "UNKNOWN",
                "original_code": "000"
            }
        }
        self.assertFalse(validate_manifest(data))

if __name__ == '__main__':
    unittest.main()
    

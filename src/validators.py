import jsonschema
from jsonschema import validate

# The JSON Schema defined previously
manifest_schema = {
    "type": "object",
    "properties": {
        "hub_id": {"type": "string"},
        "entry_metadata": {
            "type": "object",
            "properties": {
                "source_system": {"enum": ["LBC", "UDC", "DDC"]},
                "original_code": {"type": "string"}
            },
            "required": ["source_system", "original_code"]
        }
    },
    "required": ["hub_id", "entry_metadata"]
}

def validate_manifest(data):
    """Checks if the data matches the schema and internal logic."""
    try:
        # 1. Schema Validation
        validate(instance=data, schema=manifest_schema)
        
        # 2. Logic Validation: Ensure the code exists in our known taxonomy
        system = data['entry_metadata']['source_system']
        code = data['entry_metadata']['original_code']
        
        # Add your logic here to check against the taxonomy/bridge tables
        print(f"Validation successful for {system} code: {code}")
        return True
    except jsonschema.exceptions.ValidationError as e:
        print(f"Validation Error: {e.message}")
        return False


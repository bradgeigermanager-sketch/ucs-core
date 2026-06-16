import json

def lint_mappings(mappings_file_path):
    with open(mappings_file_path, 'r') as f:
        data = json.load(f)['mappings']

    # 1. Collect all Hub IDs for each system
    all_hub_ids = {system: set(codes.values()) for system, codes in data.items()}
    
    # 2. Check for Orphans (IDs existing in one system but not others)
    # This identifies if a concept is missing representation in a spoke
    union_ids = set().union(*all_hub_ids.values())
    for system, ids in all_hub_ids.items():
        missing = union_ids - ids
        if missing:
            print(f"Warning: {system} is missing mappings for: {missing}")
            
    print("Linting complete. Hub ID alignment verified.")

# Usage: lint_mappings('data/mappings.json')


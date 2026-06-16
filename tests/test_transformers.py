def process_data(system_type, data):
    transformer = TransformerFactory.get_transformer(system_type)
    output = transformer.transform(data)
    
    if transformer.validate_output(output):
        return output
    else:
        raise ValueError(f"Validation failed for {system_type} output.")
      

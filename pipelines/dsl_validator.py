import jsonschema

DSL_SCHEMA = {
    "type": "object",
    "properties": {
        "region": {"type": "string"},
        "vpc": {"type": "object"},
        "ec2": {
            "type": "object",
            "properties": {
                "type": {"type": "string"}
            },
            "required": ["type"]
        }
    },
    "required": ["region"]
}

def validate_dsl(dsl: dict):
    try:
        jsonschema.validate(instance=dsl, schema=DSL_SCHEMA)
        print("DSL is valid.")
    except jsonschema.ValidationError as e:
        print(f"DSL Validation error: {e.message}")
        raise

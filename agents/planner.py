import json

class DSLPlannerAgent:
    def run(self, dsl_str: str):
        dsl = json.loads(dsl_str)
        dsl['tags'] = {"owner": "ai-pipeline", "env": "dev"}
        if 'region' not in dsl:
            dsl['region'] = "us-east-1"
        print("🧠 Planned DSL:\n", json.dumps(dsl, indent=2))
        return dsl

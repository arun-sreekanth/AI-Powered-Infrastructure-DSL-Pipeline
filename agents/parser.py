from langchain.chat_models import ChatOpenAI

class NLParserAgent:
    def run(self, input_text: str):
        llm = ChatOpenAI(model="gpt-4", temperature=0.3)
        prompt = f"""You are an infrastructure assistant.
Given this user request: '{input_text}', generate a structured JSON DSL.
"""
        response = llm.predict(prompt)
        print("Parsed DSL:\n", response)
        return response

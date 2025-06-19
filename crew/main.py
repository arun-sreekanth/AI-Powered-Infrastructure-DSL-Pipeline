from agents.parser import NLParserAgent
from agents.planner import DSLPlannerAgent
from agents.generator import HCLGeneratorAgent
from agents.secret_agent import SecretAgent
from agents.validator import PolicyValidatorAgent
from agents.executor import ExecutionAgent

def kickoff(user_input: str):
    dsl = NLParserAgent().run(user_input)
    planned_dsl = DSLPlannerAgent().run(dsl)
    HCLGeneratorAgent().run(planned_dsl)
    SecretAgent().run()
    PolicyValidatorAgent().run()
    ExecutionAgent().run()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        user_input = input("💬 Enter your infrastructure prompt: ")
    kickoff(user_input)

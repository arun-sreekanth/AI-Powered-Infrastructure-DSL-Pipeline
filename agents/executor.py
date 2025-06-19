import subprocess

class ExecutionAgent:
    def run(self):
        print("🚀 Running Terraform Init/Plan/Apply")
        subprocess.run(["terraform", "init"], cwd="terraform")
        subprocess.run(["terraform", "plan"], cwd="terraform")
        subprocess.run(["terraform", "apply", "-auto-approve"], cwd="terraform")

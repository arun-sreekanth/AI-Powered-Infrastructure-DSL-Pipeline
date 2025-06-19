import typer
from crew.main import kickoff

app = typer.Typer()

@app.command()
def run(prompt: str):
    \"\"\"Run the AI Infra DSL pipeline with a natural language prompt.\"\"\"
    kickoff(prompt)

if __name__ == \"__main__\":
    app()

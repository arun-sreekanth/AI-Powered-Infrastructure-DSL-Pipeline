import os
from jinja2 import Environment, FileSystemLoader

class TerraformWriter:
    def __init__(self, dsl: dict):
        self.dsl = dsl
        self.env = Environment(loader=FileSystemLoader("templates"))

    def write_all(self):
        os.makedirs("terraform", exist_ok=True)
        self.write_file("main.tf", "main.tf.j2")
        self.write_file("variables.tf", "variables.tf.j2")
        self.write_file("outputs.tf", "outputs.tf.j2")

    def write_file(self, target_name, template_name):
        template = self.env.get_template(template_name)
        output = template.render(dsl=self.dsl)
        with open(f"terraform/{target_name}", "w") as f:
            f.write(output)

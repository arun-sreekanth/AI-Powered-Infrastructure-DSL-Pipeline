from pipelines.terraform_writer import TerraformWriter

class HCLGeneratorAgent:
    def run(self, dsl: dict):
        writer = TerraformWriter(dsl)
        writer.write_all()
        print("Terraform code generated")

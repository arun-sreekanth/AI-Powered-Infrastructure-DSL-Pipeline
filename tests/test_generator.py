def test_hcl_generation():
    from agents.generator import HCLGeneratorAgent
    HCLGeneratorAgent().run({"region": "us-east-1", "ec2": {"type": "t2.micro"}})
    assert open("terraform/main.tf").read() != ""

def test_parser():
    from agents.parser import NLParserAgent
    result = NLParserAgent().run("Deploy VPC with EC2")
    assert "vpc" in result or "ec2" in result

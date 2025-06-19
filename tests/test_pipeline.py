def test_pipeline_end_to_end():
    from crew.main import kickoff
    kickoff("Create VPC and EC2 instance in us-east-1")

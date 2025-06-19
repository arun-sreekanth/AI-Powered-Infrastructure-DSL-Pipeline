resource "aws_db_instance" "main" {
  allocated_storage    = var.allocated_storage
  engine               = var.engine
  instance_class       = var.instance_class
  name                 = var.db_name
  username             = var.username
  password             = var.password
  skip_final_snapshot  = true
  publicly_accessible  = false

  tags = {
    Name = var.name
  }
}

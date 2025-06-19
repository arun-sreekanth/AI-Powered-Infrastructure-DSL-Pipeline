variable "ami" {
  type        = string
  description = "AMI ID"
}

variable "instance_type" {
  type        = string
  description = "Instance type"
}

variable "subnet_id" {
  type        = string
  description = "Subnet ID to launch instance"
}

variable "name" {
  type        = string
  description = "Name tag for the instance"
}

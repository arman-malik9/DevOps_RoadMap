variable "name" {
  type = string
}
variable "age" {
   type =  number 
}
output "user" {
    value = "Hello ${var.name} and your age is ${var.age}"
}
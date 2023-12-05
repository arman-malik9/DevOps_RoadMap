// 1> hello world program
# output "hello" {
#   value = "Hello World!"
# }

// 2> ultiple block in a single terraform file
# output "Name" {
#   value = "Arman Malik"
# }
# output "Age" {
#   value = "25"
# }
# output "City" {
#   value = "Noida"
# }

// 3> use of "variable", taking input from user

# variable "Name" {
# }
# output printname {
#   value = "Hello ${var.Name}"
# }

// 4> use of "variable", and "default" keyword.

# variable Name {
#     default = "Malik"
# }
# output printname {
#   value = "Hello ${var.Name}"
# }

// 5> Use of Data types  string and number
# variable "name" {
#   type = string
# }
# variable "age" {
#    type =  number 
# }
# output "user" {
#     value = "Hello ${var.name} and your age is ${var.age}"
# }

// 6> List data type

# variable usersName {
#   type = list
# }
# output "printIndexedName" {
#     value = "Hi ${var.usersName[0]} and ${var.usersName[2]}"
# }

// 7> Terraform inbuit functions.

# variable usersName {
#   type = list
#   default = ["arhan", "arman", "arbaz"]
# }
# output "printIndexedName" {
#     value = "Hi ${join(",", var.usersName)}"
# }
# output "UpperName" {
#   value = upper(var.usersName[0])
# }
# output "firstLetterInCaps" {
#   value = title(join(" ",var.usersName))
# }

// 8> map variable:
# variable "usersAge" {
#     type = map
#     default = {
#         Arman = 25
#         Shadab = 26
#     }
# }
# variable "userName" {
#     type = string
# }

# output "users" {
#   value = "Hi my name is ${var.userName} and my age is ${lookup(var.usersAge, "Shadab")}"
# }

// 9> How to read environment variables in tf configuration files.

variable "userName" {
  type    = string
  default = "Arman Malik"
}
output "user" {
  value = "Hi  ${var.userName}"
}
#!/bin/sh
# Author : Arman Malik
# Variables in Shell scripting.

#simple example of variable.
NAME="Arman Malik"
echo "Hi, My name is $NAME"

#Concatenation of string with variable.
SPORT="Foot"
echo "My favorite sport is ${SPORT}ball."

#Unseting the value of varible using "unset" command.
Num=78
echo "Number is $Num"
unset Num 
echo "Number is $Num"


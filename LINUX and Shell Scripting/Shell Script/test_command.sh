#!/bin/sh

# Author : Arman Malik
# Script follows here:
a=12
b=0
if test "$a" -eq "$b" #or if test "$a" = "$b"
then
    echo "Hi"
else
    echo "bye"
fi
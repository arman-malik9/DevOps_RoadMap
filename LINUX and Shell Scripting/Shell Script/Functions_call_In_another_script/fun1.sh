#!/bin/bash
add()
{
    echo "Adding Two numbers"
    echo `expr $1 + $2`
}
sub()
{
    echo "Subtracting two numbers" 
    echo `expr $1 - $2`
}
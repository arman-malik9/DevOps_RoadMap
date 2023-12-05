#!/bin/bash

#if and else statement.
val=10
if [ $val == 10 ] 
then
    echo "Value is equal"
else
    echo "value is no equal"
fi

#if-elif-else statement
x=20
y=55
if [ $x == $y ]
then 
    echo "x and y are equal"
elif [ $x \> $y ]
then 
    echo "x is greater then y"
else
    echo "y is greater then x"
fi


#Nested if statment.
a=10
b=2
if [ $a == 10 ]
then
    if [ $b == 5 ]
    then 
        echo `expr $a + $b`
    else
        echo `expr $a \* $b`
    fi
else
    echo "cannot print anything" 
fi
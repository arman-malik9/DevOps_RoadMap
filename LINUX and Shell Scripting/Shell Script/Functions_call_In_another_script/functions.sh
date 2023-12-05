#!/bin/bash

#creating a function
Hello() 
{
    echo "I am DevOps Engineer"
}
#Invoking a function
Hello

#passing the parameters.
MyFun()
{
echo "I am $1 $2"
}
#Invoking a function
MyFun Arman Malik

#return statement in functions.
Person()
{
    echo "Hello $1 $2"
    return 25
}

#Invoking a function
Person Arman Malik
#capturing the return value
ret=$?
echo "You got ${ret}% discount"


#Nested Functions: calling one function in an another function.

First()
{
    echo "I am from 1st function"
}
Second()
{
    First # calling first() function inside second function.
    echo "I am from 2nd Function"
}
#Invoking second fucntion.
Second
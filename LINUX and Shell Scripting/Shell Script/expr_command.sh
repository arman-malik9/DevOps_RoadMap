#!/bin/sh

# Author : Arman Malik
# Script follows here:
# expr 2 + 4 #there must be space around opertors like +, *, - etc.
# expr 12 \* 2

#Performing operations on variables inside a shell script
echo "Enter two numbers"
read x 
read y
sum=`expr $x + $y` #x=2 and y=5
echo "Sum = $sum"

#Comparing two expressions
x=10
y=20

# matching numbers with '='
res=`expr $x = $y`
echo $res

# displays 1 when arg1 is less than arg2
res=`expr $x \< $y`
echo $res

# display 1 when arg1 is not equal to arg2
res=`expr $x \!= $y`
echo $res



####  Evaluating boolean expressions   ####
# OR operation
$expr   "geekss"  "<"  5  "|"  19  -  6  ">"  10


# AND operation
$expr  "geekss"  "<"  5  "&"  19  -  6  ">"  10

#Finding length of a string
x=geeks

len=`expr length $x`
echo $len

#Finding substring of a string
x=geeks

sub=`expr substr $x 2 3` 
#extract 3 characters starting from index 2
echo $sub


#Matching number of characters in two strings
expr geeks : geek


#!/bin/bash

#while loop
a=1
# Iterating the loop until and less than 11.
while [ $a -lt 11 ]
do
    #printing the values.
    echo $a

    #inceamenting the value of a by 1
    a=`expr $a + 1` #or ((a++))
done

#for loop
for a in 1 2 3 4 5 6 7 7 8 9 10
do
    echo $a
done

#until loop
a=0
# -gt is greater than operator
#Iterate the loop until a is greater than 10
until [ $a -gt 10 ]
do
    # Print the values
    echo $a
     
    # increment the value
    a=`expr $a + 1`
done

#break and continue statements.

Example of break
c=0
while [ $c -lt 10 ]
do
    if [ $c == 6 ]
    then
        break 
    fi
    echo $c
    c=`expr $c + 1`
done

#Example of continue.

NUMS="1 2 3 4 5 6 7"
for NUM in $NUMS
do
   Q=`expr $NUM % 2`
   if [ $Q -eq 0 ]
   then
      #echo "Number is an even number!!"
      continue
   fi
   echo $NUM
done

# Example of Case statemnet.

echo "Which color do you like best?"
echo "1 - Blue"
echo "2 - Red"
echo "3 - Yellow"
echo "4 - Green"
echo "5 - Orange"
read color;
case $color in
  1) echo "Blue is a primary color.";;
  2) echo "Red is a primary color.";;
  3) echo "Yellow is a primary color.";;
  4) echo "Green is a secondary color.";;
  5) echo "Orange is a secondary color.";;
  *) echo "This color is not available. Please choose a different one.";; 
esac
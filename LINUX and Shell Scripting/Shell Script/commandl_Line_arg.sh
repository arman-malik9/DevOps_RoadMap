#!/bin/bash

#arg start with the index of 0, but in this script we defined from 1, why?
# because 0th argument takes the file name.
#for example: bash myexample.sh arg1 aerg2 .....
echo "Displaying posionnal parameters"
echo "Argument 1: $1"
echo "Argument 2: $2"
echo "Argument 3: $3"
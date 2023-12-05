#!/bin/sh
#Assigning a command to a variable

#ex 1
var=$(mkdir -p arman/malik)
echo $var

#ex 2
treeI=$(sudo apt install tree -y)
echo $treeI
echo "tree pkg Installed"

#ex 3
treeU=$(sudo apt remove tree -y)
echo $treeU
echo "tree pkg Uninstalled"

#storing output to a variable.
output=$(which git) 
echo $output
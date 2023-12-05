#!/bin/sh
#If you declare variable var1 in parent processof linux but the scope is limit to the parent 
#command you won't be able to access var1 in child process.
#To access the var1 in child process, export command is used.


echo $var1
a = 33
b = 200
if b > a:
  print("b is greater than a")

#Indentation
#Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. \
# Other programming languages often use curly-brackets for this purpose.

#Elif
#The elif keyword is Python's way of saying "if the previous conditions were not true, then try 
# this condition".

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#Else
#The else keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#Short Hand If
if a > b: print("a is greater than b")


#Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")

#The pass Statement
#if statements cannot be empty, but if you for some reason have an if statement with no content, 
# put in the pass statement to avoid getting an error.

a = 33
b = 200

if b > a:
  pass
# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.

# ExampleGet your own Python Server
# Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i += 1
#Note: remember to increment i, or else the loop will continue forever.

# The break Statement
# With the break statement we can stop the loop even if the while condition is true:

# Example
# Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:

# Example
# Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


#   Python For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


#Looping Through a String
#Even strings are iterable objects, they contain a sequence of characters:
for x in "banana":
  print(x)

#   The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

for x in range(6):
  print(x)
#Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

#The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
#Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)

#The pass Statement
#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass
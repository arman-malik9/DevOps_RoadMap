# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.
# Exception Handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement:

# Example 1:
try:
    print(x)  #x is not defined anywhere in this code, so it will show an exception.
except:
    print("Exeception occured")

#Example 2:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


  #Example 3:
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")




# Raise an exception
# As a Python developer you can choose to throw an exception if a condition occurs.

# To throw (or raise) an exception, use the raise keyword.
# Example
# Raise an error and stop the program if x is lower than 0:
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")


# Raise a TypeError if x is not an integer:
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")

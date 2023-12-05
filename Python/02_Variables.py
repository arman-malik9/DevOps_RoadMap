#Python Variables.

age=25
firstName="Arman"
lastName="Malik"
print("Hi, my name is", firstName, lastName, "and I am", age, "years old.")

#Variables do not need to be declared with any particular type, 
# and can even change type after they have been set.
x=10    #x is a type of int.
x="City"    #now x is a type of sring
print(x)

#Casting
print("Casting")
x=str(5) #x will be '5'
y=int(5) #y will be 5
z=float(5) #z will be 5.0
print(x, y, z)


#Get the Type
#You can get the data type of a variable with the type() function.
print("You can get the data type of a variable with the type() function.")
x=667
y="world"
z=3.5
print(type(x))
print(type(y))
print(type(z))

# Single or Double Quotes?
# String variables can be declared either by using single or double quotes:

x="Arman" 
#or
x='Arman' #both are same thing

#Assign multiple values.
x,y,z, age = "Mohmmad", "Arman", "Malik", 25
print(x)
print(y)
print(z)
print(age)

#you can assign the same value to multiple variables in one line:
x=y=z = "Noida"
print(x)
print(y)
print(z)

#Unpack a Collection
#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = 5
y = "John"
#print(x + y)  #it will show an error
print(x,y) # this will not show any error

#Global Varibale
print('Global Varibale')
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#If you create a variable with the same name inside a function, this variable will be local, 
# and can only be used inside the function. The global variable with the same name will remain as it was,
#  global and with the original value.
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#The global Keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
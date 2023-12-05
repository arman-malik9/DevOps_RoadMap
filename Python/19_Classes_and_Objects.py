# Python Classes/Objects
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

class Myclass:
    x=20

obj = Myclass()
print(obj.x)


# The __init__() Function
# The examples above are classes and objects in their simplest form, and are not really useful in real 
# life applications.
# To understand the meaning of classes we have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that
#  are necessary to do when the object is being created:

#Example
#Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
    def __init__(self, id, name, city):
        self.id = id
        self.name = name
        self.city = city

p1 = Person(10,'Arman','Noida')
print(p1.id, p1.name, p1.city)


#Note: The __init__() function is called automatically every time the class is being used to create a new object.

# The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:

# Example
# The string representation of an object WITHOUT the __str__() function:


class Person:
    def __init__(self,id, name, city):
        self.id = id
        self.name = name
        self.city = city

    def __str__(self):  #it is some like toString method in Java.
        return f"{self.id} {self.name} {self.city}{self.id}"
    
p1 = Person(30,'Huzefa','GZB')
print(p1)

# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.

# Let us create a method in the Person class:


class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city
    
    def myFunction(self):
        print("Good Morning Mr." , self.name)
    def details(self):
        return "Name: "+self.name+"\nCity: "+self.city

p3 = Person("Arman", "Delhi")
p3.myFunction()

print(p3.details())

#Note: The self parameter is a reference to the current instance of the class, and is used to 
# access variables that belong to the class.

# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

# Example
# Use the words mysillyobject and abc instead of self:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()


# Modify Object Properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.age = 40
print(p1.age)


#Delete Object Properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
del p1.age
print(p1.age)

#Delete Objects
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
del p1
print(p1)


# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, 
# put in the pass statement to avoid getting an error.

class Person:
  pass

# having an empty class definition like this, would raise an error without the pass statement

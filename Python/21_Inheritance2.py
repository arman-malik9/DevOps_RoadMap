# Add the __init__() Function
# So far we have created a child class that inherits the properties and methods from its parent.
# We want to add the __init__() function to the child class (instead of the pass keyword).
# Note: The __init__() function is called automatically every time the class is being used to create a new object.  

class Person:
    def __init__(self, name, city):
        self.name=name
        self.city=city

class Student(Person):
    def __init__(self, name, city, email):
        Person.__init__(self, name, city)
        #or
        # super().__init__(name, city)
        # self.email = "arman01@gmail.com"
        self.email = email


object = Student("Arman", "Noida", "arman01@gmail.com")
print(object.name, object.city,object.email)
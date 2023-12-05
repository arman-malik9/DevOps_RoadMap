# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

#Example of Single Inheritance.
# class A:
#     def displayA(self):
#         print("Welcome to A family")

# class B(A):
#     def displayB(self):
#         print("Wlecome to B family")

# ob = B()
# ob.displayA()
# ob.displayB()

#Example of Mutlilevel inheritance
# class A:
#     def displayA(self):
#         print("Welcome to A family")

# class B(A):
#     def displayB(self):
#         print("Wlecome to B family")

# class C(B):
#     def displayC(self):
#         print("Welcome to C family")

# ob = C()
# ob.displayA()
# ob.displayB()
# ob.displayC()

#Example of Multiple Inheritance
class A:
    def displayA(self):
        print("Welcome to A family")

class B:
    def displayB(self):
        print("Wlecome to B family")

class C(A,B):
    def displayC(self):
        print("Welcome to C family")

ob = C()
ob.displayA()
ob.displayB()
ob.displayC()
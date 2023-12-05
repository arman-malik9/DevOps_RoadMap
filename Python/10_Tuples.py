# Tuple
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "male")


#The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

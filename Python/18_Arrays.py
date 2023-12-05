#Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
#Note: This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.
#reate an array containing car names:

cars = ["Ford", "Volvo", "BMW"]
print(cars)
print(cars[0])
print(cars[1])
print(cars[2])

#Modify the value of the first array item:
cars[1]='Maruti'
print(cars)

#The Length of an Array
print(len(cars))

#Looping Array Elements

for x in cars:
    print(x)


# Adding Array Elements
# You can use the append() method to add an element to an array.

cars.append('Suzuki')
cars.append('KIA')
print(cars)


#Removing Array Elements
#You can use the pop() method to remove an element from the array.

cars.pop(1)
print(cars)


#You can also use the remove() method to remove an element from the array.

cars.remove('Suzuki')
print(cars)



#Array Methods
# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
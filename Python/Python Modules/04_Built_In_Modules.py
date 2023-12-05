import platform
x = platform.system()
y = dir(platform)

print(x)
print(y)

# Import From Module
# You can choose to import only parts from a module, by using the "from" keyword.
from MyModule import find

print(find("Malik"))
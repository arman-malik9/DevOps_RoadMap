#Getter and Setter

class Details:
    def __init__(self):
        self.__name =""    #This is the private variable in Python you can access only using getter and setter.
        self.__mob =""
        self.__age =0

    def setName(self,name):
        self.__name= name

    def getName(self):
        return self.__name

    def setMob(self,mob):
        self.__mob= mob
    def getMob(self):
        return self.__mob

    def setAge(self,age):
        self.__age= age
    def getAge(self):
        return self.__age


obj = Details()
obj.setName("Arman")
obj.setAge(25)
obj.setMob("9867554199")
print(obj.getName(), obj.getAge(), obj.getMob())
    

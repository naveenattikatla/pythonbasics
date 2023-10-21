class Student:
    def __init__(self , name , marks): # constructor with no return type 
        self.name = name
        self.__marks = marks
    def getValues(self): # self says about which object you are pointing to 
        return { "Name" :  self.name , 'marks' :  self.__marks } 
    # providing setters and getters to work with data - encapsulation
    def setName(self, name):
        self.name = name
    def setMarks(self , marks):
        self.__marks = marks

# object is an instance of a class

obj =  Student("Naveen", 50) # constrcuor will be called automatically when an object is created

obj.setName("Praveen")
obj.setMarks(90)

print(obj.getValues())
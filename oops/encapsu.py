class School:
    def __init__(self , name):
        self.__name = name

    def setName(self , name): # to set the  name 
        self.__name = name
    def getName(self): # to get the name
        return self.__name


obj  = School(" HIIN    ")
obj.setName("M p p  school")
print(obj.getName())
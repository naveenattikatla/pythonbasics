class parent:
    def __init__(self):
        print("Parent constructor !")
    def GetInfo(self):
        print("GetInfo from Parent")

class student(parent):
    def __init__(self):
        print("Student constructor !")
    def GetInfo(self):
        print("GetInfo from Student")

obj = parent()

obj.GetInfo()
# Note ,  No method overloading concept in python
# but We have mehtod overriding concept in python

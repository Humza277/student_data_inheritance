class Student:
    def __init__(self, name, city, classes):
        self.name = name
        self.__city = city
        self.classes = classes

    def printvalues(self):
        print("Your name is " + self.name)
        print("Your name is " + self.__city)
        print("Your name is " + self.classes)


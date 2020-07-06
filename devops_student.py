from student_data import *

class DevOPs(Student):
    def __init__(self, name, city, classes, sql):
        super().__init__(name, city, classes)
        self.sql = sql

    def printdevops(self):
        self.printvalues()
        print("You have learned " + self.sql)


d = DevOPs("Humza", "London", "Computer Science", "SQL")
d.printdevops()
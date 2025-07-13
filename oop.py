# we will study about OOP concept including class and many more

# class Student:
#     marks = 79
#     name = 'jimmy'
#     def getMarks(self):
#         return self.marks
#
# jimmy = Student()
# print("Marks of student : ", jimmy.getMarks())


# constructors

class Employee:
    def __init__(self,name,paycheck):
        self.name = name
        self.paycheck = paycheck

employee = Employee('James',2349)
print(employee.name)
print(employee.paycheck)

employee2 = Employee('Jony',99349)
print(employee2.name)
print(employee2.paycheck)
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name=",self.name)
        print("age=",self.age)
class test(student):
    def __init__(self,mark):
        self.mark=mark
    def displaymark(self):
        print("mark=",self.mark)
class dept(test):
     def __init__(self,name,deptment):
         self.depatment=deptment
     def displaydetails(self):
        print("department=",self.deptment)
name=input("enter name=")
age=input("enter age=")
mark=input("enter mark=")
deptment=input("enter department")
obj_dept=dept(name,age)
obj_dept.display()
obj_dept.displaymark()
obj_dept.displaydetails()

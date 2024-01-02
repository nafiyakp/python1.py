class student:
    def __init__(self,roll,name,course):
        self.roll=roll
        self.name=name
        self.course=course
    def display(self):
        print("roll no=",self.roll)
        print("name=",self.name)
        print("course=",self.course)
    def __del__(self):
        class_name=self.__class__.__name__
        print(class_name,"distroyed")
stud1=student(10,"afi","mca")
stud1.display()
at=getattr(stud1,"name")
print("getattr(stud1,'name'):",at)
print("hasattr(stud1,age):",hasattr(stud1,'age'))
print("setattr(stud1,age,21):",setattr(stud1,'age',21))
stud1.display()
print("age=",stud1.age)
del stud1

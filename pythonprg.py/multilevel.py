class student:
    def __init__(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
    def details(self):
        print(self.rollno)
        print(self.name)
        print(self.course)
class test(student):
    def __init__(self,rollno,name,course,mark):
        super().__init__(rollno,name,course)
        self.mark=mark
    def marks(self):
        print(self.mark)
class result(test):
    def __init__(self,rollno,name,marks,grade):
        super().__init__(rollno,name,course,mark)
        self.grade=grade
    def calculateGrade(self):
        if self.mark>50:
           self.grade="destiction"
        elif self.mark<50:
             self.grade="pass"
        else:
           self.grade= "failed"
        print("result=",self.grade)
rollno=input("enter rollno")
name=input("enter name:")
course=input("enter course:")
mark=(int(input("enter marks:")))
obj_stud1=result(rollno,name,course,mark)
obj_stud1.details()
obj_stud1.marks()
obj_stud1.calculateGrade()

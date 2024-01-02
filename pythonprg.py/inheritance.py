class student:
    def getdata(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
    def displaydetails(self):
        print("roll no=",self.rollno)
        print("name=",self.name)
        print("course=",self.course)
class test(student):
    def getmarks(self,marks):
        self.marks=marks
    def displaymarks(self):
        print("totalmark=",self.marks)
r=input("enter rollno")
n=input("enter name:")
c=input("enter course:")
m=input("enter mark:")
obj_stud1=test()
obj_stud1.getdata(r,n,c)
obj_stud1.getmarks(m)
obj_stud1.displaydetails()
obj_stud1.displaymarks()

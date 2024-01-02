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
class sports:
    def getsportsmark(self,spmarks):
        self.spmarks=spmarks
    def display_spmarks(self):
        print("sports marks=",self.spmarks)
class result(test,sports):
    def calculateGrade(self):
       m=self.marks+self.spmarks
       if m>500:self.grade="destinction"
       elif m<400:self.grade="pass"
       else:self.grade="fail"
       print("result=",self.grade)
r=input("enter rollno")
n=input("enter name:")
c=input("enter course:")
m=int(input("enter marks:"))
s=int(input("enter sports mark:"))
obj_stud1=result()
obj_stud1.getdata(r,n,c)
obj_stud1.getmarks(m)
obj_stud1.getsportsmark(s)
obj_stud1.displaydetails()
obj_stud1.displaymarks()
obj_stud1.display_spmarks()
obj_stud1.calculateGrade()

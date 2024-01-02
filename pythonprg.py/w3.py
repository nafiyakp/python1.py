class  personal:
    def __init__(self,name,age):
          self.name=name
          self.age=age
   
    def display(self):
        print("name=",self.name)
        print("age=",self.age)
class qualification:
    def __init__(self,degreename,totalmark,percentage):
        self.degreename=degreename
        self.totalmark=totalmark
        self.percentage=percentage
    def get(self):
        return self.degreename
        return self.totalmark
        return self.percentage
    def display(self):
        print("degree name=",self.degreename)
        print("total markk=",self.totalmark)
        print("percentage=",self.percentage)
count=1
while count==1:
      name=input("enter name:")
      age=input("enter age:")
      degreename=input("enter degree name:")
      totalmark=input("enter total mark:")
      percentage=input("enter percentage:")
      obj=personal(name,age)
      obj.display()
      obj2=qualification(degreename,totalmark,percentage)
      obj2.display()

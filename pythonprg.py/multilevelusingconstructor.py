class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name=",self.name)
        print("age=",self.age)
class embloyee(person):
      def __init__(self,name,age,emp_id):
          super().__init__(name,age)
          self.id=emp_id
      def emp_details(self):
          print(self.id)
class department(embloyee):
    def __init__(self,name,age,emp_id,dept_name):
        super().__init__(name,age,emp_id)
        self.dept_name=dept_name
    def dept_details(self):
        print(self.dept_name)
name=input("enter name=")
age=input("enter age=")
emp_id=input("enter id=")
dept=input("enter deptment=")
obj_dept=department(name,age,emp_id,dept)
obj_dept.display()
obj_dept.emp_details()
obj_dept.dept_details()

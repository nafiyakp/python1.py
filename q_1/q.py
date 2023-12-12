import math
class circle:
    def __init__(self,r):
        self.radius=r
    def area_circle(self):
          return (math.pi)*(self.radius)**2
    def perimeter_circle(self):
         return 2*(math.pi)* (self.radius)
    def display(self):
        print(self.area)
        print(self.perimeter)
        
r1=int(input("enter the radius of first circle:"))
r2=int(input("enter the radius of second circle:"))
obj_c1=circle(r1)
obj_c1=circle(r2)
a1=obj_c1.area_circle()
p1=obj_c1.perimeter_circle()
a2=obj_c1.area_circle()
p2=obj_c1.perimeter_circle()
if(a1>a2):
    print("first circle is bigger")
else:
    print("second circle is bigger")
if(p1>p2):
    print("perimeter of first circle is bigger")
else:
    print("peimeter of second circle is bigger")



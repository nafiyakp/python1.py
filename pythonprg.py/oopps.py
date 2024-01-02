class shape:
    def __init__(self):
        pass
    def circle_area(self,r):
        area=pi*r**2
        return area
    def rectangle_area(self,l,b):
        area=l*b
        return area
from math import pi
r=int(input("enter radius:"))
l=int(input("enter length:"))
b=int(input("enter bredth:"))
obj_area=shape()
circle_area=obj_area.circle_area(r)
print(circle_area)
rectangle_area=obj_area.rectangle_area(l,b)
print(rectangle_area)

r=int(input("enter radius:"))
l=int(input("enter length:"))
b=int(input("enter bredth:"))
obj_area2=shape()
circle_area=obj_area.circle_area(r)
print(circle_area)
rectangle_area=obj_area.rectangle_area(l,b)
print(rectangle_area)

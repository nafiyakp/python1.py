triangle=lambda b,h:0.5*b*h
l=int(input("enter the base of triangle"))
b=int(input("enter the height of triangle"))
print("area of triangle is",triangle(l,b))
square=lambda a:a*a
a=int(input("enter the sides of square"))
print("area of square",a,"is",square(a))
rectangle=lambda l,b:l*b
l=int(input("enter length"))
b=int(input("enter breadth"))
print("area of rectangle","is",rectangle(l,b))
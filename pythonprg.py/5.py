d={1:"nafi",2:"agisa",3:"5"}
d2={3:"naji"}
print(d.keys())
print(d.values())
del d[2]
print(str(d))
print(d)
d.update(d2)
print(d)
print(d.items())
d.clear()
print(d)
d.update(d2)
print(d)

values=input("enter coma separated nos:")
list=values.split(",")
print(list)
print(tuple(list))
l=[1,3,10]
print(max(l))



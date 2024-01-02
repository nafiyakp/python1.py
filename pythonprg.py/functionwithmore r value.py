def calc(a,b):
    sum=a+b
    diff=a-b
    pro=a*b
    return (sum,diff,pro)
a=int(input("enter first no"))
b=int(input("enter second no"))
sum,diff,pro=calc(a,b)
print("sum:",sum)
print("diffrence:",diff)
print("product",pro)

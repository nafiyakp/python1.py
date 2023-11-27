sum=0
list=[]
n=int(input("enter number of elements"))
print("enter elelments")
for i in range(0,n):
            element=int(input())
            list.append(element)
print(list)
for i in list:
    sum=sum+i
print(sum)
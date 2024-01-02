list=input("enter coma separated no.s")
list1=map(int,list.split(","))
print(list1)
sum=0
for i in list1:
    sum+=i
print(sum)


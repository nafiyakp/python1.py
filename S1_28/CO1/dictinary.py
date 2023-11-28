dict={}
n1=int(input("total number of elements in ict1:"))
for i in range(n1):
    dict[i]=input("enter elements:")
print(sorted(dict.items(),key=lambda kv:(kv[1],kv[0])))
print(sorted(dict.items(),key=lambda kv:(kv[1],kv[0], reverse=true))

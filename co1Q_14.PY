n=int(input("enter a number:"))
result=0
for i in range(1,n+1):
    print(n**i)
    result=result+n**i
print(result)
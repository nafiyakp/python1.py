
def oddeven(x):
    if(x%2==0):
        print("even")
    else:
        print("oddd")
n=int(input("enter a number"))
oddeven(n)

#
def string(s,n):
   return(s*n)

s1=input("enter string")
n=int(input("enter copie"))
print("the final string is",string(s1,n))
#
def true(a,b):
    if(a==b):
       print("true")
    elif (a+b==5):
        return true
    elif(a-b==5):
        return true
    else:
        return false
n1=int(input("enter first num:"))
n2=int(input("enter second  num:"))
print("result=",true(n1,n2))

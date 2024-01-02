def gcd(a,b):
    for i in range(1,min(a,b)+1):
        if(a%i==0 and b%i==0):
            gcd=i
    print(gcd)
n1=int(input("enter first num"))
n2=int(input("enter second num"))
gcd(n1,n2)
def factors(n):
    for i in range(1,n+1):
        if (n%i==0):
            print(i)

n1=int(input("enter  num"))
factors(n1)
#
def binary(n):
    if(n>=1):
       binary(n//2)
    print(n,end=" ")
n=int(input("enter a number"))
binary(n)

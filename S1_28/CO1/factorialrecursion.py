def fact(x):
    if x==1:
        return 1
    else:
        return(x*fact(x-1))
n=int(input("enter a number"))
if n>1:
    print("the factorial of",n,fact(n))

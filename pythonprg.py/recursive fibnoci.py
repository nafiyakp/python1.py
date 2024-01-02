def fibnocci(n):
    if n<=1:
      return n
    else:
        return (fibnocci(n-1)+fibnocci(n-2))
n=int(input("enter a num"))
print("fibnocci series")
for i in range(n):
              print(fibnocci(i))

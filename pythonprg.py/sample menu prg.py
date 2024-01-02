choice=0
a,b=3,4
while choice!=2:
    print("menu:")
    print("1.addition")
    print("2.sub")
    choice=int(input("enter choice"))
    if(choice==1):
       print("sum of",a,"and",b,"is",a+b)
    if(choice==2):
       print("diff of",a,"and",b,"is",a-b)
          

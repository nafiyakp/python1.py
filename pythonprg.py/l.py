def common(list1,list2):
    result=False
    for x in list1:
        for y in list2:
            if x==y:
                result=True
    return result
list1=input("enter first list=")
list1=list(list1.split())
list2=input("enter second list=")
list2=list(list2.split())
result=common(list1,list2)
print(result)

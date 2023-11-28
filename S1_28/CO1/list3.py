list=[]
n=int(input('enter the no. of elements'))
print('enter the elements')
for i in range(0,n):
    element=int(input())
    list.append(element)
print(list)
for i in range(len(list)):
    if list[i]>100:
        list[i]="over"
print(list)

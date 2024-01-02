count=0
v="aeiouAEIOU"
s=input("enter a string:")
for i in s:
    if i in v:
       count+=1
print("the no of vowels",count)

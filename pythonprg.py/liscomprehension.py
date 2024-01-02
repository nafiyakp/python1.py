list=[1,2,3,4,5,6]
list=[x for x in list if x%2==0]
print(list)
f=["apple","orange","banana"]
b="banana"
fruit=[ x for x in f if b in x]
print(fruit)
n=8
list1=[x**2 for x in range(n+1)]
print("the square of number is:",list1)
w=input("enter a word")
vowel="aeiouAEIOU"
list=[ x for x in w if x in vowel]
print(list)
#3)d
word="how are you"
print("the enterd word is ",word)
list1=[ord(value)for value in word]
print("the ordinal values",list1)
#word in a string
word=input("enter a word")
s=input("enter a string")
count=0
a=s.split(" ")
for i in range(0,len(a)):
    if(a[i]==word):
       count+=1
print("count is",count)
#

count=0
list=["Anu","nafi","ammu","najiya"]
for x in list:
       count+=x.lower().count("a")
print(count)
#
list=[]
n=int(input("enter the number of words:"))
for i in range(0,n):
    words=input("enter a word:")
    list.append(words)
print(list)
x=max(list)
print(x)
print("the length of longest word is:",len(x))

# for loop
a=[]
n=int(input("enter the number"))
for i in range(n):
    b=input("enter the value")
    a.append(b)
c=input("enter value to insert")
index=int(input("enter index where you want to insert"))
a.insert(index,c)
print(a)


# while loop 
a=[]
n=int(input("enter the number"))
i=0
while i<n:
    b=input("enter the value")
    a.append(b)
    i=i+1
c=input("enter value to insert")
index=int(input("enter index where you want to insert"))
a.insert(index,c)
print(a)
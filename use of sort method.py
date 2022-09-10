# for loop 
a=[]
n=int(input("enter the number"))
for i in range(n):
    b=input("enter the value")
    a.append(b)
a.sort()
print(a)


# while loop 
a=[]
n=int(input("enter the number"))
i=0
while i<n:
    b=input("enter the value")
    a.append(b)
    i=i+1
a.sort()
print(a)
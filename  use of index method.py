# for loop 
n=int(input("enter the number"))
a=[]
for i in range(n):
    x=input("enter value")
    a.append(x)
x=input("enter value to find index")
z=a.index(x)
print("Index=",z)



# while loop 
n=int(input("enter the number"))
a=[]
i=0
while i<n:
    x=input("enter value")
    a.append(x)
    i=i+1
x=input("enter value to find index")
z=a.index(x)
print("Index=",z)

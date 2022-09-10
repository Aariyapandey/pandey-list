# for loop 
a=[]
n=int(input("enter the max size:-"))
for i in range(n):
    b=input("enter the value")
    a.append(b)
print("Original list is",a)
print("Max value in the list is",max(a))
print("Min value in list",min(a))


# while loop 
a=[]
n=int(input("enter the max size:-"))
i=0
while i<n:
    b=input("enter the value")
    a.append(b)
    i=i+1
print("Original list is",a)
print("Max value in the list is",max(a))
print("Min value in the list",min(a))
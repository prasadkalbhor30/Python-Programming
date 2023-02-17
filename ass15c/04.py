str=input("Enter a string :")
c=input("Enter which character you want to count :")
k=0
for i in str:
    if i==c:
        k+=1
print(c,"=",k)

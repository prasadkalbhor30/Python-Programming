n=int(input("enter how many prime numbers you want to print :"))
l1=[]
num=1
k=1
while k<=n:
    i=num-1
    while i>1:
        if num%i==0:
            break
        i-=1
    if i==1:
        l1.append(num)
        k+=1 
    num+=1
print(l1)

n=int(input("enter how many prime numbers you want to print :"))
num=1
k=1
while k<=n:
    i=num-1
    while i>1:
        if num%i==0:
            break
        i-=1
    if i==1:
        print(num)
        k+=1 
    num+=1
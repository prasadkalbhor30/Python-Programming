#prime number 
num=int(input("Enter a number : "))
i=num-1
while i>1:
    if num%i==0:
        break
    i-=1
print("Prime number" if i==1 else "Not a prime number")
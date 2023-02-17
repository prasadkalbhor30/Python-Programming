# hcf
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
i=a-1
while i>1:
    if a%i==0 and b%i==0:
        break
    i-=1
print("hcf=",i)
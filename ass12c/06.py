# coprime or not
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
i=num1-1
while i>1:
    if num1%i==0 and num2%i==0:
        break
    i-=1
print("They are Co-prime numbers" if i==1 else "They are not Co-prime numbers")
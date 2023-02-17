b=""
n=int(input("Enter a number to reverse it : "))
while n!=0:
    b+=str(n%10)
    n=n//10
b=int(b)
print(b)
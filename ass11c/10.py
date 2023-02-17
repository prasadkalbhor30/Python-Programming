b=""
n=int(input("Enter a number to convert in binery : "))
while n>=8:
    b=str(n%8)+b
    n=n//8
b=str(n)+b
b=int(b)
print(b)
print(bin(n))
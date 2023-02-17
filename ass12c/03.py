#prime number
num,ed=int(input("Enter start and end value to print prime numbers between them\nStart= ")), int(input("End value = "))
while num<=ed:
    i=num-1
    while i>1:
        if num%i==0:
            break
        i-=1
    if i==1:
        print(num)
    num+=1
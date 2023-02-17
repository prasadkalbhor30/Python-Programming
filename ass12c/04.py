#prime number 
num=int(input("Enter a number to print next prime number : "))+1
while 1:
    i=num-1
    while i>1:
        if num%i==0:
            break
        i-=1
    if i==1:
        print(num)
        break
    else: 
        num+=1
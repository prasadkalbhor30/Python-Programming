#prime number
num=1
while num<=100:
    i=num-1
    while i>1:
        if num%i==0:
            break
        i-=1
    if i==1:
        print(num) 
    num+=1
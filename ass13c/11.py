l1=[int(i) for i in input("enter a numbers separated by space : ").split(" ")]
for i in range(len(l1)):
    j=i+1
    while j<len(l1):
        if l1[i]>l1[j]:
            c=l1[i]
            l1[i]=l1[j]
            l1[j]=c
        j+=1
print(l1)
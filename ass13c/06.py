# smallest number in a given list
l1=[int(i) for i in input("enter a numbers separated by space : ").split(" ")]
for i in l1:
    k=0
    for j in l1[l1.index(i)+1::]:
        if i>j:
            k+=1
            break
    if k==0:
        print(i)
        break
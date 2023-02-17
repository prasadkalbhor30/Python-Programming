# remove non integer elements from given list
l1=[eval(i) for i in input("enter a elements separated by space : ").split(" ")]
i=0
while i<len(l1):
    if type(l1[i]) is not int:
        l1.remove(l1[i])
        i-=1
    i+=1
print(l1)
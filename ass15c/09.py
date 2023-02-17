str=input("Enter a string :")
k=0
for i in range(len(str)):
    if str[i]==' ' and str[(i+1)]!=' ' and str[(i+1)]!=len(str):
        k+=1
print("words in given string = ",k+1)

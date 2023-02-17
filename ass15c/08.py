str=input("Enter a string :")
str1=""
i=0
while (i<len(str)):
    if i==0 and str[i]<'z' and str[i]>'a' or str[i-1]==' ' and str[i]<'z' and str[i]>'a' :
        str1+=chr(ord(str[i])-32)
    else:
        str1+=str[i]
    i+=1
print("string in capitalized form = ",str1)

str=input("Enter a string :")
str1=""
for i in str:
    str1+=chr(ord(i)+32) if i>'A' and i<'Z' else i
print("string in lowercase = ",str1)

str=input("Enter a string :")
str1=""
for i in str:
    str1+=chr(ord(i)-32) if i>'a' and i<'z' else i
print("string in uppercase = ",str1)

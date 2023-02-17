# write a Python script to calculate result
MARATHI,MATHS,HISTORY,ENGLISH,SCIENCE=int(input("ENTER THE MARKS OF 5 SUBJECTS OUT OF 100 \nMARATHI = ")),int(input("MATHS = ")),int(input("HISTORY = ")),int(input("ENGLISH = ")),int(input("SCIENCE = "))
marks=(MARATHI+MATHS+HISTORY+ENGLISH+SCIENCE)/5
if marks>35:
        print("YOU ARE PASS\nMARKS OBTAINED=",marks)
else:
        print("YOU ARE FAILED")
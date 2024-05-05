## accept marks from the user. Using if…….elif….  Else,  display whether result is  fail, pass, second class , first class, Distinction etc.

marks= int(input("Enter a students marks :"))
if 75 <=marks:
    print("Students marks are Distinction ")
elif 60 <=marks:
    print("Student marks are first class ")

elif 50 <=marks:
    print("students marks are second class")
elif 33 <=marks:
    print("Students marks are pass")

else:
    print("Students are fail")
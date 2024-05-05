##  accept a character and display whether it is upper case or lower case or not an alphabet.

char =input("Enter a character :")
if char.isalpha():
    if char.isupper():
        print("The character is uppercase")
    else:
        print("The character is lowercase")
else:
    print("The character is not an alphabet")
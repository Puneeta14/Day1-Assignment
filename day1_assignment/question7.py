## accept numbers till user enters 0 and display the total of all the numbers entered.

total =0

while True:
    number =int(input("Enter a number"))
    if number ==0:
        break
    total+=number

print("The total of all the numbers entered is :",total)
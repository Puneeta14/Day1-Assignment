##  accept a number and display whether it is prime or not

num =int (input("EEnter a number: "))

if num >1:
    for i in range(2, num):
        if (num % i)==0:
            print(num,"is not a prime number ")
            break
    else:
        print(num,"is a prime number ")

else:
    print(num,"is not a prime number ")
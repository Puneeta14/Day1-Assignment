##  display prime numbers from 3 to 30

def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num % i==0:
            return False
    return True
prime_numbers =[]   # loop to find prime numbers
for num in range(3,31):
    if is_prime(num):
        prime_numbers.append(num)

print("The prime numbers from 3 to 30 are :",prime_numbers)



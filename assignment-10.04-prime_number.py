# Task : Write a program that takes a number from the user and prints the result to check if it is a prime number.

num = int(input("Is it a prime number? : "))
if num < 2:
    print(f"{num} is not a prime number.")
else:
    x = list()
    for i in range(2,num):
        if num % i == 0:
            x.append(i)
    if len(x) != 0:
        print(f"{num} is not a prime number and divisible by:")
        for j in x:
            print(j)
    else:
        print(f"{num} is a prime number.")
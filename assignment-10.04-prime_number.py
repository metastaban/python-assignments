num = int(input("Is is a prime number?: "))
if num < 2:
    print(f"{num} is not a prime number.")
else:
     = list()
    for i in range(2,num):
        if num % i == 0:
            liste.append(i)
    if len(liste) != 0:
        print(f"{num} is not a prime number and divisible by:")
        for j in liste:
            print(j)
    else:
        print(f"{num} is a prime number.")

# Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements. 
fibonacci = [1,1]

while 55 not in fibonacci:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(fibonacci)
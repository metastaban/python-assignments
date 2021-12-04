#Task : Print the prime numbers which are between 1 to entered limit number (n)

def prime(n):
    primes = list()
    for i in range(2,n+1):
        div = list()
        for j in range(2,i+1):
            if i % j == 0:
                div.append(j)
        if len(div) == 1:
            primes.extend(div)
    return primes
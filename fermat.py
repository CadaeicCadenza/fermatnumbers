'''def isprime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
        else:
            return True

def constructible(x):
    for i in range(0,10000):
        if x == (2^(2^i))+1:
            return True
    return False

x = 5

while x < 100: 
    if isprime(x):
        if constructible(x):
            print(x)
    x = x+1'''

def isprime(number):
    if number == 1:
        return False
    for factor in range(2, number):
        if number % factor == 0:
            return False
    return True

def f(n):
    return 1 + (2 ** (2 ** n))

n = 1
limit = int(input())

while n < limit:
    if isprime(f(n)):
        print(f"{f(n)} is prime")
    else:
        print(f(n))
    n = n+1

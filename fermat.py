def p(x):
    return [i for i in range(1,x)if x%i==0]==[1]

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

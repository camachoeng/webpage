
def power(a, b):
    if b==0:
        return 1
    else:
        b-=1
        return a*power(a,b)

def disc_price(price):
    disc_price = price * 0.9
    return disc_price

def is_even(n):
    if n%2 == 0:
        return True
    return False

def myrecmap(function, lista):
    if not lista:
        return []

    return [function(lista[0])] + myrecmap(function, lista[1:])

def myrecfilter(function, lista):
    if not lista:
        return []
    if function(lista[0]):
        return [function(lista[0])] + myrecmap(function, lista[1:])
    else:
        return myrecmap(function, lista[1:])

def purify(lista):
    result = []
    for i in lista:
        if is_even(i):
            result.append(i)
    return result

def recursive_purify(lista):
    if not lista:
        return []
    if is_even(lista[0]):
        return [(lista[0])] + recursive_purify(lista[1:])
    else:
        return recursive_purify(lista[1:])

def product(lista):
    result = 1
    for i in lista:
        result*=i
    return result

def recursive_product(lista):
    if not lista:
        return 1
    return lista[0] * recursive_product(lista[1:])

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def recursive_collatz(n):
    if n == 1:
        return [1]
    if n%2 == 0:
        return [n] + recursive_collatz(n / 2)
    else:
        return [n] + recursive_collatz(3*n+1)

def fibonacci(n):
    if n==0 or n==1:
        return n
    fib1 = 0
    fib2 = 1
    for i in range(n-1):
        result = fib1 + fib2
        fib1 = fib2
        fib2 = result
    return result

def recursive_fibonacci(n):
    if n==0 or n==1:
        return n
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

n = 10

result = fibonacci(n)
print(result)


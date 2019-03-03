def sumatorio(n):
    if n > 0: 
        return n + sumatorio(n-1)
    return 0


print(sumatorio(15))

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return n

print(factorial(5))

    
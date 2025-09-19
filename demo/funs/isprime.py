
def isprime(num):
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False  # not a prime

    return True # prime


print( isprime(13), isprime(10000))


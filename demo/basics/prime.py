
num = int(input("Enter a number :"))

prime = True
for i in range(2, num // 2 + 1):
    if num % i == 0:
        print('Not a prime number')
        prime = False
        break

if prime:
    print('Prime Number')



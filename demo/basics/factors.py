
num = int(input("Enter a number :"))

found = False
for i in range(2, num // 2 + 1):
    if num % i == 0:
        found = True
        print(i)

if not found:
    print('Sorry! No factors found!')



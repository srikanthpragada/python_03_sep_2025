# Display largest factor

num = int(input("Enter a number :"))

for i in range(num // 2, 0, -1):
    if num % i == 0:
        print(i)
        break

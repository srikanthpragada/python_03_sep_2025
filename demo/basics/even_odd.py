
even_count = 0
for i in range(10):
    n = int(input("Enter number [0 to stop] :"))
    if n == 0:
        break  # terminate loop
    if n % 2 == 0:
        even_count += 1

print('Even Count = ', even_count)


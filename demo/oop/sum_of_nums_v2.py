total = 0
while True:
    try:
        num = int(input("Enter number [0 to stop]: "))
        if num == 0:
            break
        total += num
    except ValueError:
        print("Invalid Number. Try again!")

print(f"Total = {total}")


try:
    num = int(input("Enter a number :"))
    print(100 / num)
except ValueError as ex:
    print('Invalid Number')
# except ZeroDivisionError:
#     print("Zero is not a valid input!")
except Exception as ex:
    print(ex)


print("The End!")


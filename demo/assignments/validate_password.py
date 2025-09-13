
pwd = "Password2"
upper = digit = False

for c in pwd:
    if c.isdigit():
        digit = True
    elif c.isupper():
        upper = True

if upper and digit:
    print("Valid Password!")
else:
    print("Invalid Password!")

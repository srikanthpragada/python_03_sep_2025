
pwd = "Password2"
upper = digit = special =  False

for c in pwd:
    if c.isdigit():
        digit = True
    elif c.isupper():
        upper = True
    elif c in ['@', '#', '_']:
        special = True

if upper and digit and special:
    print("Valid Password!")
else:
    print("Invalid Password!")

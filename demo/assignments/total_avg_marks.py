
data = "90,77,85,45,89,78"
marks = data.split(',')
print(marks)

total = 0
for m in marks:
    total += int(m)

print(total, total // len(marks))


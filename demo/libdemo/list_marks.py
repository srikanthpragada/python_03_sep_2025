
f = open("marks.txt" , "rt")

for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue  # Ignore line and go top

    name = parts[0]
    marks = list(map(int, parts[1:]))
    total = sum(marks)
    print(f"{name:20}  {total:3} {total//len(marks):2}")


f.close()


f = open("marks.txt" , "rt")

for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue  # Ignore line and go top

    name = parts[0]
    # Remove parts that are not numbers
    numbers = filter(str.isdigit, parts[1:])
    # Convert all parts to int
    marks = list(map(int, numbers))
    total = sum(marks)
    print(f"{name:20}  {total:3} {total//len(marks):2}")


f.close()

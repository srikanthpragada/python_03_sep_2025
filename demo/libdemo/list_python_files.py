import os

g = os.walk(r"c:\classroom\sep1\demo")

total_count = 0
for dirname, dirs, files in g:
    print("*" * 10, dirname , '*' * 10)
    count = 0
    for f in files:
        if f.endswith(".py"):
            print(" " * 5, f)
            count += 1

    print("=" * 10, count, "=" * 10)
    total_count += count

print('#' * 10, total_count, "#" * 10)



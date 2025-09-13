
nums = []

while True:
    n = int(input("Enter number [0 to stop] :"))
    if n == 0:
        break

    if n not in nums:
        nums.append(n)
        
nums.sort(reverse = True)

for n in nums:
    print(n, end =  ' ')





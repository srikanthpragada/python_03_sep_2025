price = int(input("Enter price :"))
qty = int(input("Enter qty :"))

amount = price * qty
discount = amount * 15 // 100
after_discount = amount - discount

tax = after_discount * 5 // 100
net_amount = after_discount + tax

print(f'Amount        : {amount:8}')
print(f'- Discount    : {discount:8}')
print(f'After Discount: {after_discount:8}')
print(f'+ Tax         : {tax:8}')
print(f'Net Amount    : {net_amount:8}')



kw = int(input("Enter the KW hours used: "))

if kw <= 1000:
    amount = kw * 0.07633
else:
    amount = (1000 * 0.07633) + ((kw - 1000) * 0.09259)

print("Amount owed is $", amount)
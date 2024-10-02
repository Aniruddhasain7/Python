units = int(input("Enter the number of units consumed: "))

if units <= 100:
    bill = 0
elif units <= 200:
    bill = (units - 100) * 5
else:
    bill = (100 * 5) + (units - 200) * 10

print("Total bill amount is Rs:", bill)

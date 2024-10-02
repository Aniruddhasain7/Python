age = int(input("Enter age: "))
sex = input("Enter sex (M/F): ")
days = int(input("Enter number of days: "))

if 18 <= age < 30:
    if sex == 'M':
        wage = 700
    elif sex == 'F':
        wage = 750
elif 30 <= age <= 40:
    if sex == 'M':
        wage = 800
    elif sex == 'F':
        wage = 850
else:
    print("Enter appropriate age")
    wage = 0

if wage != 0:
    total_wage = wage * days
    print(f"Total wages: Rs {total_wage}")

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tips = int(input("How much tip would you like to give? 10, 12, or 15? "))
persons = int(input("How many people to split the bill? "))

personal_pay = round(total_bill * (1 + tips / 100) / persons, 2)

print(f"Each person should pay: ${personal_pay}")

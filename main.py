print("Welcome to the tip caculator.")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_bill = bill * (1+percentage/100)
people = int(input("How many people to split the bill? "))
tip = round(total_bill / people,2)
print(f"Each person should pay: ${str(tip)}")


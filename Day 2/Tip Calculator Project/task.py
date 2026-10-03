print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
bill_tip = tip/100*bill
total = bill_tip + bill
bill_total = total/people

print(f"Each person should pay: ${bill_total:.2f}")
print("Welcome to the tip calculator!")
bill_amt = float(input("What was the total bill amount? \n"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? \n"))
num_people = int(input("How many people to split the bill?\n"))
total_tip_amt = (bill_amt*(tip_percent/100))
total_amount = bill_amt + total_tip_amt
per_person_split = round(total_amount/num_people,2)
print(f"Each person should pay {per_person_split}")
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $ ")) 
tip = int(input("How much tip would you like to give? 10, 12, or 15? ")) / 100
total_person = int(input("How many people to split the bill? "))
total_bill_with_tip = total_bill * (1 + tip)
bill_per_person = round((total_bill_with_tip / total_person), 2)
print(f"Each person should pay: ${bill_per_person:.2f}")





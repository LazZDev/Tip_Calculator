name = "Welcome to the tip calculator."
print(name)

bill = float(input("What was the total bill? $"))

percentage = int(input("What percentage tip would you like to give? "))
tip = percentage / 100

adj_tip = bill * tip
total_bill = bill + adj_tip

splitted_people = int(input("How many people to split the bill? "))
adj_payment = total_bill / splitted_people

print(f"Each person should pay: ${round(adj_payment, 2)}")
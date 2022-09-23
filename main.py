print("Welcome to the tip calculator.")
bill = input("What was the total bill?")
tip = input("What percentage tip would would you like to give? 10,12 or 15?")
tip1= float(tip)
bill1 = float(bill)
new_tip =  (tip1/100)* bill1
new_bill= new_tip + bill1
people= input("How many people to split the bill?")
people1 = float(people)
Each_pay = round(new_bill/people1,2)
Each_pay = "{:.2f}".format(Each_pay)
print(f"Each person should pay ", Each_pay)

print("Welcome to my tip calculator")

total_bill = input("What was the total bill? $")

percentage_bill = input("What percentage tip would you like to give? 10, 12, or 15? ")

bill_split = input("How many people to split the bill? ")

bill = int(total_bill) + (int(percentage_bill) * int(total_bill))/100


print(f"Totat bill is : ${bill}")
amount_to_pay = float(bill) / int(bill_split)

final_bill = round(amount_to_pay,2)

print(f"Each person is to pay: ${final_bill}")
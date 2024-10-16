def tip_calculator():
    print("Welcome to the tip calculator!")
    total_bill = int(input("What was the total bill? "))
    tip = int(input("How much tip would you like to give? "))
    people = int(input("How many people are splitting the bill? "))
    individual_amount = round((total_bill + tip) / people, 2)
    print(f"Each person should pay {individual_amount}")


# tip_calculator()
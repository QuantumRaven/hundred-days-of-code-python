#!/usr/bin/env python3

print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill?: "))
tip_amount = float(input("How much tip would you like to give? 10%, 12%, or 15%: "))
people = int(input("How many people are splitting the bill?: "))
total = ((bill * tip_amount) + bill) / people
print(f"Each person should pay: {round(total, 2)}")

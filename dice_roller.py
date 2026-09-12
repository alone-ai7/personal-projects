import random

number = int(input("How many dices to roll? Choose 1-5: "))
sides = int(input("How many sides? (default 6, press Enter): ") or "6")   

total = 0
for i in range(number):
	roll = random.randint(1, sides)
	total += roll
	print(f"Die {i+1}: {roll}") 
print(f"\nTotal: {total}")   
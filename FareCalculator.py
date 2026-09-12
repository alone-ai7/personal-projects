name = input("What is your name: ")

isStudent = input("Are you a student? y/n: ")

if isStudent == "y":
	fare = 13 * 0.9
	print("You qualify for the fare discount! Please pay: ", f"{fare:.2f}","PHP")

elif isStudent == "n":
	print("You didn't qualify for the discount. Please pay the standard price: 13PHP")

else:
	print("Error!")
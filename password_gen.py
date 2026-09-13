import random   # gives us random.choice() to pick random characters
import string   # gives us ready-made lists of letters, numbers, symbols

#print(dir(random)) #to just check what files inside the module
#print(dir(string))

# Ask the user how long they want the password, convert answer to a number
length = int(input("How long do you want the password to be: "))

# Combine all 4 character lists into one big "pool" to pick from
pool = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

# Start with an empty string ""
password = ""

# Loop as many times as the user asked for
for i in range(length):
    # Pick one random character from the pool and add it to the password
    password += random.choice(pool)

# Print the finished password (outside the loop, so it only prints once)
print(password)   

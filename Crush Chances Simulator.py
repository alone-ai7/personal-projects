#A text base chat chances simulator 

#flow of the game

#==================================
#Show brief history and story
#How will you treat her for 14 days
#Her answer
#End
#==================================

import time

def showHistory():
    print("""
    You met this girl on the first day of class. She was the one helping the teacher pass out papers
    and she accidentally dropped them all and laugh it off. """)
    time.sleep(1)
    
    print("""
    You thought she was cool because she wasn't trying to be. Then you saw her again in the library,
    quietly drawing in her notebook instead of studying. """)
    time.sleep(1)
    
    print("""
    That's when it hit you. You didn't think she was pretty. You wanted to know what she was
    drawing. """)
    time.sleep(1)
    
    print("""
    Let's see if she feels the same. How will you treat her?""")

showHistory()

day = 1
affection = 0

def getChoice():
    print("Day: ", day)
    print(f"Affection: {affection}/100")
    print("1. Compliment Her")
    print("2. Ask to hangout")
    print("3. Give her something")
    print("4. Ignore her")
    print("5. Be clingy")
    choice = input("Enter the number of your choice: ")
    return choice

def calculateAffection(choice):
    global affection
    if choice == '1':
        affection += 10
        print("She smiled at your compliment", "\n" + "Your current affection: ", affection, "\n")
    elif choice == '2':
        affection += 5
        print("She agreed to hangout with you!", "\n")
    elif choice == '3':
        affection += 20
        print("She was happy because she likes what you gave her!", "\n")
    elif choice == '4':
        affection -= 30
        print("She's thinking why are you ignoring her", "\n")
    elif choice == '5':
        affection -= 35
        print("She did not like you being clingy", "\n")
    else:
        affection -=50
        print("Please input a valid number! I will punish you by deducting 50 affection points!")
        
while day <= 14 and affection < 100:
    user_pick = getChoice()
    calculateAffection(user_pick)
    day += 1
    time.sleep(1)
 
if affection >= 80:
    print("She said yes")
else:
    print("Game Over. Final affection: ", affection)
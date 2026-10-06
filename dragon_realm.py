#Dragon Realm Game
#Based on "Invent your own computer games with python, 4th edition" by Al Sweigart
#Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License


#flow chart

#start
#show introduction
#player chooses a cave
#check for friendly or hungry dragon
#player wins / player loses
#ask to play again
#end
import random, time #random for the randint()function, time module for time-related functions

def displayIntro():
    print("""You are in a land full of dragons.
    \rIn front of you, you see two caves. In one cave, the dragon is friendly
    \rand will share his treasure with you. The other dragon is greedy and 
    \rhungry, and will eat you on sight!""")
    
    print()
    
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2': #keep looping until the user type 1 / 2
        print("Which cave will you go into? (1 or 2)")
        cave = input()
        
    return cave
    
def checkCave(chosenCave):
    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    
    print("A large dragon jumps out in front of you! He opens his jaws and...")
    print()
    time.sleep(2)
    
    #deciding which cave has the friendly dragon
    friendlyCave = random.randint(1, 2)
    
    if chosenCave == str(friendlyCave):
        print("The dragon gave you his treasure")
        time.sleep(1)
    else:
        print("The dragon gobbles you in one bite!")
        time.sleep(1)
        
playAgain = "yes"
while playAgain == "yes" or playAgain == "y": #loop if the player typed yes or y
    displayIntro() #this goes back to intro 
    
    caveNumber = chooseCave()
    checkCave(caveNumber)
    
    print("Do you wanna play again? (yes or no)")
    playAgain = input()
    

# in line 24, we used != to specify the the user needs to answer just 1 or 2. So basically it traps them until they gave the right answer
# in line 51, we used == to say the user needs to answer y or yes to loop again, otherwise it will exit the program

#Notes: I added my own commens to help me learn more about the mechanics of this games
#Original code unchanged
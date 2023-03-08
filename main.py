print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 



#Chose the Direction and check steps and give prompts
direction=input("You have arrived to the road less travelled, which direction would you choose, Left or Right? ")


if (direction.lower()=="left"):
    step2 = input("Bravo! You have arrived at the river, would you like to Swim or Wait for the Boat?  ")
    if step2.lower() =="wait":
        step3 = input("Superb, You have arrived on the island, There are three houses with Red, Blue and Yellow Door? Where do you like to go to hunt tressure? ")
        if step3.lower()=="red": 
            print("Burned by fire. Game over")
        elif step3.lower()=="blue":
            print("Eaten by Beast. Game over")
        elif step3.lower()=="yellow":
            print("You Win!")
    else:
        print("Attacked by Dragons. Game over")
else:
    print(" Lions ahead! Right is not always right, Better luck next time. Game over")

print("""
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"'"-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`." ` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
      """)
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

print("You find yourself at a crossroads.")
direction = input("Do you go left or right?\n").lower()

if direction == "left":
    print("You come into a clearing, there are some paths branching out ahead and left and right.")
    dir = input("Where do you go?\n").lower()

    if dir == "ahead":
        print("You find a small delapitated house.")
        enter = input("Do you go inside? Y or N\n").lower()

        if enter == "n":
            print("You go around the back of the house and see a mountain ahead.")
            mountain = input("Do you go towards the mountain? Y or N\n")

            if mountain == "y":
                print("You get to the mountain and see a cave.")
                cave = input("Do you go in the cave? Y or N\n").lower()

                if cave == "y":
                    print("You find a chest! You open it and find jewels and gold in it! Let's hope it's not cursed...")
                else:
                    print("You wander around the mountain and are chased by mountain lions who want to eat you. Good luck!")

            else:
                print("You get hungry and find some mushrooms to eat. Now you can't remember what you were doing..")

        else:
            print("You enter and find a bed. You lie down and it feels like a cloud. You take a nap.")

    else:
        swim = input("You find a river. Do you swim across? Y or N\n").lower()
        if swim == "y":
            print("You make friends with an otter and forget about the treasure.")
        else:
            print("The sound of the river lulls you into a state of relaxation and you sit and meditate")
else:
    print("You come across a bear and she takes you to be her cuddly toy. You lose!")


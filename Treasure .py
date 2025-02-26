print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
print('''You find yourself at a diversion which leads to A left or A right
what will you do??''')
direction = input()
if direction.lower() == "left":
    print("Maybe your luck hasn't run out yet, you shall continue")
    print('''you are struck by the sight of a ever stretching river, what shall you do now 
     what will, you choose will you again take a gamble? Will you wait or will you continue into the wilderness
     all by your sheer strength and nothing more. What will you choose...''')
    decision1 = input()
    if decision1.lower() == "wait":
        print('''Sometimes patience is one of the most important skills a man can have. This very patience 
        of yours helped you evade a ferocious storm and easily ride a boat to the other end of the river. 
        But now you finally reach the land where you will either gain everything or lose everything
        you look ahead only to find 3 doors. 
        Red Green Blue, only one of them leads to the treasure or maybe all of them doo or maybe none of them
        what shall you decide. How will your fate unravel now, make your final decision. ''')
        final_decision = input()
        if final_decision.lower() == "":
            print('''very well mortal, you could think something out of the given pretext. You truly earned this 
            this journey of yours was truly entertaining for me. This is why you can have the treasure:
            and it is.............. Yeah its nothing :3''')
        else:
            print('''All this just to mess up at the final stage, you entertained me well mortal but this is your end
            farewell. ''')
    else:
        print('''you overestimate your own body's capabilities and aimed to reach something so out of your 
        grasp and where did it bring you? Nowhere but failure, as you remain just another soul 
        fallen in the path of reaching the treasure''')
else:
    print("you fell into a never ending hole")
# snake water gun, game

player = input("your turn: snake(s)  water(w)  gun(g)\n")
if player == "s":
    select = "snake"
elif player == "w":
    select = "water"
elif player == "g":
    select = "gun"

import random
rn = random.randint(1, 3)
if rn == 1:
    comp = "s"
elif rn == 2:
    comp = "w"
elif rn == 3:
    comp = "g"

if comp == "s":
    select2 = "snake"
elif comp == "w":
    select2 = "water"
elif comp == "g":
    select2 = "gun"


def logic():
    if player == comp:
        return("tie")
    elif player == "s":
        if comp == "w":
            return("you win!")
        elif comp == "g":
            return("you lose!")
    elif player == "w":
        if comp == "s":
            return("you lose!")
        elif comp == "g":
            return("you win!")
    elif player == "g":
        if comp == "s":
            return("you win!")
        elif comp == "w":
            return("you lose!")

print("you chose:  "+select)
print("comp chose: "+select2)
print(logic())
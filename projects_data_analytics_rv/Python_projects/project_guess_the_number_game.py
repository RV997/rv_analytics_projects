import random
comp = random.randint(1, 100)

user = None
numofguess = 0
while (user != comp):
    user = int(input("enter number: "))
    numofguess += 1
    if user == comp:
        print("congretulations! you guessed it right",comp)
            

    elif user > comp:
        print("you selected large number")

    elif user < comp:
        print("you selected small number")

print("number of guesses",numofguess)

with open("guess_hiscore.txt", "r") as f:
    hiscore = int(f.read())

if numofguess < hiscore:
    with open("guess_hiscore.txt", "w") as f:
        f.write(str(numofguess))
        
print("highscore was:",hiscore)


        
 


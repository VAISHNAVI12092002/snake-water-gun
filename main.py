import random
# snake water or gun


def game(comp, you):
    # if two values sre equal then tie
    if comp == you:
        return None
    # check for all possibilities when comp chose s
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    # check for all possibilities when comp chose w

    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    # check for all possibilities when comp chose g
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


print("comp turn :snake(s) water(w) or gun(g)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("player 2 turn :snake(s) water(w) or gun(g)?")
a = game(comp, you)

print(f"computer chose {comp} ")
print(f"you chose {you} ")
if a == None:
    print("The game is tie")
elif a == True:
    print(" you are a winner!")
elif a == False:
    print("you are a loser!")

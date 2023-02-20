import random

def game(compu,b):
    if compu==b:
        return None
    if compu== 's':
        if b=='w':
            return False
        elif b=='g':
            return True
    elif compu== 'w':
        if b=='g':
            return False
        elif b=='s':
            return True  
    elif compu== 'g':
        if b=='s':
            return False
        elif b=='w':
            return True   

print("Comp turn: Snake(s) water(w) or gun(g) ?")
randNo=random.randint(1,3)
# print(randNo)
if randNo== 1:
    compu='s'
elif randNo== 2:
    compu='w'
elif randNo== 3:
    compu='g'

b=input("Your's turn: Snake(s) water(w) or gun(g) ?")
a=game(compu,b)

print(f"Computer choose {compu}")
print(f"You choose {b}")

if a==None:
    print("The game is tie !")
elif a:
    print("You win !")
else:
    print("You loose !")
import random

borne_minimale = 0
borne_maximale = 10


def generator(small, big):
    return random.randint(small, big)

first = input("chose the smallest number")
last = input("chose the biggest number")
try:
    first = int(first)
    last = int(last)
except ValueError:
    print("i dont like that")
    exit()
chiffre_aleatoire = generator(first, last)


nb_essaie = 0
play_game = True

while play_game:
    print(f'I chose a number bettween {first} and {last}')
    answer = input("Entrer votre essaie: ")
    try:
        answer = int(answer)
    except ValueError:
        print("i dont like that")
        continue
    if answer > chiffre_aleatoire:
        print("number is too big try again: ")
    elif answer < chiffre_aleatoire:
        print("number is too small try again: ")
    else:
        print("YOU GOT IT")
        resume = input("do you want to continue? y/n")
        if resume == "y":
            first = input("chose the smallest number")
            last = input("chose the biggest number")
            try:
                first = int(first)
                last = int(last)
            except ValueError:
                print("i dont like that")
                exit()
            chiffre_aleatoire = generator(first, last)
        else:
            play_game = False
print("See you soon....;) ")

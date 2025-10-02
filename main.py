import random

borne_minimale = 0
borne_maximale = 10

def tcy(x,y):
    choice_dif=input("keep original difficulty? y/n")
    if choice_dif = "n":
        input()
    else :
        borne_minimale = 0
        borne_maximale = 10
chiffre_aleatoire = random.randint(borne_minimale, borne_maximale)

nb_essaie = 0
play_game = True

while play_game:
    print('Jai choisi un nombre entre 0 et 10')
    answer = int(input("Entrer votre essaie: "))
    if answer > chiffre_aleatoire:
        print("number is too big try again: ")
    elif answer < chiffre_aleatoire:
        print("number is too small try again: ")
    else:
        print("YOU GOT IT")
        resume = input("do you want to contunue? y/n")
        if resume == "y":
            chiffre_aleatoire = random.randint(borne_minimale, borne_maximale)
        else:
            play_game = False
print("See you soon....")
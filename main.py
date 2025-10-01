import random

game = True

borne_minimale = 0
borne_maximale = 10
chiffre_aleatoire = random.randint(borne_minimale, borne_maximale)

nb_essaie = 0
nombre_joueur = -1
play_game = True

while play_game:
    print('Jai choisi un nombre entre 0 et 10')
    input("Entrer votre nombre: ")

    if nombre_joueur == chiffre_aleatoire:
        play_game = False
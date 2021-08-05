"""Faire le jeu du Pierre Feuille Ciseaux"""
import random
#Variables Section
issues = ["Pierre", "Feuille", "Ciseaux"]

#Main Section
while True:
    jeu = input()

    result = random.choice(issues)
    print(result)

    if jeu == result:
        print("Egalite")
    if jeu == "Pierre" and result == "Ciseaux":
        print("Vous avez gagné")
    elif jeu == "Ciseaux" and result == "Pierre":
        print("Vous avez perdu")
    if jeu == "Feuille" and result == "Pierre":
        print("Vous avez gagné")
    elif jeu == "Pierre" and result == "Feuille":
        print("Vous avez perdu")
    if jeu == "Ciseaux" and result == "Feuille":
        print("Vous avez gagné")
    elif jeu == "Feuille" and result == "Ciseaux":
        print("Vous avez perdu")

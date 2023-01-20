import random
import matplotlib.pyplot as plt

graine = int(input("Veuillez rentrez une graine : "))  # Définition de la graine aléatoire
random.seed(graine)
print()

print("Les boules gagnantes sont :", end=" ")
# Tirage des 5 boules gagnantes
win = random.sample(range(1,45), 5)
print(win,"\n")



def tirage():
    nbr = int(input("Combien de tirage voulez-vous faire ? (0 pour arrêtez) "))
    print()
    if nbr >= 1:
        resultat = [] # Initialisation de la liste qui stockera les résultats de tirage
        for p in range(nbr):
            t = random.sample(range(1,45), 5)
            t.sort()  # tri des nombres tirés dans l'ordre croissant
            resultat.append(t) # Ajout des résultats de tirage à la liste
        return resultat

def choix_tri():
    print("Choisissez une méthode de tri:")
    print("1 - Tri par insertion")
    print("2 - Tri cocktail")
    print("3 - Tri fusion")
    choix = int(input())
    if choix == 1:
        tri_insertion(resultat)
    elif choix == 2:
        tri_cocktail(resultat)
    elif choix == 3:
        tri_fusion(resultat)
    else:
        print("Choix non valide.")
    return resultat

########################################################################################
####################### Fonctions de tri des séquences de tirages ######################
########################################################################################

def tri_insertion(resultat):
    for i in range(1, len(resultat)):
        cle = resultat[i]
        j = i-1
        while j >= 0 and resultat[j] > cle:
            resultat[j + 1] = resultat[j]
            j -= 1
        resultat[j + 1] = cle
    return resultat

def tri_cocktail(resultat):
    for i in range(len(resultat)):
        for j in range(i, len(resultat)):
            if resultat[i] > resultat[j]:
                resultat[i], resultat[j] = resultat[j], resultat[i]
    return resultat

def tri_fusion(resultat):
    if len(resultat) > 1:
        milieu = len(resultat) // 2
        gauche = resultat[:milieu]
        droite = resultat[milieu:]

        tri_fusion(gauche)
        tri_fusion(droite)

        i = j = k = 0

        while i < len(gauche) and j < len(droite):
            if gauche[i] < droite[j]:
                resultat[k] = gauche[i]
                i += 1
            else:
                resultat[k] = droite[j]
                j += 1
            k += 1

        while i < len(gauche):
            resultat[k] = gauche[i]
            i += 1
            k += 1

        while j < len(droite):
            resultat[k] = droite[j]
            j += 1
            k += 1

    return resultat

########################################################################################
########################################################################################
########################################################################################

resultat = tirage()
resultat = choix_tri()
print(resultat)


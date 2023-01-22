import random
import matplotlib.pyplot as plt
import pickle
import csv
from datetime import datetime

graine = int(input("Veuillez rentrez une graine : "))
random.seed(graine) # Définition de la graine aléatoire pour la génération des séquences
print()

print("Les boules gagnantes sont :", end=" ")
# Tirage des 5 boules gagnantes/ La séquence à chercher dans la série de tirage
win = random.sample(range(1, 45), 5)
print(win, "\n")
nbr = int(input("Combien de tirage voulez-vous faire ? (0 pour arrêtez) "))

def tirage(nbr):
    print()
    if nbr >= 1:
        resultat = []  # Initialisation de la liste qui stockera les résultats de tirage
        for p in range(nbr):
            t = random.sample(range(1, 45), 5)
            t.sort()  # tri des nombres tirés dans l'ordre croissant
            resultat.append(t)  # Ajout des résultats de tirage à la liste
        return resultat

"""#####################################################################################
####################### Fonctions de tri des séquences de tirages ######################
#####################################################################################"""

def tri_insertion(resultat):
    for i in range(1, len(resultat)):
        cle = resultat[i]
        j = i - 1
        while j >= 0 and resultat[j] > cle:
            resultat[j + 1] = resultat[j]
            j -= 1
        resultat[j + 1] = cle
    for i in range(len(resultat)):
        print(f"{i+1}.",resultat[i])
    return resultat


def tri_cocktail(resultat):
    for i in range(len(resultat)):
        for j in range(i, len(resultat)):
            if resultat[i] > resultat[j]:
                resultat[i], resultat[j] = resultat[j], resultat[i]
    for i in range(len(resultat)):
        print(f"{i+1}.", resultat[i])
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
        for i, seq in enumerate(resultat):
            print(f"{i+1}.", seq)
    else:
        print("Choix non valide.")
    return resultat

"""#####################################################################################
####################### Fonctions de recherche dichotomique ############################
#####################################################################################"""

def dichotomie_iterative(resultat, win):
    debut = 0
    fin = len(resultat) - 1
    while debut <= fin:
        milieu = (debut + fin) // 2
        if resultat[milieu] == win:
            return milieu
        elif resultat[milieu] < win:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return None

def dichotomie_recursive(resultat, win, debut, fin):
    if debut > fin:
        return None
    milieu = (debut + fin) // 2
    if resultat[milieu] == win:
        return milieu
    elif resultat[milieu] < win:
        return dichotomie_recursive(resultat, win, milieu + 1, fin)
    else:
        return dichotomie_recursive(resultat, win, debut, milieu - 1)

def choix_dichotomie(resultat, win):
    print("Choisissez une méthode de recherche dichotomique:")
    print("1 - Recherche dichotomique itérative")
    print("2 - Recherche dichotomique récursive")
    choix = int(input())
    if choix == 1:
        correspondance = dichotomie_iterative(resultat, win)
    elif choix == 2:
        correspondance = dichotomie_recursive(resultat, win, 0, len(resultat) - 1)
    else:
        print("Choix non valide.")
        return None
    if correspondance is not None:
        print(f"La séquence gagnante a été trouvée à la position {correspondance+1} dans la liste des résultats.")
    else:
        print("La séquence gagnante n'a pas été trouvée dans la liste des résultats.")
    return correspondance

"""#######################################################################################
####################### Fonctions de sauvegarde/chargement de fichier ####################
#######################################################################################"""

def export_txt(resultat, graine, nbr):
    # Création du nom de fichier
    horodatage = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nom_fichier = f"{graine}_{nbr}_tirages_{horodatage}.txt"
    # Ecriture des résultats dans le fichier
    with open(nom_fichier, "w") as f:
        for i, seq in enumerate(resultat):
            f.write(f"{i + 1}. {seq}\n")
    print(f"Les résultats ont été exportés dans le fichier {nom_fichier}.")

def export_csv(resultat, graine, nbr):
    # Création du nom de fichier
    horodatage = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    nom_fichier = f"{graine}_{nbr}_tirages_{horodatage}.csv"
    # Ecriture des résultats dans le fichier
    with open(nom_fichier, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Numéro de séquence", "Séquence"])
        for i, sequence in enumerate(resultat):
            writer.writerow([i+1, sequence])
    print(f"Les résultats ont été exportés dans le fichier {nom_fichier}.")

def export_bin(resultat, graine, nbr):
    horodatage = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    nom_fichier = f"{graine}_{nbr}_tirages_{horodatage}.bin"
    with open(nom_fichier, "wb") as f:
        pickle.dump(resultat, f)
    print(f"Les résultats ont été exportés dans le fichier {nom_fichier}")

"""#######################################################################################
####################### Fonction d'affichage de la distribution aléatoire ################
#######################################################################################"""

def afficher_diagramme(resultat):
    frequence = [0] * 45  # Initialisation de la liste des fréquences à 0
    for tirage in resultat:
        for n in tirage:
            frequence[n - 1] += 1  # Incrémentation de la fréquence pour chaque nombre tiré

    # Séparation des fréquences en plages de 5 nombres consécutifs
    groupe = []
    for i in range(0, 45, 5):
        groupe.append(sum(frequence[i:i + 5]))

    plt.bar(range(1, 46, 5), groupe)
    plt.xlabel("Plages de nombres (1-5, 6-10, etc.)")
    plt.ylabel("Fréquence d'apparition")
    plt.show()

"""#######################################################################################
####################### Execution du programme ###########################################
#######################################################################################"""

resultat = tirage(nbr)
#resultat.append(win) #Permet de tester la fonction de recherche dichotomique indépendamment des séquences générées par la fonction de tirage
resultat = choix_tri()
print()
correspondance = choix_dichotomie(resultat, win)
export_txt(resultat, graine, nbr)
export_csv(resultat, graine, nbr)
export_bin(resultat, graine, nbr)
afficher_diagramme(resultat)

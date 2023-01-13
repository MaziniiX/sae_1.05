import random
import matplotlib.pyplot as plt

graine = int(input("Veuillez rentrez une graine : "))  # Définition de la graine aléatoire
random.seed(graine)
print()


def tirage():  # Fonction de tirages succesifs
    nbr = int(input("Combien de tirage voulez-vous faire ? (0 pour arrêtez) "))
    print()
    if nbr >= 1:
        for p in range(nbr):
            t = random.sample(range(1,45), 5)
            print(t)
            print()
        tirage()


def tri_cocktail(tc):
    debut = 0
    fin = len(tc) - 1
    while debut <= fin:
        echange = False
        for i in range(debut, fin):
            if tc[i] > tc[i + 1]:
                tc[i], tc[i + 1] = tc[i + 1], tc[i]
                echange = True
        fin = fin - 1
        if echange:
            for i in range(fin, debut, -1):
                if tc[i - 1] > tc[i]:
                    tc[i], tc[i - 1] = tc[i - 1], tc[i]
                    echange = True
        debut = debut + 1


def fusion(L1, L2):
    n1 = len(L1)
    n2 = len(L2)
    L12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2:
        if L1[i1] < L2[i2]:
            L12[i] = L1[i1]
            i1 += 1
        else:
            L12[i] = L2[i2]
            i2 += 1
        i += 1
    while i1 < n1:
        L12[i] = L1[i1]
        i1 += 1
        i += 1
    while i2 < n2:
        L12[i] = L2[i2]
        i2 += 1
        i += 1
    return L12


print("Les boules gagnantes sont :", end=" ")
# Tirage des 5 boules gagnantes
win = random.sample(range(1,45), 5)
print(win)

print("\n")
tirage()
#liste = [5, 2, 4, 8, 1, 3]
#tri_cocktail(liste)
#print(liste)

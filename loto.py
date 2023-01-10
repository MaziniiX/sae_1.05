import random

graine=int(input("Veuillez rentrez une graine : ")) #Définition de la graine aléatoire
random.seed(graine)
print()

def tirage(): #Fonction de tirages succesifs
    nbr=int(input("Combien de tirage voulez-vous faire ? (0 pour arrêtez) "))
    print()
    if nbr >= 1:
        for t in range(nbr):
            for n in range(5):
                a = round(random.uniform(1, 45))
                print(a, end=" ")
            print("\n")
        tirage()

print("Les boules gagnantes sont :",end=" ")
for i in range(5): #Tirage des 5 boules gagnantes
    a=round(random.uniform(1, 45))
    print(a,end=" ")

print("\n")
tirage()
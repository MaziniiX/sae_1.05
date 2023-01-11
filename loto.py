import numpy

graine=int(input("Veuillez rentrez une graine : ")) #Définition de la graine aléatoire
numpy.random.seed(graine)
print()

def tirage(): #Fonction de tirages succesifs
    nbr=int(input("Combien de tirage voulez-vous faire ? (0 pour arrêtez) "))
    print()
    if nbr >= 1:
        for p in range(nbr):
            t = numpy.random.randint(1, 45, 5)
            print(t)
            print()
        tirage()

def tri_cocktail(lst):
    start = 0
    end = len(lst) - 1
    while start <= end:
        swapped = False
        for i in range(start, end):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swapped = True
        end = end-1
        if swapped:
            for i in range(end, start, -1):
                if lst[i-1] > lst[i]:
                    lst[i], lst[i-1] = lst[i-1], lst[i]
                    swapped = True
        start = start+1
print("Les boules gagnantes sont :",end=" ")
#Tirage des 5 boules gagnantes
win=numpy.random.randint(1, 45, 5)
print(win)

print("\n")
#tirage()
liste = [5, 2, 4, 8, 1, 3]
tri_cocktail(liste)
print(liste)

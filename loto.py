import random
seed=int(input("Veuillez rentrez une graine : "))
tirage=0
random.seed(seed)
for i in range(5):
    a=round(random.uniform(1, 45))
    print(a,end=" ")
tirage=int(input("Combien de tirage voulez-vous faire ? (0 pour arrêtez)"))
for n in range(tirage):
    a = round(random.uniform(1, 45))
    print(a, end=" ")
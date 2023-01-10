nbr=int(input("Entrez un nombre : "))
fac=1
for n in range(nbr):
    fac=fac*nbr
    nbr=nbr-1
print("fac =",fac)
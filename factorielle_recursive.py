def rec(n):
    if n==1:
        return 1
    else:
        return n*rec(n-1)
n=int(input("entrez un nombre n: "))
print(rec(n))
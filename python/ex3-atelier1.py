s=0
def somme(n):
    if n==0 :
        return 0
    else :
        return n+somme(n-1)
a=int(input("entre un nombre : "))         #demander à l'utilisateur un nombre 
print("la somme de 1 à",a,"est ",somme(a)) #afficher la somme de 1 jusqu'à ce nombre
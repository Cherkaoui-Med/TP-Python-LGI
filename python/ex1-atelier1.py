def somme(n):
    f=1
    s=0
    for i in range(1,n+1):
        f=f*i
        s=s+(f/i)
    return s
a=int(input("entrer un nombre : "))                         #demander à l'utilisateur un nombre
print("la somme de 1!/1 jusqu'à ",a,"!/",a," est",somme(a))  #retourner la somme de 1!/1 jusqu'à la factorielle de ce nombre diviser par lui même 
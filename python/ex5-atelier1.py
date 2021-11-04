def nbrdechiffres(n):
    if n==0 : return 0        #condition d'arrête
    return 1+nbrdechiffres(n//10)  #chaque fois on divise le nombre sur 10 ; chaque division siginfie une chiffre de plus dans le nombre
a=int(input("enter un nombre : "))  #demander à l'utilisateur un nombre
print("le nombre de chiffres dans votre nombre est :",nbrdechiffres(a))  #retourner le nombre de chiffres dans ce nobre
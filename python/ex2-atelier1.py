def conv(n):
    if n>1:
        conv(n//2)
    print(n%2,end='')
a=int(input("entrer un nombre décimal : "))                       #demander à l'utilisateur un nombre décimal
print("la conversion de ",a," en nombre binaire est :",end='')    #retourner la conversion de ce nombre décimal en nombre binaire
conv(a)
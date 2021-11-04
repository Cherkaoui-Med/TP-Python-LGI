def frq(c,ch):
    fq=0
    for i in ch:
        if c==i:
            fq+=1
    return fq

ch=input("donnez votre chaîne de caractères : ")          #demender à l'utilisateur d'entrer une chaîne de caractères et gardes sa valeur dans "ch"
c=input("entrez le caractère que vous voulez calculer son fréquence:")
print("la fréquence de ce caractère dans votre chaîne de caractères est :",frq(c,ch))   #afficher la fréquence du caractère dans la chaîne de caractères
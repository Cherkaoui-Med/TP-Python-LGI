l=[59,40,33,14,12,59,33,40,59,33,59]
dict={}
c=0
for i in range(len(l)) :      #parcourir les éléments de la liste
    for j in range(len(l)):   #aussi parcourir les éléments de la liste
        if l[j]==l[i] :       #voir si il y a des éléments qui se répètent
            c=c+1             #incrementer c par 1 pour chaque fois on trouve que l'élèment se répète
            dict[l[i]]=c      #ajouter au dictionnaire l'élément de la liste comme clé et le nombre de fois qu'il se répète comme valeur
    c=0                       #donner à c la valeur 0 pour qu'il commence compter le nombre de répitition de l'élément suivant
print(dict)

# tri par insertion
def tri_insertion(t): 
    for i in range(1, len(t)):          #parcourir tout le tableau
        for j in range(i-1,-1,-1):      #parcourir à partit de l'élément qui précède le ième élément et on retourne en arrière
            while i>0 and  t[i]<t[j]:   #condition d'arrêt + la condition pour permuter 
                t[i],t[j]=t[j],t[i]     # permutation des éléments
                i-=1                    # condition nécéssaire pour parcourir tout les éléments précédantes du jème élément 
    return t
t=[55,42,36,1,22,0,8]
print(tri_insertion(t))
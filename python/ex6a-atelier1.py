# tri à bull 
def tri_bull(t):
    for i in range(len(t)): # parcourir tout le tableau
        for j in range(len(t)-i-1):  # on commence par parcourir tous les éléments du tableau puis à chaque fois 
                                     #on soustrait le dernier élément du parcours précédante puisqu'il est déjà trié
            if t[j]>t[j+1]:           #condition pour trier les éléments
                t[j],t[j+1]=t[j+1],t[j] #trier l'élément avec l'élément qui le suit 
    print(t)
t=[1,2,5,77,6,11]
tri_bull(t)


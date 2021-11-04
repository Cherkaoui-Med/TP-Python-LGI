l=[25,66,14,35,84,96,3,48,7,5,6,9]
a=len(l)-1
l1=[]
l2=[]
l3=[]
for i in range(a//3,-1,-1) :      #on divise la longueur du liste sur 3 , et on parcourir cette division mais on inverse
  l1.append(l[i])                 #ajouter les éléments de la première division à la liste l1 (en ordre inversé)
  l2.append(l[i+len(l)//3])       #ajouter les éléments de la deuxième division à la liste l2 (en ordre inversé)
  l3.append(l[i+2*(len(l)//3)])   #ajouter les éléments de la troisième division à la liste l3 (en ordre inversé) 

print(l1,l2,l3)        #afficher les trois listes
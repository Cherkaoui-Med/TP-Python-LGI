#deux listes données l1 et l2 :
l1=[5,33,14,65,87,77]
l2=[22,1,3,8,45,102]
l3=[]
for i in range(1,len(l1),2):   #parcourir les éléments d'index impaires du liste l1
    l3.append(l1[i])            #ajouter ces éléments à la liste l3
for j in range(0,len(l2),2):    #parcourir les éléments d'index paires du liste l1
    l3.append(l2[j])            #ajouter ces éléments à la liste l3
print(l3)
   
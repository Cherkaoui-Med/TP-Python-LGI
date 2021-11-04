l=[47, 64, 69, 37, 76, 83, 97]
dict={'Yassine':47,'Imane':69,'Mohammed':76,'Abir':97}

for element in l:   #parcourir les éléments de la liste
        if element not in dict.values(): #voir si l'élément de la liste n'existe pas dans les valeurs du dictionnaire
            l.remove(element)            #il l'efface s'il n'existe pas
print(l)
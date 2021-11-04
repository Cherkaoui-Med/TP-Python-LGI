def position(e):
    for i in range(len(m)):         #parcourir les lignes de la matrice
        for j in range(len(m[0])):  # parcouric les colonnes de la matrice 
            if e==m[i][j] :         # vérification du condition
                print(i+1,j+1)

m=[[1,2,3],[4,5,6],[6,8,9]]   #une matrice donnée
e=5                           #exemple pour e=5
position(e)                   #appel du fonction
        

 #tri par selection
def tri_selection(t):
   for i in range(len(t)):
       min = i
       for j in range(i+1, len(t)): # on cherche le minumum
           if t[min] > t[j]:
               min = j  
       a = t[i]       # on sauvegarde la valeur existant où on veut déplacer le minumum
       t[i] = t[min]  # on déplace le minumum pour qu'il soit trié
       t[min] = a     # on déplace la valeur avec qui on a trié le minumum dans sa position
   return t
t=[25,3,14,99,67]
print(tri_selection(t))
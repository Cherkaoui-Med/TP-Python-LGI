a=0
b=1
c=0
def fub(a,b):
    if a==0 and b==1 : print("0 1",end=' ')  #cas particulier pour les deux premiers termes
    c=a+b
    print(c,end=' ')   # aficher la somme de deux termes précédentes
    a=b                # a prend la valeur du b
    b=c                # b prend la valeur du somme de deux termes précédentes
    fub(a,b)           # en utilsant la récursivité on affiche continuement la somme de deux termes pércédentes
fub(a,b)               # appel du fonction
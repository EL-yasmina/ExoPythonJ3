#Définir une fonction qui effectue une rotation à gauche des éléments d'une liste. Par exemple, la liste [1,2,3,4] après une rotation à gauche devient [2,3,4,1].
def rotation_fun(list):
    if len(list) <=1: #vérifier si la liste est inferiere ou egale à 1
        return list
    first_element = list[0] # sauvgarde le premier element de la liste dans une variable 
    for i in range(len(list)-1): #parcourir chaque element de la liste en commençant par la 2 element indice1   
        list[i]=list[i+1]
    list[-1]=first_element
    return list
liste=[1,2,3,4]
rotation_fun(liste)
print(liste)
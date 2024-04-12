# Définir une fonction qui élimine les doublons d'une liste sans utiliser la fonction set().
def elimine_dupl(liste1):

    element_unique = []    #liste vide pour stocker les element unique
    for element in liste1:    #boucle pour parcourir chaque élement de la liste1    
        if element not in element_unique: #vrification de l'element dans la liste unique si n'est pas trouver donc on l'ajoute dans la liste unique  
            element_unique.append(element)
    return element_unique

liste_originale = [1, 2, 3, 1,1,1, 2, 4, 5, 5, 6]
liste_unique = elimine_dupl(liste_originale)
print(liste_originale) 
print(liste_unique)
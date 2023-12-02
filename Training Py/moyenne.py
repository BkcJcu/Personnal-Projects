liste = [2, 9, 3, 7, 5, 1, 8, 4, 6, 0]

def moyenne(liste):
    somme = 0
    for nombre in liste:
        somme += nombre
    result = somme / len(liste)
    return result

print("Voici la moyenne de la liste : ", moyenne(liste))


# Je peut simplifier encore plus en mettant : "return somme / len(liste)" et par conséquent éliminer la variable result.

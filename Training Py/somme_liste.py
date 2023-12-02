liste = [2, 9, 3, 7, 5, 1, 8, 4, 6, 0]



def somme_liste(liste):
    a = 0
    for i in range(len(liste)):
        a += liste[i]
    return a

resultat = somme_liste(liste)

print(resultat)



#---------------------------------------#

def somme_liste_alternative(liste):
    somme = 0
    for nombre in liste:
        somme += nombre
    return somme
liste = [2, 9, 3, 7, 5, 1, 8, 4, 6, 0]

def nombres_pairs(liste):
    nombres_pairs = []
    for nombre in liste:
        if nombre % 2 == 0:
            nombres_pairs.append(nombre)
    return nombres_pairs


liste = nombres_pairs(liste)
print("Voici les nombres pairs de la liste :", liste)

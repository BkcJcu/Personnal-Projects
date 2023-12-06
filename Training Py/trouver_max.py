# Manière très peu opti, je ré-utilise le tri-bulle que j'ai fait auparavant


liste = [2, 9, 3, 7, 5, 1, 8, 4, 6, 0]

def tri_bulle(liste):
    for i in range(len(liste)):
        for j in range(0, len(liste) - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]

tri_bulle(liste)
print("L'élément le plus grand de la liste est : ",liste[len(liste) - 1])


# Vrai fonction max

def trouver_max(liste):
    max_element = liste[0]
    for element in liste:
        if element >= max_element:
            max_element = element
    return max_element 

print("L'élément le plus grand de la liste est : ",trouver_max(liste))
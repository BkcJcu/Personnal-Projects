listea = [2, 9, 3, 7, 5, 1, 8, 4, 6, 0]
listeb = [12, 19, 13, 17, 15, 11, 18, 14, 16, 10, 20, 23, 28, 27, 26, 24, 25, 21, 29]

def fusionner_listes_triee(liste1, liste2):
    for i in range(len(liste2)):
        liste1.append(liste2[i])
    for i in range(len(liste1)):
        for j in range(0, len(liste1) - i - 1):
            if liste1[j] > liste1[j+1]:
                liste1[j], liste1[j+1] = liste1[j+1], liste1[j]
    return liste1

print("Voici la fusion des deux listes, triées dans l'ordre croissant :", fusionner_listes_triee(listea, listeb))
print("Ratio")

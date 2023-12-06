liste = [2, 9, 3, 7, 5, 1, 8, 4, 6, 0]

def tri_bulle(liste):
    for i in range(len(liste)):
        for j in range(0, len(liste) - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]




tri_bulle(liste)
print(liste)
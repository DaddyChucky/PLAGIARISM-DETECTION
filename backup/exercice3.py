__version__ =   "TP6 Question #3"
__author__  =   "Michael Yammine (2149029), Jérémie Riendeau (2093152)"
__date__    =   "5 décembre 2021"

import matplotlib.pyplot as plt
import numpy as np
import csv


def nuage_de_points():
    """
    Fonction qui trace 3 graphiques différents sur une seule figure.
    Les graphiques demandés sont fournis dans l'énoncé du TP.
    """
    tailles_matrice=[]
    durees_sans_numpy=[]
    durees_avec_numpy=[]
    with open("durees_receuillies.csv", 'r') as fichier_entrees:
        lecture = csv.reader(fichier_entrees, delimiter=',')
        compteur = None
        for row in lecture:
            if compteur != None:
                tailles_matrice.append(float(row[0]))
                durees_sans_numpy.append(float(row[1]))
                durees_avec_numpy.append(float(row[2]))
            compteur = 1

    tailles_matrice=np.array(tailles_matrice)
    durees_sans_numpy=np.array(durees_sans_numpy)
    durees_avec_numpy=np.array(durees_avec_numpy)

    polynome_1 = np.poly1d(np.polyfit(x=tailles_matrice, y=durees_sans_numpy, deg=3))
    polynome_2 = np.poly1d(np.polyfit(x=tailles_matrice, y=durees_avec_numpy, deg=2))

    X = np.linspace(10, 500, 200)

    plt.subplot(3,1,1)
    plt.title("Temps de calcul en fonction de la taille des matrices carrées multipliées")
    plt.plot(X, polynome_1(X), color="red", marker='o',markersize=3)
    plt.ylabel('Durée sans numpy')

    plt.subplot(3,1,2)
    plt.plot(X, polynome_2(X), color="blue", marker='o',markersize=3)
    plt.ylabel('Durée avec numpy')

    plt.subplot(3,1,3)
    plt.plot(X, polynome_1(X), color="red", marker='o',markersize=3, label='sans numpy')
    plt.plot(X, polynome_2(X), color="blue", marker='o',markersize=3, label='avec numpy')
    plt.legend(loc='upper left')
    plt.xlabel('Taille des matrices multipliées')
    plt.ylabel('Comparatif des durées')
    plt.show()



if __name__ == "__main__":
    nuage_de_points()
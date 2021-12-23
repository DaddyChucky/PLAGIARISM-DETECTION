__version__ =   "TP6 Question #1"
__author__  =   "Michael Yammine (2149029), Jérémie Riendeau (2093152)"
__date__    =   "29 novembre 2021"

import random  # Pour la génération de nombres aléatoires
import time  # Pour le chronométrage
import csv

import numpy as np  # Pour les opérations matricielles


def multiplier_matrice(A, B):
    """Fonction qui permet de multiplier deux matrices

    Arguments :
        A (List[List[int]]) : La matrice de gauche
        B (List[List[int]]) : La matrice de droite

    Valeur de retour :
        List[List[int]] : La matrice résultat
    """
    # m, n = resp. nombre de lignes et colonnes de la matrice résultat
    m, n = len(A), len(B[0])
    res = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            for k in range(len(A[0])):
                res[i][j] += A[i][k] * B[k][j]

    return res

def matrice_aleatoire(m, n):
    """Fonction qui génère une matrice de taille m * n remplie de nombre aléatoire entre 0 et 9

    Arguments :
        m (int) : Le nombre de lignes
        n (int) : Le nombre de colonnes

    Valeur de retour :
        List[List[int]] : La matrice aléatoire de taille m x n
    """
    # TODO
    """
    Référence pour la suite du programme :
    http://www.learningaboutelectronics.com/Articles/How-to-create-an-array-of-random-integers-in-Python-with-numpy.php
    Les auteurs Michael Yammine et Jérémie Riendeau s'en sont inspiré pour savoir comment faire un random array de int avec NumPy
    """
    return np.random.randint(0, 10, size=(m,n)).tolist()


def duree_multiplication_sans_numpy(A, B):
    """Fonction qui chronomètre le temps pour multiplier en utilisant la fonction multiplication_matrice

    Arguments :
        A (List[List[int]]) : La matrice de gauche
        B (List[List[int]]) : La matrice de droite

    Valeur de retour :
        float : Le temps requis pour multiplier les deux matrices sans numpy
    """
    # TODO
    """
    Référence pour la suite du programme :
    https://realpython.com/python-time-module/#:~:text=%20A%20Beginner%E2%80%99s%20Guide%20to%20the%20Python%20time,you%20have%20a%20firm%20grasp%20on...%20More%20 
    Les auteurs Michael Yammine et Jérémie Riendeau s'en sont inspiré pour savoir comment chronométrer
    """
    debut = time.perf_counter()
    multiplier_matrice(A, B)
    fin = time.perf_counter()
    return fin - debut
    
    


def duree_multiplication_avec_numpy(A, B):
    """Fonction qui chronomètre le temps pour multiplier en utilisant numpy

    Arguments :
        A (np.ndarray) : La matrice de gauche
        B (np.ndarray) : La matrice de droite

    Valeur de retour :
        float : Le temps requis pour multiplier les deux matrices avec numpy
    """
    # TODO
    A, B = np.array(A), np.array(B)
    debut = time.perf_counter()
    np.matmul(A, B)
    fin = time.perf_counter()
    return fin - debut


def generer_donnees():
    """
    Fonction qui créé une fichier CSV contenant le temps requis pour multiplier deux matrices.
    Le fichier doit avoir les colonnes taille, duree_sans_numpy, duree_avec_numpy et duree_totale.
    La définition de chaque colonne est donnée dans le fichier pdf de l'énoncé du TP.
    """
    # TODO : Retirer cette ligne et écrire votre code
    #print(matrice_aleatoire(4,4))
    #print(duree_multiplication_sans_numpy(matrice_aleatoire(3, 3),matrice_aleatoire(3, 3)))
    #print(duree_multiplication_avec_numpy(matrice_aleatoire(3, 3),matrice_aleatoire(3, 3)))
    entete = ['taille','duree_sans_numpy','duree_avec_numpy','duree_totale']
    with open("durees_receuillies.csv", 'w', encoding='utf-8', newline = '') as fichier_sortie:
        ecriture = csv.writer(fichier_sortie, delimiter=',')
        ecriture.writerow(entete)
        for taille in range(5, 306, 30):
            debut = time.perf_counter()
            ecriture.writerow([taille, 
            duree_multiplication_sans_numpy(matrice_aleatoire(taille, taille), matrice_aleatoire(taille, taille)), 
            duree_multiplication_avec_numpy(matrice_aleatoire(taille, taille), matrice_aleatoire(taille, taille)),
            (time.perf_counter()-debut)])


if __name__ == "__main__":
    generer_donnees()

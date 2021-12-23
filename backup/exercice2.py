__version__ =   "TP6 Question #2"
__author__  =   "Nom élève 1 (matricule 1), nom élève 2 (matricule 2)"
__date__    =   "Date de dernière modification"

import matplotlib.pyplot as plt  # Pour le tracer le diagramme circulaire
import csv

def diagramme_circulaire():
    """
    Fonction qui trace un diagramme circulaire de la distribution du temps d'exécution.
    Les graphiques demandés sont fournis dans l'énoncé du TP.
    """

    with open('durees_receuillies.csv') as csv_file: 
        csv_reader= csv.reader(csv_file, delimiter = ',')
        donne_sans_numpy = 0.0
        donne_avec_numpy = 0.0
        total = 0         
        for row in csv_reader: 
            if not row[0] == "temps_sans_numpy" and not row[1] == "duree_avec_numpy" and not row[2] == "duree_totale": 
                try:
                    donne_sans_numpy += float(row[0])
                    donne_avec_numpy += float(row[1])
                    total += float(row[2])
                except ValueError:
                    continue

        autres = total - (donne_sans_numpy + donne_avec_numpy)
        taille_autre = (autres / total) * 100
        taille_donnee_sans_numpy = (donne_sans_numpy / total) *100 
        taille_donnee_avec_numpy = (donne_avec_numpy / total) *100

    labels = 'Temps sans numphy', 'Temps avec numphy', 'Autre', 
    taille = [taille_donnee_sans_numpy, taille_donnee_avec_numpy  , taille_autre]
    couleurs = ['Lightgreen', 'RoyalBlue', 'DarkGrey']
    plt.title("Distribution du temps d'exécution")
    plt.pie(taille, labels=labels, colors=couleurs, 
        autopct='%1.1f%%', shadow=False, startangle=0)
    plt.axis('equal')
    plt.savefig('Pietemps01.png')
    plt.show()

if __name__ == "__main__":
    diagramme_circulaire()

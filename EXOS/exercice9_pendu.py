__version__ = "TP3 Question #9"
__author__  = "Etienne Gendron (2089899), Zouré Oussenî (2003084)"
__date__    = "24/10/2021"


from pendu_ascii_art import pendu

# Pour cet exercice nous allons programmer un jeu de bonhomme pendu.
# Pour cet exercice vous aurez à compléter plusieurs fonction qui vous permettront
# ultimement de jouer au jeu.
# Ne complèter que les fonctions commençant par TODO.
# Ces fonctions sont:
#     imprime_mot()
#     imprime_lettres_sortie()
#     devine_lettre()
#     vérifie_victoire()
mot = ""

lettres_trouvées = ""

lettres_rejetées = ""

nombre_essais_restant = 6


def imprime_mot():

    # TODO
    print("""---Lettre trouvées---""")

    mot_suite=""
   
    for lettre in mot:
        if lettre in lettres_trouvées:
            mot_suite+=lettre+" "
        else:
            mot_suite+="_"
    print(mot_suite)
    # Fonction qui imprime le mot à trouver en remplaçant les lettres
    # encore inconnues par le symbole "_".

    # Si le mot à trouver est : "chenille"
    # Et les lettre devinée sont : "cel"
    # Affiche : c _ e _ _ l l e

    # Si le mot à trouver est : "Renard"
    # Et les lettre devinée sont : "ean"
    # Affiche : _ e n a _ _
    pass


def imprime_lettres_sortie():
    # TODO
    print("---Lettre rejetées---")
    lettres_rejetées_majuscule=""
    for L in lettres_rejetées:
        lettres_rejetées_majuscule+=L.upper()+" "
    print(lettres_rejetées_majuscule)
        


    # Imprime les lettre ayant été devinée, mais ne se trouvant pas dans le mot en les séparant
    # par des espaces.

    # Si les lettres "acf" ont été rejetées comme ne faisant pas partie du mot,
    # imprime : A C F

    # Si les lettres "qpmz" ont été rejetées comme ne faisant pas partie du mot,
    # imprime : A C F

    pass


def devine_lettre():
    # TODO
    # Ici on utilise des variable globales, c'est à dire qu'elle sont créé à l'extêrieur de la fonction
    # et peuvent être utilisée à l'intérieur comme à l'extêrieur.
    # Généralement on les évites, car elles peuvent être déclicate à manipuler et causer et bug difficilement
    # décelable. Dans notre cas notre programme est relativement simple et vous n'avez pas encore appris
    # de solutions alternatives, nous nous en contenterons donc.
    global nombre_essais_restant
    global lettres_trouvées
    global lettres_rejetées
    global mot

    lettre_devinee=input("Devinez une lettre:")
    
    while lettre_devinee.isalpha()== False:
        print("Lettre invalide")
        lettre_devinee=input("Devinez une lettre a nouveau:")

    while lettre_devinee in lettres_rejetées or lettre_devinee in lettres_trouvées:
        print("Tu as deja essaye de deviner cette lettre")
        lettre_devinee=input("Choisissez une autre lettre:")


    if lettre_devinee in mot:
        print("Bien trouve!")
        lettres_trouvées+=lettre_devinee
                
    else:
        print("Non, la lettre n'est pas dans le mot choisie.")
        lettres_rejetées+=lettre_devinee
        nombre_essais_restant-=1

     
        
       


    # Demande à l'utilisateur de deviner une lettre et continu de lui
    # demander tant qu'il ne fournie pas une lettre valide.
    #   Si la lettre n'est pas valide afficher : Lettre invalide
    #   Si l'utilisateur a déjà essayé de deviner cette lettre afficher: "Tu as déjà essayé de deviner cette lettre"
    # Si le lettre est valide et qu'elle se trouve dans le mot à deviner l'ajouter à lettres_trouvées
    # et afficher : Bien trouvé!
    # Si le lettre est valide et qu'elle ne se trouve pas dans le mot à deviner l'ajouter à lettres_rejetées
    # et afficher : Non, la lettre n'est pas dans le mot choisie.
    pass


def verifie_victoire():
    # TODO
    check = all(item in lettres_trouvées for item in mot)
    if check:
        return True
    else:
        return False
    # Vérifie si toute les lettre du mot à deviner on été trouvé dans la variable lettre_trouvées.
    pass


def imprime_pendu():
    # Imprime le dessin du pendu en charactère ASCII tel que défini dans pendu_ascii_art.py
    print(pendu.get(nombre_essais_restant))


def imprime_état_du_jeu():
    imprime_pendu()
    imprime_lettres_sortie()
    imprime_mot()


def jeu():

    playing = True
    # Tant que la partie est en cours
    while playing:
        # Demander au joueur de choisir un mot
        global mot
        mot = "$"
        # Lui demander de choisir un mot tant que celui-ci n'est pas valide.
        while not mot.isalpha():
            mot = input("Choisissez un mot :")
            if not mot.isalpha():
                print("Mot invalide")
        # Définir les paramètre de la partie à leur valeur initiale.
        global nombre_essais_restant
        global lettres_rejetées
        global lettres_trouvées
        lettres_trouvées = ""
        lettres_rejetées = ""
        nombre_essais_restant = 6
        # Imprimer l'état initial du jeu
        imprime_état_du_jeu()
        while nombre_essais_restant > 0 and not verifie_victoire():
            # Tant qu'il reste des essais au joueur, lui demander de deviner une lettre
            devine_lettre()
            # et imprimer l'état actuel du jeu
            imprime_état_du_jeu()
        if nombre_essais_restant > 0:
            # Si le jour parvient à deviner le mot, le féliciter!
            print("Bravo! Vous avez gagnez!")
        if nombre_essais_restant == 0:
            # Si le joueur n'est pas parvenu à deviner le mot lui dire qu'il a perdu
            print("Vous avez perdu")
        if (
            # Proposer au joueur de rejouer
            input("Rejouer? (q -> quitter, n'importe quoi d'autre pour continuer) :")
            == "q"
        ):
            playing = False


if __name__ == "__main__":
    jeu()

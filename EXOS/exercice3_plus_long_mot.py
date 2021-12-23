__version__ = "TP3 Question #3"
__author__  = "Etienne Gendron (2089899), Zouré Oussenî (2003084)"
__date__    = "24/10/2021"




def plus_long_mot(phrase):
    # Code qui prend une phrase et imprime son plus long mot.
    # Les mots sont séparés par des espaces. "J'aime" sera considéré comme un seul mot de 6 lettres.
    # À noter que nous supposons qu'aucune phrase ne possède que des mots de même longueur.
    Plus_Long_Mot = ""
    taille_max = 0
    i= 0
    var = ""
    separateurs = ".,; !?"
    phrase = phrase + " "

    while i < len(phrase):
        if not(phrase[i] in separateurs):
            var = var + phrase[i]
        else: 
            if var != "" and len(var) > taille_max:
                    Plus_Long_Mot = var 
                    taille_max = len(var)
            var = ""
    
        i += 1

    print(Plus_Long_Mot)
    pass


if __name__ == "__main__":
    plus_long_mot("J'adore manger des carottes.")
    # carottes



__version__ = "TP3 Question #6"
__author__  = "Etienne Gendron (2089899), Zouré Oussenî (2003084)"
__date__    = "24/10/2021"

"""
def Position_Points(phrase):
    # fonction qui permet de scinder le texte en plusieurs phrases distinctes 
    mot = "."
    id = phrase.find(mot)
    return id
"""
def Sission_Texte(phrase):
    ls = []
    mot = "."

    while phrase != "":
        # id = Position_Points(phrase)
        id = phrase.find(mot) # position du "." dans la phrase 
        ls.append(phrase[0:id+1].strip())

        """
        try:
            phrase = phrase[id+1:len(phrase)]
        except:
            phrase = ""
        """
        if id+1 > len(phrase):
            phrase = ""
        else:
            phrase = phrase[id+1:len(phrase)]
    return ls

def majuscule_en_debut_de_phrase(texte):
    # Code qui s'assure que le premier mot de chaque phrase commence par une majuscule.
    # Le première lettre de chaque phrase et forcément une majuscule.
    # Les phrases se terminent par un point
    ls = Sission_Texte(texte)
    i = 0
    while i < len(ls):
        print(ls[i].capitalize(), end = ' ')
        i += 1 
    pass


if __name__ == "__main__":
    majuscule_en_debut_de_phrase(
        "je suis heureux. nous sommes vendredi. c'est bientôt la fin de semaine."
    )
    # Je suis heureux. Nous sommes vendredi. C'est bientôt la fin de semaine.

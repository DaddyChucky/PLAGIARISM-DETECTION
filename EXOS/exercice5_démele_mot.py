__version__ = "TP3 Question #5"
__author__  = "Etienne Gendron (2089899), Zouré Oussenî (2003084)"
__date__    = "24/10/2021"


def demele(mots):
    # Code qui démèle un mot ou une phrase tel qu'un caractère sur deux fait partie
    # d'une phrase tandis que les autres en font partie d'une autre.
    # Par exemple:
    # TCihgireen
    # ↓ ↓ ↓ ↓ ↓
    # T i g r e
    #  ↓ ↓ ↓ ↓ ↓
    #  C h i e n
    phrase = ["",""] 
    i = 0 
    while i < len(mots): 
        if i % 2 == 0: 
            phrase[0] = phrase[0] + mots[i]
        else:
            phrase[1] = phrase[1] + mots[i]
        i += 1
    print(phrase[0])
    print(phrase[1])
    pass


if __name__ == "__main__":

    demele("JJ'ea dsouries  muann gjeory euunxe  lpuoriorne..")
    # Je suis un joyeux luron.
    # J'adore manger une poire.

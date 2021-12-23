__version__ =   "TP3 Question #1"
__author__  =   "Etienne Gendron (2089899), Zouré Oussenî (2003084)"
__date__    =   "24/10/2021"


def verifie_palindrome(mot):
    # Code qui vérifie si un mot fourni en paramètre est ou non un palindrome.
    # Ne considérer que des mots (et non des phrases qui sont des palindromes).
    # Les majuscules ne doivent pas être différenciées de leur équivalent en minuscule. Exemple: "Ava" est un palindrome, tout comme "sALlut0tUaS".
    # Imprime dans la console : "Il ne s'agit pas d'un palindrome" si ce n'est pas un palindrome.
    # Imprime dans la console : "Il s'agit d'un palindrome" si c'est un palindrome.
    pass
    if mot.lower()==mot[::-1].lower():
        print("Il s'agit d'un palindrome")
    else:
        print("Il ne s'agit pas d'un palindrome")
if __name__ == "__main__":
    verifie_palindrome("kayak")
    # Il s'agit d'un palindrome
    verifie_palindrome("cheval")
    # Il ne s'agit pas d'un palindrome
    verifie_palindrome("Eve")
    # Il s'agit d'un palindrome
    verifie_palindrome("Anna")
    # Il s'agit d'un palindrome

__version__ = "TP3 Question #8"
__author__  = "Etienne Gendron (2089899), Zouré Oussenî (2003084)"
__date__    = "24/10/2021"


def encrypte(texte, clé):
    # Code une message texte en décalant lettre par la clé
    # en suivant un chiffrement de type César aussi connu sous le
    # nom de chiffrement par décalage.

    # Exemple 1, si la lettre est A, avec une clé de 3,
    # Elle devient un D, car D est 3 lettre plus loin dans l'alphabet

    # Exemple 2, si la lettre est Z, avec une clé de 2,
    # Elle devient un B, car B est 3 lettre plus loin dans l'alphabet
    # si en comptant on revient à la lettre A après Z.
    alphabet_upperLower = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    texte_encrypte = ""

    i = 0
    while i < len(texte):
        if texte[i].islower() == False: # lettre en majuscule
            alphabet = alphabet_upperLower[1]
        else:
            alphabet = alphabet_upperLower[0] # minuscule 

        if texte[i] in alphabet: 
            # encryptage 
            pos = alphabet.find(texte[i]) # position de la lettre dans l'alphabet
            posEncrypt = (pos + clé) % 26 
            texte_encrypte = texte_encrypte + alphabet[posEncrypt]

        else: 
            texte_encrypte = texte_encrypte + texte[i]

        i += 1

    return texte_encrypte
pass

def décrypte(texte, clé):
    # Décode une message texte en décalant lettre par la clé
    # en suivant un chiffrement de type César aussi connu sous le
    # nom de chiffrement par décalage.

    # Exemple 1, si la lettre est D, avec une clé de 3,
    # Elle devient un A, car D est 3 lettre plus loin que A dans l'alphabet

    # Exemple 2, si la lettre est B, avec une clé de 2,
    # Elle devient un Z, car B est 3 lettre plus loin que Z dans l'alphabet
    # si en comptant on revient à la lettre A après Z.
    
    alphabet_upperLower = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    texte_decrypte = ""
    clé = -clé
    i = 0
    while i < len(texte):
        if texte[i].islower() == False: # lettre en majuscule
            alphabet = alphabet_upperLower[1]
        else:
            alphabet = alphabet_upperLower[0] # minuscule 

        if texte[i] in alphabet: 
            # encryptage 
            pos = alphabet.find(texte[i]) # position de la lettre dans l'alphabet
            posDecrypt = (pos + clé) % 26 
            texte_decrypte = texte_decrypte + alphabet[posDecrypt]

        else: 
            texte_decrypte = texte_decrypte + texte[i]

        i += 1
    return texte_decrypte
    pass


if __name__ == "__main__":
    message_encrypté = encrypte("Allo poly", 3)
    print(message_encrypté)
    # Door srob

    massage_décrypté = décrypte(message_encrypté, 3)
    print(massage_décrypté)
    #c Allo poly

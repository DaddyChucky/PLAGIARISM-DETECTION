__version__ = "TP3 Question #2"
__author__  = "Etienne Gendron (2089899), Zouré Oussenî (2003084)"
__date__    = "24/10/2021"


def est_une_voyelle(ch):
    ch = ch.lower()
    if ch in "aeiouy":
        return True
    else:
        return False


def conjugue_verbe(mot):
    # Code qui prend un verbe à l'infinitif se terminant en er et le conjugue au présent.
    # Sous le format suivant pour le verbe regarder:
    """
    Verbe : regarder

    Je regarde
    Tu regardes
    Il/Elle regarde
    Nous regardons
    Vous regardez
    Ils regardent
    """
    # Sous le format suivant pour le verbe aimer:
    """
    Verbe : aimer

    J'aime
    Tu aimes
    Il/Elle aime
    Nous aimons
    Vous aimez
    Ils aiment
    """
    # Faire attention à l'utilisation du "J'" et non du "Je" lorsque le verbe comment par une voyelle
    # Vous pouvez utiliser la fonction est_une_voyelle() pour vous aider. Par exemple: est_une_voyelle("a") retournerais vrai (True).

    radical= mot[:-2]
    Presence_Voyelle = est_une_voyelle(mot[0])

    if Presence_Voyelle == True : 
        # le verbe commence par une voyelle
        print("J'" + radical + "e")
    else:
        print("je",radical+"e")
    
    print("Tu",radical+"es")
    print("Il/Elle",radical+"e")
    print("Nous",radical+"ons")
    print("Vous",radical+"ez")
    print("Ils/Elles",radical+"ent", end='\n\n')

    """pronoms = ["tu ", "il/elle ", "nous ", "vous ", "ils/elles "]
    terminaisons = ["e", "es", "e", "ons", "ez", "ent"]

    if Presence_Voyelle == True : 
        # le verbe commence par une voyelle
        pronoms.insert(0,"j'")
    else: 
        pronoms.insert(0,"je ")
    
    i = 0 
    while i < len(terminaisons):
        print(pronoms[i] + radical + terminaisons[i])
        i += 1
    print("", end = "\n\n")"""
    pass


if __name__ == "__main__":
    conjugue_verbe("soulever")
    conjugue_verbe("regarder")
    conjugue_verbe("aimer")

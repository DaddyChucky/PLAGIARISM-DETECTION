def check_input(msg):
    # Fonction qui pose une question "msg" à l'utilisateur.
    # Celui-ci peut répondre y pour oui et n pour non
    # Retourne True lorsque le réponse est oui et False lorsque la réponse est non
    ans = ""
    while ans != "y" and ans != "n":
        ans = input(msg)
        ans = ans.strip().lower()
    if ans == "y":
        return True
    elif ans == "n":
        return False
    else:
        print("Une erreur innatendue s'est produite")


def quel_génie_es_tu():
    # Ce numéro est un peu particulier, car il va falloir vous montrer créatif.
    # Vous devez coder un jeu.
    # Dans ce jeu vous poserez des questions à l'utilisateur, celles-ci se réponde par oui (y) ou non (n).
    # À partir des réponses de ces question et d'un arbre de vérité vous devez deviner quel est le génie de
    # l'utilisateur et l'imprimer.
    # Vous êtes libres de poser les questions que vous voulez et
    # de créer l'arbre à la structure que vous voulez
    #
    # Une sortie doit exister pour chaque génie offert à polytechnique.
    # C'est à dire...
    # Génie biomédical
    # Génie chimique
    # Génie civil
    # Génie géologique
    # Génie des mines
    # Génie électrique
    # Génie logiciel
    # Génie informatique
    # Génie mécanique
    # Génie physique
    pass


if __name__ == "__main__":
    quel_génie_es_tu()

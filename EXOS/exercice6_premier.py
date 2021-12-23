import math


def verifie_premier(num):
    # Vérifie si un nombre est premier.
    # L'imprime si oui
    if num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):
            if (num % i) == 0:
                return
        print(num)
        return True
    return False


def imprime_premiers_entre_1_et_n(n):
    # Prenant un entier n, afficher tous les entiers premier entre 1 et n.
    # Vous pouvez utiliser la fonction verifie_premier pour vous aider.

    pass


def imprime_n_premiers(n):
    # prenant un entier n, afficher les n premiers entiers.
    # Vous pouvez utiliser la fonction verifie_premier pour vous aider.

    pass


if __name__ == "__main__":
    imprime_premiers_entre_1_et_n(10)
    """
    2
    3
    5
    7
    """
    imprime_n_premiers(10)
    """
    2
    3
    5
    7
    11
    13
    17
    19
    23
    29
    """

# _________                             .__       .__     __    _________ .__                 .__                  ________           .____            _____              __         .__               
# \_   ___ \  ____ ______ ___.__._______|__| ____ |  |___/  |_  \_   ___ \|  |__ _____ _______|  |   ____   ______ \______ \   ____   |    |   _____ _/ ____\____   _____/  |______  |__| ____   ____  
# /    \  \/ /  _ \\____ <   |  |\_  __ \  |/ ___\|  |  \   __\ /    \  \/|  |  \\__  \\_  __ \  | _/ __ \ /  ___/  |    |  \_/ __ \  |    |   \__  \\   __\/  _ \ /    \   __\__  \ |  |/    \_/ __ \ 
# \     \___(  <_> )  |_> >___  | |  | \/  / /_/  >   Y  \  |   \     \___|   Y  \/ __ \|  | \/  |_\  ___/ \___ \   |    `   \  ___/  |    |___ / __ \|  | (  <_> )   |  \  |  / __ \|  |   |  \  ___/ 
#  \______  /\____/|   __// ____| |__|  |__\___  /|___|  /__|    \______  /___|  (____  /__|  |____/\___  >____  > /_______  /\___  > |_______ (____  /__|  \____/|___|  /__| (____  /__|___|  /\___  >
#         \/       |__|   \/              /_____/      \/               \/     \/     \/                \/     \/          \/     \/          \/    \/                 \/          \/        \/     \/ 
# Le chat, le renard et le poisson | 14 sept. 2021 | Charles De Lafontaine

class Jeu:
    def __init__(self, x: int, y: int):
        self.H = x
        self.V = y
        self.partieTermine = False
        self.gagnant = ""

class Chat(Jeu):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)

class Renard(Jeu):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)

class Poisson(Jeu):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.mange = False

class Maison(Jeu):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)

if __name__ == "__main__":
    chat = Chat(3, 6)
    renard = Renard(9, 7)
    poisson = Poisson(6, 8)
    maison = Maison(1, 8)
    jeu = Jeu(None, None)

    # Procédure chat
    def procedure_chat():
        if chat.V == poisson.V and chat.H == poisson.H:
            poisson.mange = True

        if chat.V == maison.V and chat.H == maison.H:
            jeu.partieTermine = True
            jeu.gagnant = "Chat"

        if poisson.mange == False:
            if chat.V < poisson.V:
                chat.V += 1
            elif chat.V > poisson.V:
                chat.V -= 1
            elif chat.H < poisson.H:
                chat.H += 1
            elif chat.H > poisson.H:
                chat.H -= 1
        
        else:
            if chat.V < maison.V:
                chat.V += 1
            elif chat.V > maison.V:
                chat.V -= 1
            elif chat.H < maison.H:
                chat.H += 1
            elif chat.H > maison.H:
                chat.H -= 1
    
    # Procédure renard
    def procedure_renard():
        if renard.V == chat.V and renard.H == chat.H:
            jeu.partieTermine = True
            jeu.gagnant = "Renard"

        if renard.H < chat.H:
            renard.H += 1
        elif renard.H > chat.H:
            renard.H -= 1
        elif renard.V < chat.V:
            renard.V += 1
        elif renard.V > chat.V:
            renard.V -= 1

    n_iteration = 0
    while not jeu.partieTermine:
        print("-> Début procédure #", n_iteration)

        procedure_chat()
        procedure_renard()

        print("Coordonnées chat (x, y): (", chat.H, ",", chat.V, ")")
        print("Coordonnées renard (x, y): (", renard.H, ",", renard.V, ")")
        print("Coordonnées maison (x, y): (", maison.H, ",", maison.V, ")")

        print("-> Fin procédure #", n_iteration)

        n_iteration += 1
        
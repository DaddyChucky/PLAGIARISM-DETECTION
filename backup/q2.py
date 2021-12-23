# _________                             .__       .__     __    _________ .__                 .__                  ________           .____            _____              __         .__               
# \_   ___ \  ____ ______ ___.__._______|__| ____ |  |___/  |_  \_   ___ \|  |__ _____ _______|  |   ____   ______ \______ \   ____   |    |   _____ _/ ____\____   _____/  |______  |__| ____   ____  
# /    \  \/ /  _ \\____ <   |  |\_  __ \  |/ ___\|  |  \   __\ /    \  \/|  |  \\__  \\_  __ \  | _/ __ \ /  ___/  |    |  \_/ __ \  |    |   \__  \\   __\/  _ \ /    \   __\__  \ |  |/    \_/ __ \ 
# \     \___(  <_> )  |_> >___  | |  | \/  / /_/  >   Y  \  |   \     \___|   Y  \/ __ \|  | \/  |_\  ___/ \___ \   |    `   \  ___/  |    |___ / __ \|  | (  <_> )   |  \  |  / __ \|  |   |  \  ___/ 
#  \______  /\____/|   __// ____| |__|  |__\___  /|___|  /__|    \______  /___|  (____  /__|  |____/\___  >____  > /_______  /\___  > |_______ (____  /__|  \____/|___|  /__| (____  /__|___|  /\___  >
#         \/       |__|   \/              /_____/      \/               \/     \/     \/                \/     \/          \/     \/          \/    \/                 \/          \/        \/     \/ 
# Fibonacci | 14 sept. 2021 | Charles De Lafontaine

# Version "longue"
def fibonacci():
    i = avant_dernier_nombre = 0
    dernier_nombre = 1

    while i < 10:
        print(dernier_nombre)
        variable_temporaire = avant_dernier_nombre
        avant_dernier_nombre = dernier_nombre
        dernier_nombre += variable_temporaire
        i += 1

# Décommentez pour rouler la première version
# if __name__ == "__main__":
#     fibonacci()

# Équivalent en version récursive
def fibonnaci(n) -> None:
    if n <= 1:
        return n
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)

# Décommentez pour rouler la seconde version
# if __name__ == "__main__":
#     for i in range(10):
#         print(fibonnaci(i))

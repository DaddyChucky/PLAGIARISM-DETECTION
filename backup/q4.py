# _________                             .__       .__     __    _________ .__                 .__                  ________           .____            _____              __         .__               
# \_   ___ \  ____ ______ ___.__._______|__| ____ |  |___/  |_  \_   ___ \|  |__ _____ _______|  |   ____   ______ \______ \   ____   |    |   _____ _/ ____\____   _____/  |______  |__| ____   ____  
# /    \  \/ /  _ \\____ <   |  |\_  __ \  |/ ___\|  |  \   __\ /    \  \/|  |  \\__  \\_  __ \  | _/ __ \ /  ___/  |    |  \_/ __ \  |    |   \__  \\   __\/  _ \ /    \   __\__  \ |  |/    \_/ __ \ 
# \     \___(  <_> )  |_> >___  | |  | \/  / /_/  >   Y  \  |   \     \___|   Y  \/ __ \|  | \/  |_\  ___/ \___ \   |    `   \  ___/  |    |___ / __ \|  | (  <_> )   |  \  |  / __ \|  |   |  \  ___/ 
#  \______  /\____/|   __// ____| |__|  |__\___  /|___|  /__|    \______  /___|  (____  /__|  |____/\___  >____  > /_______  /\___  > |_______ (____  /__|  \____/|___|  /__| (____  /__|___|  /\___  >
#         \/       |__|   \/              /_____/      \/               \/     \/     \/                \/     \/          \/     \/          \/    \/                 \/          \/        \/     \/ 
# Multiplication de deux nombres | 14 sept. 2021 | Charles De Lafontaine

def multiplication_nb(premier_nombre, deuxieme_nombre):
    return float(premier_nombre) * float(deuxieme_nombre)

if __name__ == "__main__":
    premier_nombre = input("Choisissez votre premier nombre: ")
    deuxieme_nombre = input("Choisissez votre deuxieme nombre: ")

    print("Résultat de la multiplication:", multiplication_nb(premier_nombre, deuxieme_nombre))

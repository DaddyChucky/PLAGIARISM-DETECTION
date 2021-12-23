# _________                             .__       .__     __    _________ .__                 .__                  ________           .____            _____              __         .__               
# \_   ___ \  ____ ______ ___.__._______|__| ____ |  |___/  |_  \_   ___ \|  |__ _____ _______|  |   ____   ______ \______ \   ____   |    |   _____ _/ ____\____   _____/  |______  |__| ____   ____  
# /    \  \/ /  _ \\____ <   |  |\_  __ \  |/ ___\|  |  \   __\ /    \  \/|  |  \\__  \\_  __ \  | _/ __ \ /  ___/  |    |  \_/ __ \  |    |   \__  \\   __\/  _ \ /    \   __\__  \ |  |/    \_/ __ \ 
# \     \___(  <_> )  |_> >___  | |  | \/  / /_/  >   Y  \  |   \     \___|   Y  \/ __ \|  | \/  |_\  ___/ \___ \   |    `   \  ___/  |    |___ / __ \|  | (  <_> )   |  \  |  / __ \|  |   |  \  ___/ 
#  \______  /\____/|   __// ____| |__|  |__\___  /|___|  /__|    \______  /___|  (____  /__|  |____/\___  >____  > /_______  /\___  > |_______ (____  /__|  \____/|___|  /__| (____  /__|___|  /\___  >
#         \/       |__|   \/              /_____/      \/               \/     \/     \/                \/     \/          \/     \/          \/    \/                 \/          \/        \/     \/ 
# Calcul moyenne | 14 sept. 2021 | Charles De Lafontaine

def calcul_moyenne_etudiants(notes):
    return round(sum(notes) / len(notes), 2)

if __name__ == "__main__":
    notes = [60.1, 90.7, 100, 50, 23, 10.5, 60.8, 70.1, 90.1, 99.9]
    print("La moyenne de votre class est:", calcul_moyenne_etudiants(notes), "%")
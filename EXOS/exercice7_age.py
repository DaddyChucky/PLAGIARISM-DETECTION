__version__ = "TP3 Question #7"
__author__  = "Etienne Gendron (2089899), nom élève 2 (matricule 2)"
__date__    = "24/10/2021"


def gateau_factorie(nb_étage, hauteur_étage):
    # Programme qui imprime un gateau d'anniversaire pour l'usager.
    # Le programme commence par demander l'age de l'usager et continu de lui demander tant que l'age
    # n'est pas un entier valide.
    # Le programme imprime ensuite un gateau sur lequel il y aura autant de bougies que l'age de l'usager,
    # ayant nb_étage(fournie en paramètre) d'une hauteur de
    # hauteur_étage (fournie en paramètre) chacun.
    # Le progremme affiche ensuite "Joyeux Neme anniversaire" ou N est l'age de l'utilisateur.

    # Voici un exemple de gateau pour un usager de 4 ans, ayant un gateau de 2 étages d'une hauteur de 2.
    """
    Quel age as-tu? 4
        i i i i
      @%@%@%@%@%@%
      {          }
      {          }
    @%@%@%@%@%@%@%@%
    {              }
    {              }
    @%@%@%@%@%@%@%@%

    Joyeux 4eme anniversaire
    """
    # Voici un exemple de gateau pour un usager de 3 ans, ayant un gateau de 3 étages d'une hauteur de 1.
    """
    Quel age as-tu? 3
          i i i
        @%@%@%@%@%
        {        }
      @%@%@%@%@%@%@%
      {            }
    @%@%@%@%@%@%@%@%@%
    {                }
    @%@%@%@%@%@%@%@%@%

    Joyeux 3eme anniversaire
    """
    # Voici un exemple de gateau pour un usager de 1 ans, ayant un gateau de 1 étage d'une hauteur de 1.
    """
    Quel age as-tu? 1
      i
    @%@%@%
    {    }
    @%@%@%

    Joyeux 1eme anniversaire
    """
    def entier(prompt):
      while True:
        try:
          value = int(input(prompt))
        except  ValueError:
          print("Veuillez entrer un entier positif")
          continue
        else:
         break
      return value

    nb_bougie=entier("Quel age avez-vous?:")
    nb_bougie=int(nb_bougie)
  
    space="  "
    print(space*nb_étage,nb_bougie*"i ")
    i=1
    if i<=nb_étage:
      print(space*(nb_étage-i),(nb_bougie+(2*i))*"@%")
      n=1
      if n<=hauteur_étage:
        print(space*(nb_étage-i), "{",space*(nb_bougie+(2*(i-1))),"}")
      else:
        return
        n=n+1
    else:
      return
    i=i+1
    print(space*(nb_étage-i),(nb_bougie+(2*(i-1)))*"@%")
    print("Joyeux",nb_bougie,"eme anniversaire")
      
    
if __name__ == "__main__":
    gateau_factorie(1, 1)

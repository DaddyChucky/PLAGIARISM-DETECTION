__version__ = "TP3 Question #4"
__author__  = "Nom élève 1 (matricule 1), nom élève 2 (matricule 2)"
__date__    = "Date de dernière modification"


def remplace_tout(phrase, mot_a_remplacer, mot_remplaçant):
    # Code qui prend une phrase, un mot à remplacer et un mot remplaçant et réimprime la phrase
    # en ayant remplacé le mot à remplacer par le mot remplaçant
    print(phrase.replace(mot_a_remplacer, mot_remplaçant))
    pass


if __name__ == "__main__":
    remplace_tout(
        """\tMa chère Héloise, tu es le soleil de mes journées,
        aucune autre que toi Héloise ne sait m'éclairer. 
        Oh Héloise tu es la seule pour moi, 
        Quand tu es proche de moi Héloise, je me sens comme une roi.
        Héloise, apaise mon coeur bohème,
        Oh Héloise je t'en prie dit moi que tu m'aimes.""",
        "Héloise",
        "Sophie",
    )
    ### SORTIE DU PROGRAMME
    ###    Ma chère Sophie, tu es le soleil de mes journées,
    ###    aucune autre que toi Sophie ne sait m'éclairer.
    ###    Oh Sophie tu es la seule pour moi,
    ###    Quand tu es proche de moi Sophie, je me sens comme une roi.
    ###    Sophie, apaise mon coeur bohème,
    ###    Oh Sophie je t'en prie dit moi que tu m'aimes.

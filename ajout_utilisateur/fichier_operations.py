def read_file(chemin):
    # fonction read_file
    """Renvoie un dictionnaire écrit dans un document texte en respectant la syntaxe python
    chemin (str) : chemin vers le fichier texte
    return (dict) : dictionnaire tel qu'écrit dans le fichier texte"""
    # on ouvre le fichier
    with open(chemin,"r") as fichier:
        # on recupère son contenu sous forme de chaine de caractères
        contenu = fichier.read()
    # on la transforme en dictionnaire python pour la renvoyer
    return eval(contenu)
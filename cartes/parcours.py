def bfs(graph, start):
    """Parcours en largeur d'un graphe
    graph (dict) : lsite d'adjacences d'un graphe
    start (int/str) : nom du sommet de départ
    return (list) : ordre dans lequel on a parcouru les sommets"""
    visited = set() # Ensemble pour suivre les sommets déjà visités
    resultat = []   # Liste pour stocker l'ordre des sommets visités
    file = []       # File pour gérer les sommets à traiter

    # Ajout du nœud de départ à la file et marquage comme visité
    file.append(start)
    visited.add(start)

    # Boucle principale pour la traversée en largeur
    while file:
        # Traitement du sommet en cours
        sommet_courant = file.pop(0)
        resultat.append(sommet_courant)

        # Parcours des voisins du sommet en cours
        for voisin, _ in graph[sommet_courant]:
            # Vérification que le voisin n'a pas déjà été visité
            if voisin not in visited:
                # Ajout du voisin à l'ensemble des visités et à la file
                visited.add(voisin)
                file.append(voisin)

    # Retour de la liste ordonnée des nœuds visités
    return resultat

def dfs(graph, start):
    """Parcours en profondeur d'un graphe
    graph (dict) : liste d'adjacences du graphe
    start (int/str) : nom du sommet de départ
    return (list) : ordre dans lequel on a parcouru le graphe"""

    visited = set() # Initialisation de l'ensemble des sommets visités
    resultat = []   # Initialisation de la liste pour stocker l'ordre des sommets visités

    # Appel initial de la fonction auxiliaire pour commencer la visite en profondeur
    dfs_visiter(start, visited, resultat, graph)

    return resultat

def dfs_visiter(sommet_courant, visited, resultat, graph):
    """fonction récursive de parcours en profondeur d'un graphe
    sommet_courant (int/str) : nom du sommet ou l'on se trouve
    visited (set) : ensemble des sommet déjà"""
    # Ajout du sommet courant à l'ensemble des sommets visités et à la liste résultat
    visited.add(sommet_courant)
    resultat.append(sommet_courant)

    # Parcours des voisins du sommet courant
    for voisin, _ in graph[sommet_courant]:
        # Vérification si le voisin n'a pas été visité
        if voisin not in visited:
            # Appel récursif pour visiter le voisin
            dfs_visiter(voisin, visited, resultat, graph)
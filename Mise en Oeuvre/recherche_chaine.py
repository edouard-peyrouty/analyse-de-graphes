def chaine(graph, depart, arrivee):
    """Recherche l'existance d'une chaine entre deux noeuds d'un graphe et en renvoie une le cas échéant
    graph (dict) : liste d'adjacence du graphe
    depart, arrivee (int/str) : étiquette des extrémités du chemin
    return (list) : suite de noeud correspondant au chemin"""
    visited = set() # Initialisation de l'ensemble des sommets visités
    chemin = []     # Initialisation de la liste pour stocker l'ordre des sommets visités
    
    # Si la fonction auxiliaire trouve un chemin
    if trouver_chemin(depart, arrivee, visited, chemin, graph):
        # on le renvoie
        return chemin
    else:
        # s'il n'y pas de chemin on renvoie la valeur None
        return None

def trouver_chemin(courant, arrivee, visited, chemin, graph):
    """recherche récursive de l'existance d'un chemin entre deux noeuds d'un graphe
    courant,arrivee (int/float) : étiquette des extremités du chemin
    visited (set) : ensemble des neouds déjà visités
    chemin (list) : ordre dans lequel on a visité les noeuds depuis le début des appels récursifs
    graph (dict) : liste d'adjacence du graphe
    return (bool) : vrai si un chemin existe faux sinon"""
    # Ajout du sommet courant à l'ensemble des sommets visités et à la liste résultat
    visited.add(courant)
    chemin.append(courant)
    
    # cas d'arrêt lorsque on recherche un chemin d'un noeud à lui même
    if courant == arrivee:
        return True
    
    # on parcours les voisins du noeud de départ qui n'ont pas déjà été visités
    for voisin,_ in graph[courant]:
        if voisin not in visited:
            # Si l'on trouve un chemin entre au moins un des voisins et le noeud d'arrivée, on renvoie True 
            if trouver_chemin(voisin, arrivee, visited, chemin, graph):
                return True
    
    # si aucun chemin n'existe on renvoie false et on vide la liste chemin
    chemin.pop()
    return False

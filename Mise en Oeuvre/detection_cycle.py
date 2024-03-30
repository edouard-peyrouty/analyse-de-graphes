def detection_cycle(graph):
    """recherche l'existance d'un cycle dans un graphe 
    graph (dict) : liste d'djacence du graphe
    return (list/None) : liste des sommets formant le cycle et None si aucun cycle
    """
    visited = set() # ensemble des sommets visités
    cycle = []      # liste des sommets formant un cycle

    # on appelle la fonction auxilaire de recherche de cycle récursif pour chaque sommet du graphe
    for noeud in graph.keys():
        # on ne passe qu'une seule fois par chaque sommet
        if not noeud in visited:
            if recherche_cycle(noeud,None,visited,cycle,graph):
                # on renvoie le premier cycle que l'on trouve
                return cycle

    # valeur par défaut si aucun cycle trouvé     
    return None

def recherche_cycle(courant,parent,visited,cycle,graph):
    """fonction récursive de recherche de cycle
    courant (int/str) : noeud a partir duquel on cherhce un cycle
    parent (int/str) : noeud à partir duquel on cherchait un cycle à l'étape précédente, voisin du noeud courant
    visited (set) : ensemble des noeuds à aprtir desquels on a chercher des cycles
    graph (dict) : liste d'adjacence du graphe
    return (list/None) : sommet formant un cycle ou None si aucun cycle
    """
    # on met à jour l'ensemble des noeuds visités et les sommets formant un cycle
    visited.add(courant)   
    cycle.append(courant)

    # on visite chaque voisin du noeud courant
    for voisin,_ in graph[courant]:
        # on recherche un cycle à partir du voisin si cela n'a pas déjà été fait
        if not voisin in visited:
            if recherche_cycle(voisin,courant,visited,cycle,graph):
                # une fois un cycle trouvé, on le fait remonter le long des appels récursifs
                return cycle
        # on revoie le cycle si l'on rencontre un sommet que l'on a déjà visité autre que le sommet parent
        elif voisin != parent:
            cycle.append(voisin)
            for i in range(cycle.index(voisin)):
                cycle.pop(i)    
            return cycle

    # si aucun cycle trouvé, on renvoie None   
    cycle.remove(courant)
    return None     
from math import inf
    
def construire_chemin(debut,fin,predecesseurs):
    """
    Construit un chemin entre deux noeuds à partir d'un dictionnaire de prédécesseurs
    debut,fin (str) : extrémités du chemin
    return (list) : chemin
    
    """
    chemin = []         # noeud dans l'ordre
    noeud_courant = fin # on part du noeud d'arrivé

    # remonte jusqu'au noeud de départ
    while noeud_courant != debut:
        # on ajoute le noeud courant au chemin
        chemin.append(noeud_courant)
        # on remonte d'un neoud
        noeud_courant = predecesseurs[noeud_courant]
    
    # on ajoute le noeud de départ au chemin
    chemin.append(noeud_courant)
    # par construction, le chemin est à l'envers on l'inverse avant de le renvoyer
    return chemin[::-1]

def dijkstra(graph,debut,fin):
    """Trouve le chemin le plus court entre deux noeuds dans un graphe
    graph (dict) : liste d'adjacence 
    debut (str) : nom du noeud de départ
    fin (str) : nom du noeud d'arrivée
    return (list) : liste des noeuds du chemin 
    """
    # a chaque noeud on associe la distance la plus courte que l'on connait pour l'atteindre
    distances = {noeud : inf for noeud in graph.keys()}
    # donc 0 pour le noeud de départ
    distances[debut] = 0
    # a chaque noeud on associe son prédécesseur dans le chemin le plus court que l'on connait pour l'atteindre
    predecesseurs = {noeud : None for noeud in graph.keys()}
    # file des noeuds a traiter 
    file_prioritaire = [(debut,0)]

    # tant qu'il y a des noeuds a traiter
    while len(file_prioritaire) != 0:
        # on travaille sur le noeud de la liste des noeuds a traiter ayant le plus petit poids/distance et on le retire de la liste des noeuds à traiter
        if len(file_prioritaire) == 1 :
            noeud_courant, distance_courante = file_prioritaire.pop(0)
        else :
            noeud_courant, distance_courante = min(file_prioritaire, key=lambda x: x[1])
            file_prioritaire.remove(min(file_prioritaire, key=lambda x: x[1])) 

        # on s'intéresse à chaque voisin du noeud courant 
        for voisin, poids in graph[noeud_courant]:
            # on calcule la distance du chemin vers le noeud voisin courant passant par le noeud courant   
            nouvelle_distance = distance_courante + poids
            # si cette derniere est inférieure à la plus courte distance vers ce noeud connue on met à jour :
            if nouvelle_distance < distances[voisin]:
                # - la distance la plus courte que l'on connait pour atteindre le noeud voisin courant 
                distances[voisin] = nouvelle_distance
                # - le predecesseur du noeud voisin courant dans le chemin le plus court que l'on connait pour l'atteindre
                predecesseurs[voisin] = noeud_courant
                # enfin on ajoute le noeud voisin courant dans la liste des noeuds à traiter
                file_prioritaire.append((voisin,nouvelle_distance))
                
    return construire_chemin(debut,fin,predecesseurs)
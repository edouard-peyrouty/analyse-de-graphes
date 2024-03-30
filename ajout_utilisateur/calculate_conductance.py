def calculate_conductance(graph, communities):
    """calcule la conductance d'un découpage en communauté d'un graphe
    grah (dict) : liste d'adjacence du graphe
    communities (dict) : dictionnaire des communautés sous la forme {noeud:communauté}
    return (float) : conductance globale du graphe
    """
    total_conductance = 0
    total_communities = len(communities.values())

    # Parcours de toutes les communautés
    for community in communities.values():
        # Calcul de la conductance de la communauté
        community_conductance = calculate_conductance_communitie(graph, communities, community)
        # Ajout de la conductance de la communauté à la conductance totale
        total_conductance += community_conductance

    # Calcul de la conductance globale moyenne
    global_conductance = total_conductance / total_communities
    return - global_conductance

def calculate_conductance_communitie(graph, communities, community):
    """calcule la conductance d'une communauté d'un graphe
    grah (dict) : liste d'adjacence du graphe
    communities (dict) : dictionnaire des communautés sous la forme {noeud:communauté}
    communitie (str/int) : etiquette de la communauté étudiée
    return (float) : conductance d'une communauté d'un graphe
    """
    # Calcul du nombre total de liens sortants de la communauté
    total_community_edges = sum(weight for node in graph for _, weight in graph[node]
                                if communities[node] == community)
    # Initialisation de la conductance à une valeur élevée
    conductance = float('inf')
    
    # Parcours de tous les noeuds de la communauté
    for node in graph:
        # Si le noeud appartient à la communauté en cours d'évaluation
        if communities[node] == community:
            # Calcul du nombre de liens entre le noeud et les noeuds extérieurs à la communauté
            external_edges = sum(weight for neighbor, weight in graph[node] if communities[neighbor] != community)
            # Calcul de la conductance pour ce noeud
            node_conductance = external_edges / max(total_community_edges, 1)  # Éviter la division par zéro
            # Mise à jour de la conductance minimale
            conductance = min(conductance, node_conductance)
    
    return conductance
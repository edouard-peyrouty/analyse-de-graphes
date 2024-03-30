from itertools import combinations

def calculate_modularity(graph, communities):
    """calcule la modularité d'un découpage en communauté d'un graphe
    grah (dict) : liste d'adjacence du graphe
    communities (dict) : dictionnaire des communautés sous la forme {noeud:communauté}
    return (float) : modularité globale du graphe
    """
    # modularité initial à 0
    modularity = 0
    # calcule la somme des poids de toutes les arêtes du graphe
    total_edges = sum(sum(weight for _, weight in neighbors) for neighbors in graph.values()) // 2

    # pour chaque paire de communautés possible
    for pair_communities in combinations(set(communities.values()), 2):
        # on calcule la proportion de liens entre les communautés par rapports aux liens au sein d'un de ces communautés
        fraction_intra_community = calculate_fraction_intra_community(graph, pair_communities, communities)
        # on incrémente la modularité totale de la différence entre la somme précédente et la proportion de liens total de la 1er commuanté de la paire par rapport à la somme de tous les liens du graphe
        modularity += fraction_intra_community - ((calculate_weighted_edges_in_community(graph, pair_communities[0], communities) / total_edges) ** 2)

    # on renvoie la modularité
    return modularity

def calculate_fraction_intra_community(graph, pair_communities, communities):
    """ Calcule et renvoie la proportion de liens entre deux communautés par rapport au nombre de liens au sein d'une seule de ces communautés
    graph (dict) : liste d'adjacence du graph
    pair_commuities (tuple) : paire de deux communautés
    communities (dict) : dictionnaire des communauté de la forme {noeud:communauté}
    return (float) : ration liens entre communautés / lien au sein de la 1er communauté
    """
    # calcule la somme pondérée des liens entre les deux communautés
    edges_intra_community = calculate_weighted_edges_between_communities(graph, pair_communities, communities)
    # calcule la somme pondérée des liens au sein de la première communauté de la paire
    edges_total = calculate_weighted_edges_within_community(graph, pair_communities[0], communities)
    # renvoie le ratio entre les deux sommes
    return edges_intra_community / edges_total if edges_total != 0 else 0

def calculate_weighted_edges_between_communities(graph, pair_communities, communities):
    """renvoie la somme des poids des liens partant d'une communauté donnée et arrivant dans une autre communautés elle auusi précisée
    graph (dict) : lisyte d'adjacence du graphe
    pair_commuities (tuple) : paire de deux communautés
    communities (dict) : dictionnaire des communauté de la forme {noeud:communauté}
    return (int) : somme des poids au sein d'une communauté
    """
    return sum(weight for node in graph for neighbor, weight in graph[node]
               if communities[node] == pair_communities[0] and communities[neighbor] == pair_communities[1])

def calculate_weighted_edges_within_community(graph, community, communities):
    """renvoie la somme des poids des liens au seins d'une communauté donnée
    graph (dict) : lisyte d'adjacence du graphe
    community (str/int) : étiquette d'une communauté
    communities (dict) : dictionnaire des communauté de la forme {noeud:communauté}
    return (int) : somme des poids au sein d'une communauté
    """
    return sum(weight for node in graph for neighbor, weight in graph[node]
               if communities[node] == community and communities[neighbor] == community)

def calculate_weighted_edges_in_community(graph, community, communities):
    """renvoie la somme des poids des liens partant d'une communautée donnée
    graph (dict) : lisyte d'adjacence du graphe
    community (str/int) : étiquette d'une communauté
    communities (dict) : dictionnaire des communauté de la forme {noeud:communauté}
    return (int) : somme des poids des liens partant d'une communauté
    """
    return sum(weight for node in graph for _, weight in graph[node]
               if communities[node] == community)


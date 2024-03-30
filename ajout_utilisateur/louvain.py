from matplotlib.pyplot import *

def louvain(graph,calculate_modularity):
    """Applique l'algorithme de louvain pour découper un graphe en communautés
    graph (dict) : liste d'djacences du graphe
    calculate_modularity (function) : fonction de calcule de la métrique"""
    def initialize_communities(graph):
        """renvoie un dictionnaire de communautés ou chauqe noued est dans sa propre communauté
        graph (dict) : liste d'adjacence du graphe
        return (dict) : dictionnaire {noeud : communauté}
        """
        return {node: i for i, node in enumerate(graph)}

    def neighbors(node, graph):
        """renvoie la liste des voisin d'un noeud
        node (int/str) : noeud dont on veut les voisins
        graph (dict) : liste d'adjacence du graphe
        return (list) : voisins du noeud
        """
        return [neighbor for neighbor, _ in graph[node]]

    def move_node(node, neighbor, communities):
        """déplace un noeud d'une communauté vers une autre
        node (int/str) : noeud à déplacer
        neighbor (int/str) : noeud issu de la communauté ou l'on souhaite mettre le neoud
        communities (dict) : dictionnaire des communautés sous la forme {noeud : communauté}
        return (dict) : nouveau dictionnaire des communautés
        """
        # on fait une copie du dictionnaire des communautés
        new_communities = communities.copy()
        # on remplace la communauté du noeud souhaité par celle du noeud choisi
        new_communities[node] = new_communities[neighbor]
        # on renvoie le nouveau dictionnaire
        return new_communities

    def display_modularity_evolution(modularity_evolution):
        """ Affiche la courbe de l'évolution de la métrique
        modularity_evolution (list) : liste des différentes valeurs que prend la métrique au court des itérations
        """
        # on met en abscicce le nombre d'itérations
        N = [i for i in range(len(modularity_evolution))]
        # on trace la courbe
        plot(N,modularity_evolution,marker='o',linestyle='-')
        # Légende du graphique
        title('Evolution de la métrique au cours des itérations')
        ylabel('Métrique')
        xlabel('Nb itérations')
        legend()
        show()

    # variables
    communities = initialize_communities(graph)                 # dictionnaire des communautés
    best_modularity = calculate_modularity(graph, communities)  # modulaeité du decoupage des communautés initiale
    modularity_evolution = [best_modularity]                    # liste stockant l'évolution de la modularité

    # déroulement de l'algorithme de louvain
    while True:
        # on parcours les noeud du graphe
        for node in graph:
            # on essaie de le déplacer dans les communautés de chacun de ses voisins
            for neighbor in neighbors(node, graph):
                new_communities = move_node(node, neighbor, communities)
                # on calcule la modularité après le déplacement
                current_modularity = calculate_modularity(graph, new_communities)
                # si celle-ci est meilleure on la garde pour la suite
                if current_modularity > best_modularity:
                    best_modularity = current_modularity
                    communities = new_communities
                    modularity_evolution.append(current_modularity)

        # Si la modularité n'évolue plus, terminer
        if best_modularity == calculate_modularity(graph, communities):
            break

    display_modularity_evolution(modularity_evolution)
    return communities
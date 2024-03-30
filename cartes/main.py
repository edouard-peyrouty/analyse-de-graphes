from graphes import *
from parcours import *
from detection_cycle import *
from recherche_chaine import *
from dijkstra import *

def creation_graphe():
    """contruit un graphe
    return (dict) : liste d'adjacences du graphe"""
    graph = init_graph(6)
    add_edge(graph,0,1,4)
    add_edge(graph,0,4,6)
    add_edge(graph,1,2,3)
    add_edge(graph,1,3,10)
    add_edge(graph,2,3,2)
    add_edge(graph,2,5,3)
    return graph


if __name__ == "__main__":
    # création du graphe 
    graph = creation_graphe()
    
    # affichage du graphe
    print_graph(graph)

    # parcours en largeur du graphe
    print(bfs(graph,1))

    # parcours en profondeur du graphe
    print(dfs(graph,2))

    # recherche de cycle
    print(detection_cycle(graph))

    # recherche de chaine
    print(chaine(graph,4,5))

    # plus court chemin
    print(dijkstra(graph,0,3))
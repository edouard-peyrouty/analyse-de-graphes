import networkx as nx
import matplotlib.pyplot as plt
from louvain import louvain
from fichier_operations import read_file
from graph_operations import graphe_personnages
from calculate_conductance import calculate_conductance
from calculate_modularity import calculate_modularity

if __name__ == "__main__":
    # étape 1 : Lire les données
    personnages = read_file("data/personnagesMIS.txt")
    relations = read_file("data/relationsMIS.txt")
    print("étape 1 : ok")

    # étape 2 : Construire le graphe
    graph = graphe_personnages(personnages, relations)
    print("étape 2 ok")

    # Demander à l'utilisateur de choisir la mesure de qualité
    user_choice = input("Choisissez la mesure de qualité (1 pour modularity, 2 pour conductance): ")

    # on met dans la variables quality_mesure la fonction de calcule de la métrique choisie
    if user_choice == "1":
        quality_measure = calculate_modularity
    elif user_choice == "2":
        quality_measure = calculate_conductance
    else:
        print("Choix non valide. Utilisation de modularity par défaut.")
        quality_measure = calculate_modularity

    # étape 3 : recherche de communauté par l'algorithme de Louvain
    communautes = louvain(graph,quality_measure)
    print("étape 3 : ok")

    # étape 4 : afficher les communautés
    # Convertir le dictionnaire en un objet Graph de NetworkX
    G = nx.Graph({node: {v: weight for v, weight in neighbors} for node, neighbors in graph.items()})

    # Utiliser l'algorithme de disposition spring_layout avec une valeur spécifique de k
    k_value = 2000
    pos = nx.circular_layout(G, scale=k_value)

    # Ajuster les positions des nœuds en fonction de leur communauté
    for node, community in communautes.items():
        pos[node][0] += community * 0.1  # Ajustement horizontal basé sur la communauté
        pos[node][1] += community * 1.0  # Ajustement vertical basé sur la communauté

    # Définir les couleurs pour chaque nœud en fonction de sa communauté
    node_colors = [communautes[node] for node in G.nodes()]

    # Visualiser le graphe avec des couleurs de communauté
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color=node_colors, cmap=plt.cm.Set1,
            edge_color='gray')
    plt.show()

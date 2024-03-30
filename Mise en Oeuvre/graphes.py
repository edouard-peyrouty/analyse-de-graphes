def init_graph(order):
    """Créé la liste d'adjacences vide d'un graphe
    order (int) : ordre du graphe
    return (dict{int:list}) : liste d'adjacences vide"""
    return {i : [] for i in range(order)}

def add_edge(graph,src,dest,weight=1,oriented=False):
    """Ajoute une arrête à la loste d'ajdacence d'un graphe
    graph (dict) : liste d'adjacences du graphe
    src,dest (int) : extrémités de l'arête
    weigth (int) : poids de l'arête
    oriented (bool) : si vrai alors l'arête est a sens unique src -> dest"""
    graph[src].append((dest,weight))
    if not oriented:
        graph[dest].append((src,weight))

def print_graph(graph):
    """Affiche la liste d'adjacences d'un graphe
    graph (dict) : liste d'djacences"""
    for noeud,voisins in graph.items():
        print(f"Liste d'adjacence pondérée du noeud {noeud} : ", end="")
        for voisin,weight in voisins:
            print(f" -> ({voisin},{weight})",end="")
        print()

        
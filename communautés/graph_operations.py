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
        print(f"{noeud} : ", end="")
        for voisin,weight in voisins:
            print(f" -> ({voisin},{weight})",end="")
        print()

def graphe_personnages(noeuds,aretes):
    """crée le graphe des relations des personnages des misérables"""
    # on génère les noeuds du graphe
    graph_numerique = init_graph(len(noeuds))

    # on ajoute les arêtes
    for noeud1,noeud2_et_poids in aretes.items():
        noeud2,poids = noeud2_et_poids
        add_edge(graph_numerique,noeud1,noeud2,poids)

    # on remplace les clés numériques par les noms des personnages
    graph_nom = {noeuds[perso]:[(noeuds[num_perso],poids) for num_perso,poids in liste_relation] for perso,liste_relation in graph_numerique.items()}

    return graph_nom
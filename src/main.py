from graphe import Graphe

NOMBRE_SOMMET = 12

"""
def generer_graphe_barabasi_albert(m):
    graphe = Graphe.graphe_barabasi_albert(m)


def generer_graphe_aleatoire(nombre_sommet):
    graphe = Graphe.graphe_aleatoire(nombre_sommet)

"""

if __name__ == '__main__':
    R = []
    X = []
    graphe = Graphe().graphe_aleatoire(NOMBRE_SOMMET)
    graphe.afficher_graphe()

    print("\n*************************** SANS PIVOT ***************************")
    print(list(graphe.bron_kerbosch_sans_pivot(list(graphe.liste_adjacence.keys()), R, X)))

    print("\n*************************** AVEC PIVOT ***************************")
    print(list(graphe.bron_kerbosch_avec_pivot(list(graphe.liste_adjacence.keys()), R, X)))

    print("\n********************* AVEC ORDRE DE DEGENERESCENCE ********************")
    print(list(graphe.version_avec_ordonnancement()))

    print("\n********************* ENUMERATION CLIQUES MAXIMALES ********************")
    print(graphe.enumeration_cliques_max())
    
    print("\n****************** ENUMERATION CLIQUES MAXIMALES V2 *****************")
    print(list(graphe.enumeration_cliques_max_2()))


    # Dessiner des graphes
    graphe.dessiner_graphe()
 
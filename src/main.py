from graphe import Graphe

NOMBRE_SOMMET = 12

"""
def generer_graphe_barabasi_albert(m):
    graphe = Graphe.graphe_barabasi_albert(m)


def generer_graphe_aleatoire(nombre_sommet):
    graphe = Graphe.graphe_aleatoire(nombre_sommet)

"""

if __name__ == '__main__':

    #graphe = Graphe().graphe_aleatoire(NOMBRE_SOMMET)
    R = []
    X = []
    graphe = Graphe().graphe_barabasi_albert(9)
    graphe.afficher_graphe()

    print("*************************** SANS PIVOT ***************************")
    print(list(graphe.bron_kerbosch_sans_pivot(list(graphe.liste_adjacence.keys()), R, X)))

    print("*************************** AVEC PIVOT ***************************")
    print(list(graphe.bron_kerbosch_avec_pivot(list(graphe.liste_adjacence.keys()), R, X)))

    print("********************* AVEC ORDRE DE DEGENERESCENCE ********************")
    print(list(graphe.version_avec_ordonnancement()))

    print("********************* ENUMERATION CLIQUES MAXIMALES ********************")
    print(graphe.enumeration_cliques_max())
    
    print("****************** ENUMERATION CLIQUES MAXIMALES V2 *****************")
    graphe.enumeration_cliques_max_2()

    # Dessiner des graphes
    graphe.dessiner_graphe()
 
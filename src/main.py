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

    graphe = Graphe().graphe_aleatoire(NOMBRE_SOMMET)
    graphe.afficher_graphe()
    R = []
    X = []
    graphe.bron_kerbosch_sans_pivot(list(graphe.liste_adjacence.keys()), R, X)

    # Dessiner des graphes
    graphe.dessiner_graphe()


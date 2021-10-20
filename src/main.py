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

    graphe = Graphe().graphe_barabasi_albert(9)
    graphe.afficher_graphe()
    R = []
    X = []

    print(list(graphe.bron_kerbosch_avec_pivot(list(graphe.liste_adjacence.keys()), None, X)))


    # Dessiner des graphes
    graphe.dessiner_graphe()


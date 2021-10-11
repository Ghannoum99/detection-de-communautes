from graphe import Graphe
import networkx as nx
import matplotlib.pyplot as plt

NOMBRE_SOMMET = 4

"""
def generer_graphe_barabasi_albert(m):
    graphe = Graphe.graphe_barabasi_albert(m)


def generer_graphe_aleatoire(nombre_sommet):
    graphe = Graphe.graphe_aleatoire(nombre_sommet)

"""

if __name__ == '__main__':

    graphe = Graphe().graphe_barabasi_albert(3)
    graphe.afficher_graphe()

    # Dessiner des graphes
    graphe.dessiner_graphe()

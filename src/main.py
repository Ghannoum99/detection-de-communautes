# -*- coding: utf-8 -*-

from graphe import Graphe

NOMBRE_SOMMET = 12
m = 7

if __name__ == '__main__':
    # initialisation de 2 listes vides
    R = list()
    X = list()

    # Creation d'un objet graphe
    # Générer un graphe aléatoire
    #graphe = Graphe().graphe_aleatoire(NOMBRE_SOMMET)

    # Générer un graphe selon le modele de Barabasi
    graphe = Graphe().graphe_barabasi_albert(m)

    graphe.afficher_graphe()

    print("\n%%%%%%%%%%%%%%%%%%%%%%% SANS PIVOT %%%%%%%%%%%%%%%%%%%%%%%")
    print(list(graphe.bron_kerbosch_sans_pivot(list(graphe.liste_adjacence.keys()), R, X)))

    print("\n%%%%%%%%%%%%%%%%%%%%%%%  AVEC PIVOT %%%%%%%%%%%%%%%%%%%%%%%")
    print(list(graphe.bron_kerbosch_avec_pivot(list(graphe.liste_adjacence.keys()), R, X)))

    print("\n%%%%%%%%%%%%%%%%%%%%%%% AVEC ORDRE DE DEGENERESCENCE %%%%%%%%%%%%%%%%%%%%%%%")
    print(list(graphe.version_avec_ordonnancement()))

    print("\n%%%%%%%%%%%%%%%%%%%%%%% ENUMERATION CLIQUES MAXIMALES %%%%%%%%%%%%%%%%%%%%%%%")
    print(graphe.enumeration_cliques_max())
    
    print("\n%%%%%%%%%%%%%%%%%%%%%%%  ENUMERATION CLIQUES MAXIMALES V2 %%%%%%%%%%%%%%%%%%%%%%%")
    print(list(graphe.enumeration_cliques_max_2()))
    
    # Dessiner l'objet graphe
    graphe.dessiner_graphe()
 
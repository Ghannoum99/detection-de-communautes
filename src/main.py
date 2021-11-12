# -*- coding: utf-8 -*-

from graphe import Graphe

NOMBRE_SOMMET = 15
m = 7

if __name__ == '__main__':
    # initialisation de 2 listes vides
    R = list()
    X = list()

    # Creation d'un objet graphe
    # Générer un graphe aléatoire
    graphe = Graphe().graphe_aleatoire(NOMBRE_SOMMET)

    # Générer un graphe selon le modele de Barabasi
    #graphe = Graphe().graphe_barabasi_albert(m)
    print("%%%%%%%%%%%%%%%%% Liste d'adjacence : %%%%%%%%%%%%%%%%%")
    graphe.afficher_graphe()

    print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Bron-Kerbosh sans pivot : %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print(list(graphe.bron_kerbosch_sans_pivot(list(graphe.liste_adjacence.keys()), R, X)))

    print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Bron-Kerbosh avec pivot : %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print(list(graphe.bron_kerbosch_avec_pivot(list(graphe.liste_adjacence.keys()), R, X)))

    print("\n%%%%%%%%%%%%%%%%%%%%% Bron-Kerbosh avec ordre de degenerescence : %%%%%%%%%%%%%%%%%%%%%%%")
    print(list(graphe.version_avec_ordonnancement()))

    print("\n%%%%%%%%%%%%%%%%%%%%%%% ENUMERATION CLIQUES MAXIMALES Version 1 : %%%%%%%%%%%%%%%%%%%%%%%")
    print(graphe.enumerer_cliques_max_v1())
    
    print("\n%%%%%%%%%%%%%%%%%%%%%%% ENUMERATION CLIQUES MAXIMALES Version 2 : %%%%%%%%%%%%%%%%%%%%%%%")
    print(list(graphe.enumerer_cliques_max_v2()))
    
    # Dessiner l'objet graphe
    graphe.dessiner_graphe()
 
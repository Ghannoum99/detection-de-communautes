# -*- coding: utf-8 -*-

from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
import random

"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%               Outils Pour La Conception D'Algorithmes
%
%                   ISTY - IATIC 4 [2021 - 2022]
%
%   Sujet : Détection de communautes dans des réseaux sociaux
%
%   Auteurs: GHANNOUM Jihad - KHIARI Slim - NOUIRA Nessrine - TOIHIR Yoa
%   
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""


class Graphe:

    def __init__(self, liste_adjacence: dict = {}):
        self.liste_adjacence = liste_adjacence

    # Fonction permettant de calculer le nombre de sommets d'un graphe
    def get_nombre_sommet(self):
        return len(self.liste_adjacence.keys())

    # Fonction permettant de calculer le nombre d'aretes dans un graphe
    def get_nombre_aretes(self):
        aretes = 0
        for sommet in self.liste_adjacence.values():
            aretes += sum([len(sommet)])

        return aretes / 2

    # Fonction permettant de calculer le degré d'un graphe représenté par sa liste d'adjacence
    # ( somme de degrées de chaque sommet du graphe)
    def get_somme_degres(self, liste_adjacence):
        somme_degres = 0
        for sommet in liste_adjacence.values():
            somme_degres += sum([len(sommet)])

        return somme_degres

    # Fonction permettant d'initialiser la liste d'adjacence
    # Entrée : le nombre de sommet (n)
    # Cette fonction permet de créer une liste d'adjacence de n sommets
    # En premier temps chaque sommet est de degré 0
    # Elle sera utilisée dans la fonction de génération des graphes aléatoires
    def initialiser_liste_adjacence(self, nombre_sommet):
        liste_adjacence = {}
        for sommet in range(1, nombre_sommet + 1):
            liste_adjacence[sommet] = []

        return liste_adjacence

    # Fonction permettant d'afficher la liste d'adjacence de chaque sommet
    def afficher_graphe(self):
        for sommet, voisin in self.liste_adjacence.items():
            print("L(" + str(sommet) + ") = " + str(self.liste_adjacence[sommet]))

    # Fonction permettant de dessiner un graphe
    def dessiner_graphe(self):
        # creation d'un graphe G vide
        G = nx.DiGraph()

        for sommet in self.liste_adjacence.keys():
            # ajouter le sommet en cours au graphe G
            G.add_node(sommet)

            # parcourir la liste de voisins du sommet en cours
            for voisin in range(0, len(self.liste_adjacence[sommet])):
                # ajouter une arete (sommet,voisin)
                G.add_edge(sommet, self.liste_adjacence[sommet][voisin])

        # Positionner les nœuds en utilisant l'algorithme Fruchterman-Reingold force-directed.
        pos = nx.spring_layout(G)

        # dessiner les noeuds du graphe G
        nx.draw_networkx_nodes(G, pos)
        # dessiner les étiquettes des nœuds sur le graphe G.
        nx.draw_networkx_labels(G, pos)
        # dessiner les aretes du graphe G
        nx.draw_networkx_edges(G, pos, edge_color='r', arrows=False)
        # afficher le graphe
        plt.show()

    # Fonction permettant d'avoir la liste de voisins d'un sommet donné
    def get_voisins(self, sommet):
        return self.liste_adjacence[sommet]

    """
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    %   PREMIERE PARTIE : GENERER DES GRAPHES ALEATOIRES
    %
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """

    # Partie 1.1

    # Algorithme pour générer un graphe aléatoire
    def graphe_aleatoire(self, nombre_sommet):
        liste_adjacence = {}

        # Initialisation de la liste d'adjascence
        liste_adjacence = self.initialiser_liste_adjacence(nombre_sommet)

        for sommet in liste_adjacence.keys():

            # Mise à jour de la liste d'adjascence pour obtenir les mêmes
            # sommets dans la liste d'adjacence du sommet voisin et la liste d'adjascence du sommet en cours
            if sommet > 1:
                for voisin_possible in liste_adjacence.keys():
                    if sommet in liste_adjacence[voisin_possible]:
                        liste_adjacence[sommet].append(voisin_possible)

            # L'ajout aléatoire d'une arête dans le graphe
            for sommet_voisin in range(sommet + 1, len(liste_adjacence) + 1):
                if sommet_voisin not in liste_adjacence[sommet]:
                    probabilite = random.gauss(0, 2)
                    if (probabilite > 0) and (probabilite < 1):
                        # Il faut ajouter l'arete selon l'ordre
                        # premiere arete du sommet 1 c'est l'arete qui relie le sommet 1 et le sommet 2
                        liste_adjacence[sommet].append(sommet_voisin)

        return Graphe(liste_adjacence)

    # Partie 1.2

    # Algorithme pour générer un graphe aléatoire avec le modéle Barabasi-Albert
    def graphe_barabasi_albert(self, m):
        if m <= 0:
            return Graphe()

        # Initialement le graphe est graphe triangle
        liste_adjacence = defaultdict(list, {1: [2, 3], 2: [1, 3], 3: [1, 2]})

        for i in range(3, 3 + m):
            # Calcul de la somme des degrées
            somme_degres = self.get_somme_degres(liste_adjacence)

            # Récuperation des noeuds
            noeuds = set(liste_adjacence.keys()) - {i} - set(liste_adjacence[i])

            for noeud in noeuds:
                degree = len(liste_adjacence[noeud])  # degree : degree du noeud en cours
                probabilite = degree / somme_degres
                # si la valeur aléatoire < probabilité, on va ajouter ce noeud
                if random.random() < probabilite:
                    liste_adjacence[i].append(noeud)
                    liste_adjacence[noeud].append(i)

        return Graphe(liste_adjacence)

    """
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    %   DEUXIEME PARTIE : Algorithmes de Bron-Kerbosch
    %
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """

    # Partie 2.1

    # Algorithme de Bron Kerbosch Version Standard
    # P: ensemble des sommets
    # R: un sous ensemble des sommets de la potentielle clique
    # X: contient des sommets deja traites
    def bron_kerbosch_sans_pivot(self, P, R=None, X=None):
        P = list(P)
        R = list() if R is None else R
        X = list() if X is None else X

        # if P union X = 0 --> reporter R comme clique maximale
        if len(P + X) == 0:
            yield R

        else:
            for sommet in P[:]:
                yield from self.bron_kerbosch_sans_pivot(list(set(P) & set(self.get_voisins(sommet))), R + [sommet],
                                                         list(set(X) & set(self.get_voisins(sommet))))

                P.remove(sommet)
                X.append(sommet)

    # Partie 2.2

    # Algorithme de Bron Kerbosch avec pivot
    def bron_kerbosch_avec_pivot(self, P, R=None, X=None):
        P = list(P)
        R = list() if R is None else R
        X = list() if X is None else X

        # if P union X = 0 --> raporter R comme clique maximale
        if len(P + X) == 0:
            yield R
        else:
            # choisir un pivot selon l'algo de Tomita
            pivot = self.pivot_tomita(P, X)

            # parcourir la liste P privée de N(pivot)
            # avec N(pivot) : la liste des voisins du sommet pivot
            for sommet in list(set(P).difference(self.get_voisins(pivot))):
                yield from self.bron_kerbosch_avec_pivot(list(set(P) & set(self.get_voisins(sommet))), R + [sommet],
                                                         list(set(X) & set(self.get_voisins(sommet))))

                P.remove(sommet)
                X.append(sommet)

    # choisir un pivot pour minimiser le nombre d'appels récursif
    # cet algorithme consiste à prendre u tel que |P inter N(u)| soit maximal
    # N(u) : les voisins du sommet u.
    def pivot_tomita(self, P, X):
        # L'union de P et X
        P_union_X = list(P + X)
        # initialiser u comme le premier sommet de P union X
        u = P_union_X[0]

        # L'intersection de P et N(u)
        P_inter_voisin_de_u = list(set(P) & set(self.get_voisins(u)))
        # initialiser le degre max à la taille de la liste ( P inter N(u) )
        degre_max = len(P_inter_voisin_de_u)

        # P Union X privée de u
        # P union X \ {u}
        P_union_X_privee_de_u = list(set(P_union_X) - {u})

        for v in P_union_X_privee_de_u:
            # L'intersection de P et N(v)
            P_inter_voisin_de_v = list(set(P) & set(self.get_voisins(v)))
            if len(P_inter_voisin_de_v) > degre_max:
                u = v
                degre_max = len(P_inter_voisin_de_v)
        return u

    # Version avec ordonnancement des noeuds
    def version_avec_ordonnancement(self):
        P = list(self.liste_adjacence.keys())
        X = []
        liste_sommets_degenerescence = self.get_degenerescence_graphe()

        for sommet in liste_sommets_degenerescence:
            yield from self.bron_kerbosch_avec_pivot(list(set(P).intersection(self.get_voisins(sommet))), [sommet],
                                                     list(set(X).intersection(self.get_voisins(sommet))))

            P.remove(sommet)
            X.append(sommet)

    # Algorithme de dégénérescence d'un graphe
    # Cet algorithme retourne un int contenant la dégénérescence et la liste
    # de sommets dans un ordre optimal pour la coloration de graphe
    # (commençant par le sommet ayant le plus haut degré)
    def get_degenerescence_graphe(self):
        # Initialisation d'une liste L qui sera retournée
        L = []

        # Initialisation d'une liste D qui contiendra dans chacune 
        # de ses cases, les sommets ayant un degré correspondant 
        # à l'indice de la case
        D = []

        nbr_voisins_max = max(map(lambda x: len(x), self.liste_adjacence.values()))
        D = [list() for i in range(nbr_voisins_max + 1)]

        for sommet, liste in self.liste_adjacence.items():
            i = len(liste)
            D[i].append(sommet)

        # Initialisation de k à 0
        k = 0
        n = len(self.liste_adjacence.keys())
        x = 0

        while x <= n:
            x = x + 1
            # On parcourt les cases de D en cherchant une qui n'est pas vide
            for i in range(nbr_voisins_max + 1):
                if D[i]:
                    k = max([k, i])
                    # On sélectionne aléatoirement un sommet dans D
                    v = random.choice(D[i])
                    # On ajoute le sommet v au début de la liste L
                    L.insert(0, v)
                    # On supprime le sommet v de D
                    D[i].remove(v)
                    voisins_v = self.get_voisins(v)
                    # On parcourt tous les voisins de v 
                    for w in voisins_v:
                        if w not in L:
                            # On cherche à retirer un degré à w et à le déplacer 
                            # à l'indice correspondant dans D 
                            iterateur = filter(lambda x: x not in L or x == v, self.get_voisins(w))
                            list_voisins = list(iterateur)
                            ind = len(list_voisins)
                            D[ind].remove(w)
                            D[ind - 1].append(w)

        return L

    """
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    %   TROISIEME PARTIE : Algorithmes d’énumération des cliques en fonction de la dégénérescence
    %
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """

    # Partie 3.1

    # Algorithme d'énumération des cliques maximales
    def enumerer_cliques_max_v1(self):
        # Calcul de l'ordre de dégénérescence du graphe
        liste_degenerescence = self.get_degenerescence_graphe()

        # On initialise une table de hachage vide
        T: dict = {}

        # Génération des sous-graphes du graphe
        operator_ss_graphes = self.generer_sous_graphes(list(liste_degenerescence), [], list(liste_degenerescence))
        sous_graphes = []
        ss_graphe_dict: dict = {}
        for ss_graphe in operator_ss_graphes:
            ss_graphe_dict.clear()
            for sommet in ss_graphe:
                voisins = list(filter(lambda x: x in ss_graphe, self.get_voisins(sommet)))
                ss_graphe_dict[sommet] = voisins
            sous_graphes.append(Graphe(ss_graphe_dict))

        n = len(sous_graphes)

        for j in range(0, n-1):
            SG = sous_graphes[j]
            cliques_maximales = SG.version_avec_ordonnancement()
            for clique_k in cliques_maximales:
                # On trie les sommets de la clique en respectant l'ordre de dégénérescence 
                liste_degenerescence_clique_k = sorted(set(liste_degenerescence) & set(clique_k),
                                                       key=liste_degenerescence.index)
                if liste_degenerescence_clique_k not in T.values():
                    T[j] = liste_degenerescence_clique_k

        return T

    # Cette fonction permet de générer récursivement tous les sous-graphes d'un graphe
    def generer_sous_graphes(self, sommets_pas_traites, sous_graphes_actu, voisins):
        # On cherche à récupérer une liste de sommets candidats
        # qu'on va traiter pour décider les intégrer à notre liste de sous-graphes
        if not sous_graphes_actu:
            sommets_candidats = sommets_pas_traites
        else:
            sommets_candidats = list(set(sommets_pas_traites) & set(voisins))
        if not sommets_candidats:
            # On retourne les sous-graphes lorsqu'il n'y a plus de sommets candidats
            yield sous_graphes_actu
        else:
            v = random.choice(sommets_candidats)
            sommets_pas_traites.remove(v)
            yield from self.generer_sous_graphes(sommets_pas_traites, sous_graphes_actu, voisins)
            sous_graphes_actu.append(v)
            voisins.extend(self.get_voisins(v))
            yield from self.generer_sous_graphes(sommets_pas_traites, sous_graphes_actu, voisins)

    # Partie 3.2

    # Algorithme d'énumération des cliques maximales 3.2
    def enumerer_cliques_max_v2(self):
        # Calcul de l'ordre de dégénérescence du graphe
        liste_degenerescence = self.get_degenerescence_graphe()

        # Génération des sous-graphes du graphe
        operator_ss_graphes = self.generer_sous_graphes(list(liste_degenerescence), [], list(liste_degenerescence))
        sous_graphes = []
        ss_graphe_dict: dict = {}
        #parcours des sommets puis pour chaque sommet i les voisins du sommet i
        for ss_graphe in operator_ss_graphes:
            ss_graphe_dict.clear()
            for sommet in ss_graphe:
                voisins = list(filter(lambda x: x in ss_graphe, self.get_voisins(sommet)))
                ss_graphe_dict[sommet] = voisins
            sous_graphes.append(Graphe(ss_graphe_dict))

        n = len(sous_graphes)

        res = []
        
        for j in range(0, n-1):
            SG = sous_graphes[j]
            cliques_maximales = SG.version_avec_ordonnancement()
            for clique_k in cliques_maximales:
                for sommet in clique_k :
                    sommets_degen = list(liste_degenerescence)
                    v = sommets_degen[j]

                    present = False
                    for clique_max in res:
                        result = all(elem in clique_max for elem in clique_k)
                        if result:
                            present = True
                    # si les sommets ont un voisin commun d'ordre inférieur dans σ qui est adjacent à tous les sommets de la clique
                    if not (self.verifier_rank_adjacence(sommet, v, liste_degenerescence, clique_k)) and not present:
                        # on insère la clique dans la liste des cliques maximales
                        res.append(clique_k)

        return res

    # Cette méthode vérifie les sommets qui ont un voisin commun d'ordre inférieur et aussi l’adjacence des sommets
    def verifier_rank_adjacence(self, sommet, v, liste, clique):
        voisins_de_x = self.get_voisins(sommet)
        for voisin in voisins_de_x:
            if voisins_de_x.index(voisin) < liste.index(v):
                if self.verifier_adjacence(v, clique):
                    return True
        return False
    
    # Cette méthode sert à vérifier qu’un sommet x est adjacent à un autre sommet dans la liste de sommets
    def verifier_adjacence(self, sommet_recherche, liste_sommets):
        for sommet in liste_sommets:
            if sommet_recherche not in self.get_voisins(sommet):
                return False
        return True
            

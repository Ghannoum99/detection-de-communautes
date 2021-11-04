# -*- coding: utf-8 -*-

"""

Sujet : Détéction des communautes dans des réseaux sociaux

Auteurs : GHANNOUM Jihad - KHIARI Slim - NOUIRA Nessrine - TOIHIR Yoa



1. Expliquer ce qu'on a fait dans la classe Graphe (les attributs et les méthodes)
2. Ajouter des commentaires
3. Expliquer le rôle de chaque variable
4. Ajouter les références (les 2 articles)


"""
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
import random

class Graphe:

    def __init__(self, liste_adjacence: dict = {}):
        self.liste_adjacence = liste_adjacence

    def get_nombre_sommet(self):
        return len(self.liste_adjacence.keys())

    def get_nombre_aretes(self):
        aretes = 0
        for sommet in self.liste_adjacence.values():
            aretes += sum([len(sommet)])

        return aretes / 2

    def get_somme_degrees(self, liste_adjacence):
        somme_degrees = 0
        for sommet in liste_adjacence.values():
            somme_degrees += sum([len(sommet)])

        return somme_degrees

    def initialiser_liste_adjacence(self, nombre_sommet):
        liste_adjacence = {}
        for sommet in range(1, nombre_sommet + 1):
            liste_adjacence[sommet] = []

        return liste_adjacence

    def afficher_graphe(self):
        for sommet, voisin in self.liste_adjacence.items():
            print("L(" + str(sommet) + ") = " + str(self.liste_adjacence[sommet]))

    def dessiner_graphe(self):
        G = nx.DiGraph()

        for sommet in self.liste_adjacence.keys():

            G.add_node(sommet)
            for voisins in range(0, len(self.liste_adjacence[sommet])):
                G.add_edge(sommet, self.liste_adjacence[sommet][voisins])

        pos = nx.spring_layout(G)

        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos, edge_color='r', arrows=False)
        plt.show()

    def get_voisin(self, sommet):
        return self.liste_adjacence[sommet]

    ##############################################################################################################
    ############################### PREMIERE PARTIE : GENERER DES GRAPHES ALEATOIRES #############################
    ##############################################################################################################

    ################################################ PARTIE 1.1 ##################################################
    # EXPLICATION

    def graphe_aleatoire(self, nombre_sommet):
        liste_adjacence = {}

        #Initialisation de la liste d'adjascence
        liste_adjacence = self.initialiser_liste_adjacence(nombre_sommet)

        for sommet in liste_adjacence.keys():

            #Mise à jour de la liste d'adjascence pour obtenir les mêmes sommets dans la liste d'adjacence du sommet voisin et la liste d'adjascence du sommet en cours
            if sommet > 1:
                for voisin_possible in liste_adjacence.keys():
                    if sommet in liste_adjacence[voisin_possible]:
                        liste_adjacence[sommet].append(voisin_possible)

            #L'ajout aléatoire d'une arête dans le graphe
            for sommet_voisin in range(sommet + 1, len(liste_adjacence) + 1):
                if sommet_voisin not in liste_adjacence[sommet]:
                    probabilite = random.gauss(0, 2)
                    if (probabilite > 0) and (probabilite < 1):
                        # Il faut ajouter l'arete selon l'ordre
                        # premiere arete du sommet 1 c'est l'arete qui relie le sommet 1 et le sommet 2
                        liste_adjacence[sommet].append(sommet_voisin)

        return Graphe(liste_adjacence)

    ########################## PARTIE 1.2 : GENERER LES GRAPHES DE Barabasi-Albert #############################
    # EXPLICATION
    def graphe_barabasi_albert(self, m):
        if m <= 0:
            return Graphe()

        # Initialement le graphe est graphe triangle
        liste_adjacence = defaultdict(list, {1: [2, 3], 2: [1, 3], 3: [1, 2]})

        for i in range(3, 3 + m):
            #Calcul de la somme des degrées
            somme_degrees = self.get_somme_degrees(liste_adjacence)

            #Récuperation des noeuds
            noeuds = set(liste_adjacence.keys()) - {i} - set(liste_adjacence[i])

            #Ajout des arretes aleatoirement
            for noeud in noeuds:
                degree = len(liste_adjacence[noeud]) # degree : degree du noeud en cours
                probabilite = degree / somme_degrees
                if random.random() < probabilite:
                    liste_adjacence[i].append(noeud)
                    liste_adjacence[noeud].append(i)

        return Graphe(liste_adjacence)

    ##############################################################################################################
    ############################################# DEUXIEME PARTIE ################################################
    ##############################################################################################################

    ################################################ PARTIE 2.1 ##################################################
    # Algorithme de Bron Kerbosch Version Standard
    # P: ensemble des sommets sommets_candidats pour être ajoutes a la potentielle clique
    # R: un sous ensemble des sommets de la potentielle clique
    # X: contient des sommets deja traites ou appartenant deja a une clique maximale

    def bron_kerbosch_sans_pivot(self, P, R=None, X=None):
        P = list(P)
        R = list() if R is None else R
        X = list() if X is None else X

        if len(P) == 0 and len(X) == 0:
            yield R

        else:
            for sommet in P[:]:
                yield from self.bron_kerbosch_sans_pivot(list(set(P) & set(self.get_voisin(sommet))), R + [sommet],
                                                         list(set(X) & set(self.get_voisin(sommet))))

                P.remove(sommet)
                X.append(sommet)

    ################################################ PARTIE 2.2 ##################################################
    # Algorithme de Bron Kerbosch version améliorée
    # Algorithme de Bron Kerbosch avec pivot
    def bron_kerbosch_avec_pivot(self, P, R=None, X=None):
        P = list(P)
        R = list() if R is None else R
        X = list() if X is None else X

        if len(P) == 0 and len(X) == 0:
            yield R
        else:
            pivot = self.choisir_aleatoirement(set(P)) or self.choisir_aleatoirement(set(X))

            for sommet in list(set(P).difference(self.get_voisin(pivot))):
                yield from self.bron_kerbosch_sans_pivot(list(set(P) & set(self.get_voisin(sommet))), R + [sommet],
                                                         list(set(X) & set(self.get_voisin(sommet))))

                P.remove(sommet)
                X.append(sommet)

    # Choisir un element aléatoire du "Set": ensemble
    def choisir_aleatoirement(self, ensemble):
        if len(ensemble) != 0:
            pivot = ensemble.pop()
            ensemble.add(pivot)
            return pivot

    # Version avec ordonnancement des noeuds
    def version_avec_ordonnancement(self):
        P = list(self.liste_adjacence.keys())
        X = []
        liste_sommets_degenerescence = self.get_degenerescence_graphe()

        for sommet in liste_sommets_degenerescence:
            yield from self.bron_kerbosch_avec_pivot(list(set(P).intersection(self.get_voisin(sommet))), [sommet],
                                                     list(set(X).intersection(self.get_voisin(sommet))))

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
                    voisins_v = self.get_voisin(v)
                    # On parcourt tous les voisins de v
                    for w in voisins_v:
                        if w not in L:
                            # On cherche à retirer un degré à w et à le déplacer
                            # à l'indice correspondant dans D
                            iterateur = filter(lambda x: x not in L or x == v, self.get_voisin(w))
                            list_voisins = list(iterateur)
                            ind = len(list_voisins)
                            D[ind].remove(w)
                            D[ind - 1].append(w)

        return L

    ##############################################################################################################
    ############################################# TROISIEME PARTIE ###############################################
    ##############################################################################################################

    ################################################ PARTIE 3.1 ##################################################
    # Algorithme d'énumération des cliques maximales
    def enumeration_cliques_max(self):
        # Calcul de l'ordre de dégénérescence du graphe
        liste_degenerescence = self.get_degenerescence_graphe()

        # On initialise une table de hachage vide
        T : dict = {}

        # Génération des sous-graphes du graphe
        operator_ss_graphes = self.generer_sous_graphes(list(liste_degenerescence), [], list(liste_degenerescence))
        sous_graphes = []
        ss_graphe_dict : dict = {}
        for ss_graphe in operator_ss_graphes:
            ss_graphe_dict.clear()
            for sommet in ss_graphe:
                voisins = list(filter(lambda x: x in ss_graphe, self.get_voisin(sommet)))
                ss_graphe_dict[sommet]=voisins
            sous_graphes.append(Graphe(ss_graphe_dict))

        n = len(sous_graphes)

        for j in range(0, n):
            SG = sous_graphes[j]
            cliques_maximales = SG.version_avec_ordonnancement()
            for clique_k in cliques_maximales:
                # On trie les sommets de la clique en respectant l'ordre de dégénérescence
                liste_degenerescence_clique_k = sorted(set(liste_degenerescence) & set(clique_k),
                                                       key=liste_degenerescence.index)
                if liste_degenerescence_clique_k not in T.values():
                    T[j] = liste_degenerescence_clique_k

        return T

    # Cette fonction permet de générer tous les sous-graphes d'un graphe
    def generer_sous_graphes(self, sommets_pas_traites, sous_graphes_actu, voisins):
       if not sous_graphes_actu:
           sommets_candidats = sommets_pas_traites
       else:
           sommets_candidats = list(set(sommets_pas_traites) & set(voisins))
       if not sommets_candidats:
           yield sous_graphes_actu
       else:
           v = random.choice(sommets_candidats)
           sommets_pas_traites.remove(v)
           yield from self.generer_sous_graphes(sommets_pas_traites, sous_graphes_actu, voisins)
           sous_graphes_actu.append(v)
           voisins.extend(self.get_voisin(v))
           yield from self.generer_sous_graphes(sommets_pas_traites, sous_graphes_actu, voisins)

    ################################################ PARTIE 3.2 ##################################################
   # Algorithme d'énumération des cliques maximales 3.2
    def enumeration_cliques_max_2(self):
        #récupere le dégres maximale dans le graphe
        k = max(map(lambda x: len(x), self.liste_adjacence.values()))
        # Calcul de l'ordre de dégénérescence du graphe
        liste_degenerescence = self.get_degenerescence_graphe()

        # On initialise une table de hachage vide
        liste_adjacence_degenerescence: dict = {}
        #lister les voisins de chaque sommets
        for sommet in liste_degenerescence:
            liste_adjacence_degenerescence.update({sommet: self.get_voisin(sommet)})

        n = len(self.liste_adjacence.keys()) + 1

        graphe_g_degen = Graphe(liste_adjacence_degenerescence)

        for j in range(1, n):
            # On trie les clique selon leur ordre
            clique_maximales = graphe_g_degen.version_avec_ordonnancement()
            #on va parcourir  tout les clique
            for clique_k in clique_maximales:
                #On va parcourir tout les sommets dans le clique
                for sommet in clique_k:
                    #tester si le voisin de sommet posséde le plus petit ordre et
                    # que la sommet appartient au clique
                    if (len(self.get_voisin(sommet)) < k) and (sommet in clique_k):
                        print("reject")
                    else:
                        #renvoyer les cliques maximale
                        yield from clique_maximales



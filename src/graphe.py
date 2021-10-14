from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
import random


class Graphe:

    def __init__(self, liste_adjacence: dict = {}):
        self.liste_adjacence = liste_adjacence
        print("to", self.liste_adjacence)

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
            print(liste_adjacence)
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

    def verif_graphe_connexe(self, liste_adjacence):
        for sommet in list(liste_adjacence.keys()):
            if len(liste_adjacence[sommet]) < 1:
                del liste_adjacence[sommet]
        return liste_adjacence

    def get_voisin(self, sommet):
        return self.liste_adjacence[sommet]


    ##############################################################################################################
    ############################### PREMIERE PARTIE : GENERER DES GRAPHES ALEATOIRES #############################
    ##############################################################################################################

    ################################################ PARTIE 1.1 ##################################################
    # EXPLICATION

    def graphe_aleatoire(self, nombre_sommet):
        liste_adjacence = {}

        liste_adjacence = self.initialiser_liste_adjacence(nombre_sommet)

        for sommet in liste_adjacence.keys():
            P = liste_adjacence
            #del P[sommet]

            for voisin_possible in P.keys():
                if sommet in P[voisin_possible]:
                    liste_adjacence[sommet].append(voisin_possible)

            liste_voisin = []
            liste_voisin = list(P.keys())
            for sommet_voisin in range(sommet + 1 , len(liste_adjacence) + 1):
                if sommet_voisin not in liste_adjacence[sommet]:
                    #probabilite = random.gauss(0, 1)
                    probabilite = random.random()
                    print("proba(" + str(sommet) + ", " + str(sommet_voisin) + ") = " + str(probabilite))
                    if (probabilite > 0) and (probabilite < 1):
                        # Il faut ajouter l'arete selon l'ordre
                        # premiere arete du sommet 1 c'est l'arete qui relie le sommet 1 et le sommet 2
                        liste_adjacence[sommet].append(sommet_voisin)

        liste_adjacence = self.verif_graphe_connexe(liste_adjacence)
        return Graphe(liste_adjacence)

    ########################## PARTIE 1.2 : GENERER LES GRAPHES DE Barabasi-Albert #############################
    # EXPLICATION
    def graphe_barabasi_albert(self, m):
        if m <= 0:
            return Graphe()

        # Initialement le graphe est graphe triangle
        liste_adjacence = defaultdict(list, {1: [2, 3], 2: [1, 3], 3: [1, 2]})

        for i in range(3, 3 + m):
            somme_degrees = self.get_somme_degrees(liste_adjacence)

            noeuds = set(liste_adjacence.keys()) - {i} - set(liste_adjacence[i])

            for noeud in noeuds:
                degree = len(liste_adjacence[noeud])
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
    # P: ensemble des sommets candidats pour être ajoutes a la potentielle clique
    # R: un sous ensemble des sommets de la potentielle clique
    # X: contient des sommets deja traites ou appartenant deja a une clique maximale
    # Cet algorithme n'est pas efficace pour les graphes qui contiennent beaucoup de cliques non maximales
    def bron_kerbosch_sans_pivot(self, P, R, X):
        if len(P) == 0 and len(X) == 0:
            return R
        else:
            for sommet in P:
                R.append(sommet)
                self.bron_kerbosch_sans_pivot(list(set(P).intersection(self.get_voisin(sommet))), R,
                                              list(set(X).intersection(self.get_voisin(sommet))))
                # P.remove(sommet)
                del P[sommet]
                X.append(sommet)


    ################################################ PARTIE 2.2 ##################################################
    # Algorithme de Bron Kerbosch version améliorée

    # Algorithme de Bron Kerbosch avec pivot
    def bron_kerbosch_avec_pivot(self, P, R, X):
        if len(P) == 0 and len(X) == 0:
            print("R", R)
            return R
        else:
            list_u = random.choices(P + X)
            u = list_u[0]

            iterateur = filter(lambda x: x not in self.get_voisin(u), P)
            list_voisins = list(iterateur)

            P.extend(list_voisins)

            for sommet in P:
                R.append(sommet)
                self.bron_kerbosch_avec_pivot(list(set(P).intersection(self.get_voisin(sommet))), R,
                                              list(set(X).intersection(self.get_voisin(sommet))))

                P.remove(sommet)
                X.append(sommet)

    # Version avec ordonnancement des noeuds
    def version_avec_ordonnancement(self):
        P = list(self.liste_adjacence.keys())
        R = []
        X = []
        V = []
        liste_sommets_degenerescence = self.get_degenerescence_graphe()[1]

        for sommet in liste_sommets_degenerescence:
            R.clear()
            R.append(sommet)
     
            print("retour", self.bron_kerbosch_avec_pivot(list(set(P).intersection(self.get_voisin(sommet))), R,
                                                 list(set(X).intersection(self.get_voisin(sommet)))))

            P.remove(sommet)
            X.append(sommet)

        return V

    # Algorithme de dégénérescence d'un graphe
    # Cet algorithme retourne un ordre de dégénérescence des sommets du graphe
    # commençant par le sommet ayant le plus haut degré
    def get_degenerescence_graphe(self):
        L = list()
        D = []

        nbr_voisins_max = max(map(lambda x: len(x), self.liste_adjacence.values()))
        D = [list() for i in range(nbr_voisins_max + 1)]

        for sommet, liste in self.liste_adjacence.items():
            i = len(liste)
            D[i].append(sommet)

        k = 0
        n = len(self.liste_adjacence.keys())
        x = 0

        while x <= n:
            x = x + 1
            print("\nD", D)
            print("L", L)
            for i in range(nbr_voisins_max + 1):
                if D[i]:
                    k = max([k, i])
                    v = random.choice(D[i])
                    print("\nv", v)
                    L.insert(0, v)
                    print("L", L)
                    D[i].remove(v)
                    voisinsV = self.liste_adjacence[v]
                    print("voisins", voisinsV)
                    for w in voisinsV:
                        if w not in L:
                            print("voisin", w)
                            iterateur = filter(lambda x: x not in L or x == v, self.get_voisin(w))
                            list_voisins = list(iterateur)
                            ind = len(list_voisins)
                            D[ind].remove(w)
                            D[ind - 1].append(w)
                    print("\nD", D)

        print("L", L)

        return [k, L]

    ##############################################################################################################
    ############################################# TROISIEME PARTIE ###############################################
    ##############################################################################################################


    ################################################ PARTIE 3.1 ##################################################
    # EXPLICATION
    # Algorithme d'énumération des cliques maximales
    def enumeration_cliquesMax(self):
        k = self.get_degenerescence_graphe()[0]
        liste_degenerescence = self.get_degenerescence_graphe()[1]

        liste_adjacence_degenerescence: dict = {}
        for sommet in liste_degenerescence:
            liste_adjacence_degenerescence.update({sommet: self.get_voisin(sommet)})

        T = []

        n = len(self.liste_adjacence.keys())

        graphe_g_degen = Graphe(liste_adjacence_degenerescence)

        for j in range(1, n):
            clique_maximales = graphe_g_degen.version_avec_ordonnancement()
            for clique_k in clique_maximales:
                iterateur = filter(lambda x: x in clique_k, self.liste_adjacence)
                liste_adjacence_clique_k = list(iterateur)
                grapheclique_k = Graphe(liste_adjacence_clique_k)
                liste_degenerescence_clique_k = grapheclique_k.get_degenerescence_graphe()[1]
                countclique_k = T.count(liste_degenerescence_clique_k)
                if countclique_k > 0:
                    print("reject")
                else:
                    T.append(liste_degenerescence_clique_k)
                    return liste_degenerescence_clique_k

        return T


    ################################################ PARTIE 3.2 ##################################################
    # EXPLICATION



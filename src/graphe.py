from collections import defaultdict
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
            print(liste_adjacence)
        return liste_adjacence

    def afficher_graphe(self):
        for sommet, voisin in self.liste_adjacence.items():
            print("L(" + str(sommet) + ") = " + str(self.liste_adjacence[sommet]))

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

    def get_voisin(self, sommet):
       return self.liste_adjacence[sommet]

    # P: ensemble des sommets candidats pour être ajoutes a la potentielle clique
    # R: un sous ensemble des sommets de la potentielle clique
    # X: contient des sommets deja traites ou appartenant deja a une clique maximale
    # Cet algorithme n'est pas efficace pour les graphes qui contiennent beaucoup de cliques non maximales
    def bron_kerbosch_sans_pivot(self, P, R, X):
        if len(P) == 0 and len(X) == 0:
            return R
        else:
            for sommet in P:
                self.bron_kerbosch_sans_pivot(list(set(P).intersection(self.get_voisin(sommet))), R.append(sommet),
                                              list(set(X).intersection(self.get_voisin(sommet))))
                P.remove(sommet)
                X.append(sommet)

    # Algorithme de Bron Kerbosch avec pivot
    def bron_kerbosch_avec_pivot(self, P, R, X):
        if len(P) == 0 and len(X) == 0:
            return R
        else:
            u = random.choices(P + X)
            for sommet in P.extend(self.get_voisin(u)):
                self.bron_kerbosch_avec_pivot(list(set(P).intersection(self.get_voisin(sommet))), R.append(sommet),
                                              list(set(X).intersection(self.get_voisin(sommet))))

                P.remove(sommet)
                X.append(sommet)

    # Version avec ordonnancement des noeuds
    def version_avec_ordonnancement(self, graphe):
        P = list(self.liste_adjacence.keys())
        R = []
        X = []
        for sommet in graphe.liste_adjacence.keys():
            self.bron_kerbosch_avec_pivot(list(set(P).intersection(self.get_voisin(sommet))), sommet,
                                          list(set(X).intersection(self.get_voisin(sommet))))
            P.remove(sommet)
            X.append(sommet)

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
                    probabilite = random.gauss(0, 1)
                    print("proba(" + str(sommet) + ", " + str(sommet_voisin) + ") = " + str(probabilite))
                    if (probabilite > 0) and (probabilite < 1):
                        # Il faut ajouter l'arete selon l'ordre
                        # premiere arete du sommet 1 c'est l'arete qui relie le sommet 1 et le sommet 2
                        liste_adjacence[sommet].append(sommet_voisin)

        return Graphe(liste_adjacence)
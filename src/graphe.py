from collections import defaultdict
import random


class Graphe:

    sommets = {}

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

    def set_nombre_sommet(self):
        pass

    def afficher_graphe(self):
        for key in sorted(list(self.sommets.keys())):
            print(key + str(self.sommets[key].voisins))

    def barabasi_albert_graphe(self, m):
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

    # P: ensemble des sommets candidats pour etre ajoutes a la potentielle clique
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

    def generer_graphe_aleatoire(self):
        arretes = []
        voisins=list()
        nombreMaximal = input('Nombre de sommets maximal : ')
        nombre_sommets_aleatoire = random.randint(0,int(nombreMaximal))
        nombre_d_arrete_maximal = (nombre_sommets_aleatoire*(nombre_sommets_aleatoire-1))/2

        #Ajout des sommets d'une manière aléatoire à notre graphe
        for i in range(nombre_sommets_aleatoire):
            g.sommets[i]=[]

        #Ajout des arretes d'une manière aléatoire à notre graphe
        for sommet_de_depart in range(nombre_sommets_aleatoire):
            for sommet_de_fin in range(nombre_sommets_aleatoire):
                 probabilite_de_liaison_avec_autre_sommet = random.uniform(0, 1.5)
                 #print( str(probabilite_de_liaison_avec_autre_sommet) +" de chance pour lier " + str(sommet_de_depart) +" et "+ str(sommet_de_fin) )
                 if  probabilite_de_liaison_avec_autre_sommet <=1 and probabilite_de_liaison_avec_autre_sommet > 0:
                    if sommet_de_depart not in self.sommets[sommet_de_fin] :
                        self.sommets[sommet_de_fin].append(sommet_de_depart)
                    if sommet_de_fin not in self.sommets[sommet_de_depart]:
                        self.sommets[sommet_de_depart].append(sommet_de_fin)

        print("La liste d'adjsasnce du graphe : " + str(self.sommets))
"""
    def get_sommet(self):
        sommets = []
        for key, value in self.liste_adjacence.items():
            sommets.extend(value)

        return list(dict.fromkeys(sommets))


    def get_arete(self):
        nombre_aretes = self.get_nombre_arete()

        if nombre_aretes == 0:
            return []

        aretes = [[] for j in range(nombre_aretes)]

        liste_adjacence = copy.deepcopy(self.liste_adjacence)
        i = 0

        for noeud, noeuds in liste_adjacence.items():
            for sommet in noeuds:
                aretes[i] = [noeud, sommet]
                liste_adjacence[sommet].remove(noeud)
                i += 1

        return aretes
"""

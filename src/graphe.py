from collections import defaultdict
import random
from sommet import Sommet


class Graphe:

    sommets = {}

    def __init__(self, liste_adjacence: dict = {}):
        self.liste_adjacence = liste_adjacence


    def ajouter_sommet(self, sommet):
        if isinstance(sommet, Sommet) and sommet.nom not in self.sommets:
            self.sommets[sommet.nom] = sommet
            return True
        else:
            return False

    def ajouter_arrete(self, u, v):
        if u in self.sommets and v in self.sommets:
            self.sommets[u].ajouter_voisin(v)
            self.sommets[v].ajouter_voisin(u)
            return True
        else:
            return False

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


    def get_voision(self, sommet):
        pass

    # P: ensemble des sommets candidats pour etre ajoutes a la potentielle clique
    # R: un sous ensemble des sommets de la potentielle clique
    # X: contient des sommets deja traites ou appartenant deja a une clique maximale
    def bron_kerbosch(self, P, R, X):
        if len(P) == 0 and len(X) == 0:
            return R
        for sommet in P:
            # N(s): ensemble de voisin de v
            # P = P inter Voision(sommet)
            # X = X inter Voisin(sommet)
            self.bron_kerbosch(R.append(sommet),self.get_voision(sommet), self.get_voision(sommet))
            P = P.extend(sommet)
            X = X.append(sommet)


    def bron_kerbosch_pivot(self):
        pass

    def generer_graphe_aleatoire(self):
        arretes=[]
        sommets_possibles=['A', 'B', 'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        nombre_de_sommets = input("Nombre de sommets du graphe à générer: ")
        nombre_arretes_maximal = (int(nombre_de_sommets)*(int(nombre_de_sommets)-1))/2

        #Ajout des sommets d'une manière aléatoire à notre graphe
        for i in range(int(nombre_de_sommets)):
            sommet_aleatoire = random.choice(sommets_possibles)
            sommet_a_ajouter = Sommet(sommet_aleatoire)
            self.ajouter_sommet(sommet_a_ajouter)
            sommets_possibles.remove(sommet_aleatoire)

        sommets_choisis = list(self.sommets.keys())

        #Pour chaque sommet de depart, on cherche les voisins aléatoirement
        for sommet_de_depart in  sommets_choisis:

            sommets_fin = []
            sommets_choisis = list(self.sommets.keys())

            nombre_sommets_aleatoire_d_arrives = random.randint(0,int(nombre_arretes_maximal))
            nombre_arretes_maximal=nombre_arretes_maximal-nombre_sommets_aleatoire_d_arrives

            #enlever la redondane des sommets d'arrivés pour chaque sommet de départ
            for i in range(0,nombre_sommets_aleatoire_d_arrives):
                sommet_de_fin = random.choice(sommets_choisis)
                if sommet_de_fin not in sommets_fin:
                    sommets_fin.append(sommet_de_fin)
                else:
                    pass

            #Construction des arretes avec le sommet de début et le sommet d'arrrié
            for sommet_fin in  sommets_fin:
                    sommet_fin = random.choice(sommets_fin)
                    sommets_fin.remove(sommet_fin)
                    ensemble = str(sommet_de_depart)+str(sommet_fin)
                    ensemble = ensemble.upper()
                    arretes.append(ensemble)

            for arrete in arretes:
                self.ajouter_arrete(arrete[:1], arrete[1:])

            sommets_fin = []

        self.afficher_graphe()







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


 def generer_graphe_aleatoire():
        g = Graphe()
        arretes = []
        nombreMaximal = input('Nombre de sommets maximal : ')
        nombre_sommets_aleatoire = random.randint(0,int(nombreMaximal))
        nombre_d_arrete_maximal = (nombre_sommets_aleatoire*(nombre_sommets_aleatoire-1))/2
        nombre_d_arrete = random.randint(0, nombre_d_arrete_maximal)

        #Ajout des sommets d'une manière aléatoire à notre graphe
        for i in range(nombre_sommets_aleatoire):
            sommet_aleatoire = random.choice(['A', 'B', 'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
            if sommet_aleatoire not in g.sommets:
                sommet_a_ajouter = Sommet(sommet_aleatoire)
                g.ajouter_sommet(sommet_a_ajouter)

        #Ajout des arretes d'une manière aléatoire à notre graphe
        for arrete in range(nombre_d_arrete):
            depart = random.randint(1,len(g.sommets.keys())-1)
            liste_des_sommets = list(g.sommets)
            fin = random.randint(1,len(g.sommets.keys())-1)
            ensemble = liste_des_sommets[depart]+liste_des_sommets[fin]
            ensemble = ensemble.upper()
            arretes.append(ensemble)
        for arrete in arretes:
            g.ajouter_arrete(arrete[:1], arrete[1:])

        #supprimer les sommets sans voisins
        for key in sorted(list(g.sommets.keys())):
            if bool(g.sommets[key].voisins) < 1:
                del g.sommets[key]


        print("La liste des sommets: ")
        print(list(g.sommets))
        print("\n")

        print("La liste des arretes: ")
        print(arretes)
        print("\n")

        print("Les listes d'adjacences du graphe:")
        g.afficher_graphe()


print("\n------------------------PARTIE 1.1----------------------------\n")
generer_graphe_aleatoire()

print("------------------------ALBERT BARBASI----------------------------\n")
g=Graphe()
print("La liste d'adjacence:")
print(g.barabasi_albert_graphe(5))
"""

g= Graphe()
g.generer_graphe_aleatoire()


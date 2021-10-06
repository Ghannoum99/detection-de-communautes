import copy
from collections import defaultdict
import random


class Graphe:

    def __init__(self,liste_adjacence: dict = {}):
        self.liste_adjacence = liste_adjacence


    def ajouter_sommet(self):
        pass

    def ajouter_arete(self):
        pass

    def afficher_graphe(self):
        pass

    @staticmethod
    def barabasi_albert_graph(m):
        if m <= 0:
            return Graphe()

        liste_adjacence = defaultdict(list, {0: [1, 2], 1: [0, 2], 2: [0, 1]})

        for j in range(3, 3 + m):
            somme_degrees = sum([len(sommets) for sommets in liste_adjacence.values()])
            noeuds = set(liste_adjacence.keys()) - {j} - set(liste_adjacence[j])

            for noeud in noeuds:
                degree = len(liste_adjacence[noeud])
                probabilite = degree / somme_degrees
                if random.random() < probabilite:
                    liste_adjacence[j].append(noeud)
                    liste_adjacence[noeud].append(j)

        return Grape(liste_adjacence)

    def set_nombre_sommet(self):
        pass

    def get_nombre_sommet(self):
        return len(self.liste_adjacence.keys())

    def get_nombre_arete(self):
        aretes = [len(sommets) for sommets in self.liste_adjacence.values()]
        return int(sum(aretes) / 2)
            sommets.append(key)

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

        return aretes    def generer_graphe_aleatoire():
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
                sommet_a_ajouter = Sommets( sommet_aleatoire )
                g.ajouterSommet(sommet_a_ajouter)

        #Ajout des arretes d'une manière aléatoire à notre graphe
        for arrete in range(nombre_d_arrete):
            depart = random.randint(1,len(g.sommets.keys())-1)
            liste_des_sommets = list(g.sommets)
            fin = random.randint(1,len(g.sommets.keys())-1)
            ensemble = liste_des_sommets[depart]+liste_des_sommets[fin]
            ensemble = ensemble.upper()
            arretes.append(ensemble)
        for arrete in arretes:
            g.ajouterArrete(arrete[:1], arrete[1:])

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
print(g.albert_barbasi(5))




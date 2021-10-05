import random

class Sommets:
	def __init__(self, n):
		self.nom = n
		self.voisins = list()

	def ajouterVoisin(self, v):
		if v not in self.voisins :
			self.voisins .append((v))
			self.voisins .sort()

class Graphe:
	sommets = {}

	def ajouterSommet(self, vertex):
		if isinstance(vertex, Sommets) and vertex.nom not in self.sommets:
			self.sommets[vertex.nom] = vertex
			return True
		else:
			return False

	def ajouterArrete(self, u, v, weight=0):
		if u in self.sommets and v in self.sommets:
			self.sommets[u].ajouterVoisin(v)
			self.sommets[v].ajouterVoisin(u)
			return True
		else:
			return False

	def afficherGraphe(self):
		for key in sorted(list(self.sommets.keys())):
			print(key + str(self.sommets[key].voisins))

def genererGrapheAleatoire():
    g = Graphe()
    arretes = []

    #Pour le moment, on prend 10 comme nombre maximal de sommets dans le graphe
    nombre_sommets_aleatoire = random.randint(5, 10)

    #Ajout des sommets d'une manière aléatoire à notre graphe
    for i in range(nombre_sommets_aleatoire):
        sommet_aleatoire = random.choice(['A', 'B', 'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
        if sommet_aleatoire not in g.sommets:
            sommet_a_ajouter = Sommets( sommet_aleatoire )
            g.ajouterSommet(sommet_a_ajouter)

    print("La liste des sommets: ")
    print(list(g.sommets))
    print("\n")

    nombre_d_arrete_maximal = (nombre_sommets_aleatoire*(nombre_sommets_aleatoire-1))/2
    nombre_d_arrete = random.randint(5, nombre_d_arrete_maximal)

    #Ajout des arretes d'une manière aléatoire à notre graphe
    for arrete in range(nombre_d_arrete):
        depart = random.randint(1,len(g.sommets.keys())-1)
        liste_des_sommets = list(g.sommets)
        fin = random.randint(1,len(g.sommets.keys())-1)
        ensemble = liste_des_sommets[depart]+liste_des_sommets[fin]
        ensemble = ensemble.upper()
        arretes.append(ensemble)

    print("La liste des arretes: ")
    print(arretes)
    print("\n")

    for arrete in arretes:
    	g.ajouterArrete(arrete[:1], arrete[1:])

    print("Les listes d'adjascenes du graphe:")
    g.afficherGraphe()
    print("\n")

genererGrapheAleatoire()
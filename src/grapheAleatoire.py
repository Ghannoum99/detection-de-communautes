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

	def ajouterSommet(self, sommet):
		if isinstance(sommet, Sommets) and sommet.nom not in self.sommets:
			self.sommets[sommet.nom] = sommet
			return True
		else:
			return False

	def ajouterArrete(self, u, v):
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

    print("Les listes d'adjascenes du graphe:")
    g.afficherGraphe()

genererGrapheAleatoire()

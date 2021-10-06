class Sommets:
	def __init__(self, n):
		self.nom = n
		self.voisins = list()

	def ajouter_voisin(self, v):
		if v not in self.voisins :
			self.voisins .append((v))
			self.voisins .sort()
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
        liste_sommets_degenerescence = self.get_degenerescence_graphe()[1]

        for sommet in liste_sommets_degenerescence:
            R.clear()
            R.append(sommet)
            self.bron_kerbosch_avec_pivot(list(set(P).intersection(self.get_voisin(sommet))), R,
                                              list(set(X).intersection(self.get_voisin(sommet))))
            
            P.remove(sommet)
            X.append(sommet)
            
    # Algorithme de dégénérescence d'un graphe
    # Cet algorithme retourne un ordre de dégénérescence des sommets du graphe
    # commençant par le sommet ayant le plus haut degré
    def get_degenerescence_graphe(self):
        L = list()
        D = []
        
        nbrVoisinsMax = max(map(lambda x: len(x), self.liste_adjacence.values()))
        D = [list() for i in range(nbrVoisinsMax+1)]
     
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
            for i in range(nbrVoisinsMax+1): 
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
                            D[ind-1].append(w)
                    print("\nD", D)
             
        print("L", L)
        
        return [k, L]
    
    # PAS FINI Algorithme d'énumération des cliques maximales
    def enumeration_cliquesMax(self):
        k = self.get_degenerescence_graphe()[0]
        liste_degenerescence = self.get_degenerescence_graphe()[1]
        liste_adjacence_degenerescence = []
        
        for sommet in liste_degenerescence: 
            liste_adjacence_degenerescence.append({sommet: self.liste_adjacence.get_voisin(sommet)})
            
        T = []
        
        n = len(self.liste_adjacence.keys())
        
        for j in range(1, n):
            cliquesMaximales = self.version_avec_ordonnancement()
            for clique in cliquesMaximales:
                indexK = T.index(k)
            
        return T
        
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
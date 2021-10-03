#ifndef GENERERUNGRAPHEALEATOIRE_H
#define GENERERUNGRAPHEALEATOIRE_H


typedef struct
{
	int** coeffs;
}t_matrice_adjascence;

typedef struct
{
	int nombre_de_sommets;
	t_matrice_adjascence* matrice_d_adjascence;
}graphe;


t_matrice_adjascence* allouerMatriceAdjascence(int lignes_colonnes);
void desallouerMatriceAdjascence(t_matrice_adjascence** matrice_adjascence, graphe graphe_aleatoire_desaloc);
void saisirValeurs(int** tableau, int ligne_colonne);
void saisirMatrice(t_matrice_adjascence* mat, graphe graphe_aleatoire);
void genererGrapheAleatoire();

#endif

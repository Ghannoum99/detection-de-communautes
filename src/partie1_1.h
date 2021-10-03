#ifndef PARTIE1_1_H
#define PARTIE1_1_H


typedef struct
{
	int nombre_lignes_colonnes;
	int** coeffs;
}t_matrice_adjascence;

typedef struct
{
	int nombre_de_sommets;
	t_matrice_adjascence* matrice_d_adjascence;
}graphe;


t_matrice_adjascence* allouerMatriceAdjascence(int lignes_colonnes);
void desallouerMatriceAdjascence(t_matrice_adjascence** matrice_adjascence);
void saisirValeurs(int** tableau, int ligne_colonne);
void saisirMatrice(t_matrice_adjascence* mat);
void genererGrapheAleatoire();

#endif

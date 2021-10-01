#ifndef PARTIE1_1_H
#define PARTIE1_1_H


typedef struct
{
	int nombre_lignes;
	int nombre_colonnes;
	int** coeffs;
	float** probas;
}t_matrice_adjascence;

float genererUnNombreAleatoire(int max, int min);
t_matrice_adjascence* allouerMatriceAdjascence(int lignes_colonnes);
void desallouerMatriceAdjascence(t_matrice_adjascence** matrice_adjascence);
void saisirValeurs(float** tableauProba, int** tableau, int ligne, int colonne);
void saisirMatrice(t_matrice_adjascence* mat);
void genererGrapheAleatoire();

#endif

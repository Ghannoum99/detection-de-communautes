#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "partie1_1.h"


float genererUnNombreAleatoire(int max, int min){
	
	srand(time(NULL));
	float scale = rand()/(float)RAND_MAX;
	return min + scale * (max-min);
}

t_matrice_adjascence* allouerMatriceAdjascence(int lignes_colonnes)
{
	t_matrice_adjascence* mat = NULL;
	int i = 0,j=0;
	
	mat = (t_matrice_adjascence*)malloc(sizeof(t_matrice_adjascence));
	
	mat->nombre_lignes = lignes_colonnes;
	mat->nombre_colonnes = lignes_colonnes;
	
	mat->coeffs = (int**)malloc(mat->nombre_lignes*sizeof(int*));
	for(i=0; i<mat->nombre_lignes ; i++)
	{
		mat->coeffs[i] = (int*)malloc(mat->nombre_colonnes*sizeof(int));
		for(j=0; j<mat->nombre_colonnes ; j++)
		{
			mat->coeffs[i][j] = -1;
		}
	}
	mat->probas = (float**)malloc(mat->nombre_lignes*sizeof(float*));
	for(i=0; i<mat->nombre_lignes ; i++)
	{
		mat->probas[i] = (float*)malloc(mat->nombre_colonnes*sizeof(float));
		for(j=0; j<mat->nombre_colonnes ; j++)
		{
			mat->probas[i][j] = -1;
		}
	}

	return mat;
}

void desallouerMatriceAdjascence(t_matrice_adjascence** matrice_adjascence)
{
	int i=0;

	for(i=0; i<(*matrice_adjascence)->nombre_lignes ; i++)
	{
		free((*matrice_adjascence)->coeffs[i]);
	}
	free((*matrice_adjascence)->coeffs);
	free(*matrice_adjascence);
	
	*matrice_adjascence = NULL;
}

void saisirValeurs(float** tableauProba, int** tableau, int ligne, int colonne)
{
	int i,j=0;
	int valeur;
	
	srand(time(NULL));
	
	
	printf("Remplissage de la matrice d'adjascence d'une manière aléatoire : lien/probabilité\n");
	for(i=0; i<colonne; i++)
	{
		for(j=0; j<ligne;j++)
		{
			float scale = rand()/(float)RAND_MAX;
			tableau[i][j]=rand()%2;
			float w = 0 + scale * (1-0);
			tableauProba[i][j]=w;
		}
	}
}

void saisirMatrice(t_matrice_adjascence* mat)
{	
	saisirValeurs(mat->probas,mat->coeffs,mat->nombre_lignes, mat->nombre_colonnes);
}


void genererGrapheAleatoire()
{
	int nombre_de_sommets;
	t_matrice_adjascence *matrice = NULL;
	t_matrice_adjascence *matriceProbas = NULL;
	int i,j;
	
	printf("Nombre de sommets: ");
	scanf("%d",&nombre_de_sommets);
	
	matrice = allouerMatriceAdjascence(nombre_de_sommets);
	saisirMatrice(matrice);


	for(i=0; i<nombre_de_sommets; i++)
	{
		for(j=0; j<nombre_de_sommets;j++)
		{
			printf("%d/%f ",matrice->probas[i][j],matrice->coeffs[i][j]);
		}
		printf("\n");
	}
	desallouerMatriceAdjascence(&matrice);
}


int main(void){

	genererGrapheAleatoire();
	
	return 0;
	
}

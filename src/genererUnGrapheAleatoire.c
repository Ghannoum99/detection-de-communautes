#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "genererUnGrapheAleatoire.h"

t_matrice_adjascence* allouerMatriceAdjascence(int nbr_sommets)
{
	t_matrice_adjascence* mat = NULL;
	int i = 0,j=0;
	
	mat = (t_matrice_adjascence*)malloc(sizeof(t_matrice_adjascence));
	
	mat->coeffs = (int**)malloc(nbr_sommets*sizeof(int*));
	for(i=0; i<nbr_sommets; i++)
	{
		mat->coeffs[i] = (int*)malloc(nbr_sommets*sizeof(int));
		for(j=0; j<nbr_sommets ; j++)
		{
			mat->coeffs[i][j] = -1;
		}
	}

	return mat;
}

void desallouerMatriceAdjascence(t_matrice_adjascence** matrice_adjascence, graphe graphe_aleatoire_desaloc)
{
	int i=0;

	for(i=0; i<graphe_aleatoire_desaloc.nombre_de_sommets ; i++)
	{
		free((*matrice_adjascence)->coeffs[i]);
	}
	free((*matrice_adjascence)->coeffs);
	free(*matrice_adjascence);
	
	*matrice_adjascence = NULL;
}

void saisirValeurs(int** tableau, int ligne_colonne)
{
	int i,j=0;
	int valeur;
	
	srand(time(NULL));
	
	
	printf("Remplissage de la matrice d'adjascence d'une manière aléatoire :\n");
	for(i=0; i<ligne_colonne; i++)
	{
		for(j=0; j<ligne_colonne;j++)
		{
			tableau[i][j]=rand()%2;
		}
	}
	for(i=0; i<ligne_colonne; i++)
	{
		for(j=0; j<ligne_colonne;j++)
		{
			if(tableau[i][j] == 1)
			{
				tableau[j][i] = 1;
			}
			else
			{
				tableau[j][i] = 0;
			}
		}
	}
}

void saisirMatrice(t_matrice_adjascence* mat, graphe graphe_aleatoire)
{	
	saisirValeurs(mat->coeffs,graphe_aleatoire.nombre_de_sommets);
}


void genererGrapheAleatoire()
{
	graphe graphe_aleatoire;
	int i,j;
		
	printf("Nombre de sommets: ");
	scanf("%d",&graphe_aleatoire.nombre_de_sommets);
	
	graphe_aleatoire.matrice_d_adjascence = allouerMatriceAdjascence(graphe_aleatoire.nombre_de_sommets);
	saisirMatrice(graphe_aleatoire.matrice_d_adjascence,graphe_aleatoire);

	printf("  ");
	for(i=0; i<graphe_aleatoire.nombre_de_sommets; i++)
	{
			printf("%d ",i);
	}
	printf("\n");
	for(i=0; i<graphe_aleatoire.nombre_de_sommets; i++)
	{
		printf("%d ",i);
		for(j=0; j<graphe_aleatoire.nombre_de_sommets;j++)
		{
			printf("%d ",graphe_aleatoire.matrice_d_adjascence->coeffs[i][j]);
		}
		printf("\n");
	}
	desallouerMatriceAdjascence(&graphe_aleatoire.matrice_d_adjascence,graphe_aleatoire);
}


int main(void){

	genererGrapheAleatoire();
	
	return 0;
	
}

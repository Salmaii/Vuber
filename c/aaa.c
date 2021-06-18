#include <stdio.h>

void troca(int vetor[], int i, int j)
{
	int aux = vetor[i];
	vetor[i] = vetor[j];
	vetor[j] = aux;
}

void permuta(int vetor[], int inf, int sup)
{
    int i;
    int matriz[6][3];
	if(inf == sup)
	{
		for(i = 0; i <= sup; i++)
			printf("%d ", vetor[i]);
            printf("\n");
	}
	else
	{
		for(int i = inf; i <= sup; i++)
		{
			troca(vetor, inf, i);
			permuta(vetor, inf + 1, sup);
			troca(vetor, inf, i); // backtracking
		}
	}
	printf("O vetor i = %d \n", vetor[i]);
}

int main(int argc, char *argv[])
{
    //        a  b  p
    int vetor[3][3];
    int x=0, y=0, z=0;

	int v[] = {1, 2, 3, 4};
	int tam_v = sizeof(v) / sizeof(int);

	permuta(v, 0, tam_v - 1);

        for(x=0;x<6;x++){
        for(y=0;y<3;y++){
        printf("Ponto a: ");
        scanf("%i", &vetor[x][x]);
        printf("\n");

        printf("Ponto b: ");
        scanf("%i", &vetor[x][x+1]);
        printf("\n");


        printf("Peso: ");
        scanf("%i", &vetor[x][x+2]);
        printf("\n");
        }
    }


	return 0;
}
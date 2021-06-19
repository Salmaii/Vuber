#include <stdio.h>

typedef struct
{
	int origem;
	int destino;
	int peso;
} Pesos;

void troca(int vetor[], int i, int j);

void permuta(int vetor[], int inf, int sup);

int pesoTotal(int origem, int destino, int qntd_pesos);

int main(int argc, char *argv[])
{
	int i = 0;
	int qtd = 0;
	int calculaPeso = 0;
	int total = 0;
	Pesos peso[5];

	peso[0].peso = 10;
	peso[0].destino = 1;
	peso[0].origem = 2;

	peso[1].peso = 15;
	peso[1].destino = 2;
	peso[1].origem = 3;
	
	peso[2].peso = 24;
	peso[2].destino = 3;
	peso[2].origem = 4;
	
	//int v[] = {'a', 'b', 'c', 'd'};
	int v[] = {1, 2, 3, 4};
	int tam_v = sizeof(v) / sizeof(int);
	int tam = sizeof(v);

	permuta(v, 0, tam_v - 1);

	for(i = 0; i < tam_v - 1; i++) {
		int aux = pesoTotal(peso[i].origem, peso[i+1].destino, peso[i].peso);
		
		total = total + aux;
		printf("Dentro loop\n");
	}


	printf("Peso Total: %d", total);
	printf("\n");
	return 0;
}

void troca(int vetor[], int i, int j)
{
	int aux = vetor[i];
	vetor[i] = vetor[j];
	vetor[j] = aux;
}

void permuta(int vetor[], int inf, int sup)
{
	if (inf == sup)
	{
		for (int i = 0; i <= sup; i++)
			printf("%d ", vetor[i]);
		printf("\n");
	}
	else
	{
		for (int i = inf; i <= sup; i++)
		{
			troca(vetor, inf, i);
			permuta(vetor, inf + 1, sup);
			troca(vetor, inf, i); // backtracking
		}
	}
}

int pesoTotal(int origem, int destino, int qntd_pesos)
{
	Pesos pesos[qntd_pesos];

	for (int i = 0; i < qntd_pesos; i++)
	{
		if (origem == pesos[i].origem && destino == pesos[i].destino)
		{
			return pesos[i].peso;
		}
	}
	return 0;
}
#include <stdio.h>
#include <stdlib.h>


int main() {
	int N;
	int *S = 0;
	int *E = 0;
	int i;
	int count = 1;

	scanf("%d", &N);
	
	S = (int*)malloc(sizeof(int)*N);
	E = (int*)malloc(sizeof(int)*N);

	for (i = 0; i < N; i++)
	{
		scanf("%d %d", &S[i], &E[i]);
	}
	
	
	for (i = 0; i < N; i++)
	{
		
		if (E[0] <= S[i])
		{
			E[0] = E[i];
			count++;
			
		}
	}
	printf("%d", count);
}
	
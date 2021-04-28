#include<stdio.h>
#include<stdlib.h>

int main()
{
	int N, P[1005];
	int i, j, temp;
	int sum = 0;
	scanf("%d", &N);


	for (i = 0; i < N; i++)
		scanf("%d", &P[i]);

	for (i = 0; i < N; i++)
	{
		for (j = i + 1; j < N; j++)
		{
			if (P[j] < P[i])
			{
				temp = P[i];
				P[i] = P[j];
				P[j] = temp;
			}
		}
	}

	for (i = 0; i < N; i++)
		P[i+1] += P[i];
	
	for (i = 0; i < N; i++)
		sum += P[i];

	printf("%d", sum);
}
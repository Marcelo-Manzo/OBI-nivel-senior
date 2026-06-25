#include <stdio.h>
int main()
{
    int listaA[1000], listaB[1000], intersec[1000], m, n, i, cont = 0, jaEsta;
    scanf("%d", &m);
    for(i = 0; i<m; i++)
    {
        scanf("%d", &listaA[i]);
    }
    scanf("%d", &n);
    for(i = 0; i<n; i++)
    {
        scanf("%d", &listaB[i]);
    }

    for(i = 0; i<m; i++)
    {
        for(int j = 0; j<n; j++)
        {
            if(listaA[i] == listaB[j])
            {
                jaEsta = 0;
                for(int z = 0; z<cont; z++)
                {
                    if(listaA[i] == intersec[z])
                    {
                        jaEsta = 1;
                    }
                }
                if(jaEsta == 0)
                {
                    intersec[cont] = listaA[i];
                    cont++;
                }
            }
        }
    }
    for(i = 0; i<cont; i++)
    {
        printf("%d", intersec[i]);
    }
}
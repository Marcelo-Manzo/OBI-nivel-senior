#include <stdio.h>

int main()
{
    int lista[1000], listaPar[1000], listaImpar[1000], n, i;
    scanf("%d", &n);
    for(i = 0; i< n; i++)
    {
        scanf("%d", &lista[i]);
    }
    int contP = 0;
    int contI = 0;
    for(i = 0; i<n; i++)
    {
        if(lista[i] % 2 == 0)
        {
            listaPar[contP] = lista[i];
            contP++;
        }
        else
        {
            listaImpar[contI] = lista[i];
            contI++;
        }
    }
    for(i = 0; i<contP; i++)
    {
        printf("%d", listaPar[i]);
    }
    printf("\n");
    for(i = 0; i<contI; i++)
    {
        printf("%d", listaImpar[i]);
    }
    return 0;

}
#include<stdio.h>
#include <math.h>
int main()
{
    int lista[1000], listaQ[1000], i, n, cont = 0;
    scanf("%d", &n);
    while(n != -1)
    {
        lista[cont] = n;
        cont++;
        scanf("%d", &n);
    }

    for(i = 0; i<cont; i++)
    {
        listaQ[i] = (int)pow(lista[i],2);
    }
    for(i = 0; i<cont; i++)
    {
        printf(" %d ", listaQ[i]);
    }
    return 0;
}
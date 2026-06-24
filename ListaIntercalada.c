#include <stdio.h>

int main()
{
    int listaA[1000], listaB[1000], listaC[2000];
    int m, n;
    int i = 0, j = 0, k = 0;
    
    // Leitura da Lista A
    scanf("%d", &m);
    for(int idx = 0; idx < m; idx++) {
        scanf("%d", &listaA[idx]);
    }
    
    // Leitura da Lista B
    scanf("%d", &n);
    for(int idx = 0; idx < n; idx++) {
        scanf("%d", &listaB[idx]);
    }
    
    // Intercala começando sempre pela Lista A
    while (i < m && j < n) {
        listaC[k++] = listaA[i++];
        listaC[k++] = listaB[j++];
    }
    
    // Copia o restante da Lista A (se houver)
    while (i < m) {
        listaC[k++] = listaA[i++];
    }
    
    // Copia o restante da Lista B (se houver)
    while (j < n) {
        listaC[k++] = listaB[j++];
    }
    
    // Impressão dos elementos separados por espaço
    for(int idx = 0; idx < k; idx++) {
        printf("%d ", listaC[idx]);
    }
    
    return 0;
}
#include <stdio.h>
int main()
{
    int lista[1000]; nums[10] = {0}, i, n,cont = 0, teve = 0;
    scanf("%d", &n);
    while(n != null)
    {
        lista[cont] = n;
        cont++;
        scanf("%d", &n);
    }
    for(i = 0; i<cont; i++)
    {
        nums[lista[i]]++;
    }
    for(i=0; i<10; i++)
    {
        if(nums[i] % 2 != 0)
        {
            printf(" %d ",i);
            teve = 1;
        }
    }
    if(teve == 0)
    {
        printf("N");
    }
    return 0;
}
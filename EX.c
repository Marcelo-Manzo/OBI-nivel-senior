int main(){
    int matriz[10][10];
    for(int i = 0; i<10; i++)
    {
        for(int j = 0; j<10; j++)
        {
            scanf("%d", &matriz[i][j]);
        }
    }
    for(int i = 0; i<10; i++)
    {
        for(int j = 0; j<10; j++)
        {
            printf("%d",matriz[i][j]);
        }
    }
}
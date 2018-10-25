#include<stdio.h>
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=n; i>=1;i--)
    {
        for(int m=65;m<=i+64;m++)
        {
            printf("%c",m);
        }
        for(int j=0; j<2*(n-i)-1;j++)
        {
            printf(" ");
        }
        for(int o=i+63;o>=65;o--)
        {

            printf("%c",o);


        }
        printf("\n");
    }
}

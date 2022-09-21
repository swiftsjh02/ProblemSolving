#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){

    FILE *fp = fopen("input.txt","r");

    if(fp==NULL){
        printf("no file\n");
        return -1;
    }
    int n=0;
    fscanf(fp,"%d",&n);
        

  

    for(int i=0;i<n;i++){

    char s[10000];
    char t[100];

    fscanf(fp,"%s",s);
    fscanf(fp,"%s",t);
            


    int m = strlen(s);
    int n = strlen(t);
    int **dp = (int **)malloc(sizeof(int *) * (m + 1));
    for(int i = 0; i <= m; i++){
        dp[i] = (int *)malloc(sizeof(int) * (n + 1));
    }
    for(int i = 0; i <= m; i++){
        dp[i][0] = 1;
    }
    for(int i = 1; i <= n; i++){
        dp[0][i] = 0;
    }
    for(int i = 1; i <= m; i++){
        for(int j = 1; j <= n; j++){
            if(s[i - 1] == t[j - 1]){
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
            }else{
                dp[i][j] = dp[i - 1][j];
            }
        }
    }


    for(int i=0; i<m+1; i++){
        for(int j=0; j<n+1; j++){
            printf("%d ",dp[i][j]);
        }
        printf("\n");
    }

    printf("%d\n", dp[m][n]);

    }
    

    

    return 0;
}
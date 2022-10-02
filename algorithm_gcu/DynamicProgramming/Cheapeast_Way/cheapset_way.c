#include <stdio.h>
#include <stdlib.h>


int dodp(int x,int y,int sum,int m,int n, int a[10][100],int dp[10][100]){
    if(x==n){
        return 0;
    }
    
    sum+=a[y][x];

    if(dp[y][x]==0){
        dp[y][x]=sum;
    }
    else{
        if(dp[y][x]>sum){
            dp[y][x]=sum;
        }
    }


    dodp(x+1,y,sum,m,n,a,dp);
    dodp(x+1,(y+1)%m,sum,m,n,a,dp);
    dodp(x+1,y-1,sum,m,n,a,dp);
 
}


int main(){
    FILE *fp=fopen("input.txt","r");
    int m,n;
    while(fscanf(fp,"%d %d",&m,&n)!=EOF){
        int sum=0;
        int x,y=0;
        int a[10][100]={0};
        int dp[10][100]={0};
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                fscanf(fp,"%d",&a[i][j]);
            }
        }

        dodp(x,y,sum,m,n,a,dp);

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                printf("%d ",dp[i][j]);
            }
            printf("\n");
        }

    }


    return 0;
}
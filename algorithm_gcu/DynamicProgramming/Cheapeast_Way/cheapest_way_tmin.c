#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node node;
struct node {
    int record[100];
    int sum;
    int record_idx;
};
int mod(int n, int d) {
    if(n<0){
        return d-1;
    }
    return n%d;
}


int main(){
    FILE *fp=fopen("input.txt","r");
    int m,n;
    while(fscanf(fp,"%d %d",&m,&n)!=EOF){
        int sum=0;
        int x=0;
        int y=0;
        int path[10][100]={0};
        node dp[10][100];
        memset(dp,0,m*n);
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                fscanf(fp,"%d",&path[i][j]);
            }
        }


        for(int i=0; i<m; i++){
            node A;
            A.sum=path[i][n-1];
            A.record_idx=n-1;
            A.record[A.record_idx--]=path[i][n-1];
            dp[i][n-1]=A;
        }

        for(int j=n-2; j>=0; j--){
            for(int i=0; i<m; i++){
                node dforwd=dp[mod(i-1,m)][j+1];
                node forwd=dp[i][j+1];
                node dbackwd=dp[mod(i+1,m)][j+1];

                node *min=&dforwd;
                if(forwd.sum<min->sum){
                    min=&forwd;
                }
                if(dbackwd.sum<min->sum){
                    min=&dbackwd;
                }
                dp[i][j]=*min;
                dp[i][j].sum+=path[i][j];
                dp[i][j].record[dp[i][j].record_idx--]=path[i][j];
            }
        }
        node *ans=&dp[0][0];
        int min_ans=dp[0][0].sum;
        for(int i=1; i<m; i++){
            if(dp[i][0].sum<min_ans){
                min_ans=dp[i][0].sum;
                ans=&dp[i][0];
            }
        }
        


        for(int i=0; i<n; i++){
            printf("%d ",ans->record[i]);
        }
        printf("\n%d\n",ans->sum);

    }

    return 0;
}






    
  



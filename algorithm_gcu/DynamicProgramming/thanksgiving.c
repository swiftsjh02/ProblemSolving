#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
        
        
    while (1){
        int n;
        double sum=0;
        double student[1001];
        double avg=0;
        double ans1,ans2=0;
        scanf("%d",&n);
        if(n==0){
            break;
        }
        for(int i=0;i<n;i++){
            scanf("%lf",&student[i]);
            sum+=student[i];
        }
        avg=round(sum/n*100)/100;

        for(int i=0; i<n; i++){
            if(student[i]>avg){
                ans1+=student[i]-avg;
            }
            else{
                ans2+=avg-student[i];
            }
        }

        if(ans1<ans2){
            printf("$%.2lf\n",ans1);
            continue;
        }
        else{
            printf("$%.2lf\n",ans2);
            continue;
        }
        
        
    }
}


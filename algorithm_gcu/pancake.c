#include <stdio.h>
#include <string.h>
#include <stdlib.h>




void flip(int arr[], int i)
{
    int temp, start = 0;
    while (start < i)
    {
        temp = arr[start];
        arr[start] = arr[i];
        arr[i] = temp;
        start++;
        i--;
    }
}

int findmax(int arr[],int n){
    int max=0;
    for(int i=n; i>1; i--){
        if (arr[i]>arr[max]){
            max=i;
        }
    }
    return max;
}

void pancake(int arr[],int n){
    
    for (int i=n; i>1; i--){
        int max=findmax(arr,i);
        if (max!=i-1){
            flip(arr,max);
            flip(arr,i-1);
            
            
            
        }
    }
    
}


int main(){
    
    FILE *fp = fopen("test.txt","r");

    if(fp==NULL){
        printf("no file\n");
        return -1;
    }
    char line[255];
    int tmp[255];
    while(fgets(line,sizeof(line),fp)!=NULL){
        printf("%s",line);
        int numofcake=0;
        char *ptr = strtok(line," ");
        while(ptr!=NULL){
            tmp[numofcake]=atoi(ptr);
            ptr=strtok(NULL," ");
            numofcake++;
        }

        pancake(tmp,numofcake);
      

    }

    fclose(fp);

}



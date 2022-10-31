#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

char * decrypt(char *str,int strlen,int n,int d){
    char *decstr=(char*)malloc(sizeof(char)*strlen);
    printf("printing dec:\n");
    for(int i=0; i<strlen; i++){
        int temp=str[i];
        decstr[i]=(int)pow(temp,d)%n;
        printf("%c",decstr[i]);
    }
    printf("\n");

    return decstr;
}

char * incrypt(char *str,int strlen,int n,int e){
    printf("printing inc:\n");
    char *encstr=(char*)malloc(sizeof(char)*strlen);
    for(int i=0; i<strlen; i++){
        int temp=str[i];
        encstr[i]=(int)pow(temp,e)%n;
        printf("%c",encstr[i]);
    }
    printf("\n");
    return encstr;
}


int main(){
    int p=11;
    int q=37;
    int e,n;
    int d=103;
    char c[1000];
    printf("Enter E:");
    scanf("%d",&e);
    e=7;
    printf("\n");
    printf("Enter N:");
    scanf("%d",&n);
    printf("\n");
    printf("Enter the message:");
    scanf("%s",c);
    printf("\n");
    int s_len=strlen(c);

    char *inc=incrypt(c,s_len,n,e);
    
    char *dec=decrypt(inc,s_len,n,d);


    return 0;
}
#include<stdio.h>
#
struct pq{ //struct for storage p and q
  int p;
  int q;
};

long decryption(long c,long d,long n){ //decrypt function use private key (d,n)
  double l=1;
  double result=1;
	for(int loop=0;loop < d ; loop++){
		result=(result*((double)c));
		l=(long)(result/n);
		result=result-(l*n);
	}
	return (long)result;
}

struct pq factorization(int n){ //find p and q and return
  struct pq ans;
    while(1){
        if(n<2) return ans;
        int p=2;
        int pri[20];
        int idx=0;
        int i;
 
        while(n!=1){
            if(n%p==0){
                n=n/p;
                pri[idx]=p;
                idx+=1;
                p=2;
            }
            else{
                p+=1;
            }
        }
 
        if(idx==1) return ans;
        else{
            for(i=0; i<idx-1; i++){
                ans.p=pri[i];
            }  
          ans.q=pri[i];
        }
    }
  return ans;
}

int EEA(int a, int b) {
	int s1=1,s2=0;
	int remain, s,quo;
	while (b!=0) {
		quo=a/b;
		remain=a%b;
		a=b; 
        b = remain;
		s=s1 - quo * s2;
		s1=s2;
    s2=s;	
	}
	s=s1;
	return s;
}

int main(){
  int c;
  int e;
  int p;
  int q;
  int n;
  printf("enter e:");
  scanf("%d",&e);
  printf("enter n:");
  scanf("%d",&n);
  printf("enter c:");
	scanf("%d",&c);
  struct pq ans=factorization(n);
  int d=EEA(e,(ans.p-1)*(ans.q-1));
	printf("result:%ld\n",decryption(c,d,n));
	return 0;
}
#include<stdio.h>

struct pq{ //struct for storage p and q
  long long p;
  long long q;
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
        long long p=2;
        long long pri[20];
        long long idx=0;
        long long i;
 
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

long long EEA(long long a, long long b) {
	long long s1=1,s2=0;
	long long remain, s,quo;
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
  int e;
  int p;
  int q;
  int n;
  int loop;
  scanf("%d",&loop);
  for(int i=0; i<loop; i++){
  
  scanf("%d %d",&n,&e);
  struct pq ans=factorization(n);
  int d=EEA(e,(ans.p-1)*(ans.q-1));
  printf("%d\n",d);
  }
 
	return 0;
}
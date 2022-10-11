#include<stdio.h>
#include<stdlib.h>

void swap(int *a, int *b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

int main(){
	FILE *fp=fopen("input.txt","r");
	if(fp==NULL){
		printf("File not found");
		return 0;
	}

	int t;
	fscanf(fp,"%d",&t);
	
	while (t--){
		int T[1000];
		int FINE[1000];
		int n;
		int *ans;
		int day = 0;
		fscanf(fp,"%d", &n);
		ans=malloc(sizeof(int)*n);
		for (int i = 0; i < n; i++)
			fscanf(fp,"%d%d", T + i, FINE + i), ans[i] = i;
		for (int i = 0; i < n; i++){
			for (int j = 0; j < n - 1; j++){
				if (T[ans[j]] * FINE[ans[j + 1]] > FINE[ans[j]] * T[ans[j + 1]])
					swap(ans+j, ans+j + 1);
				else if (T[ans[j]] * FINE[ans[j + 1]] == FINE[ans[j]] * T[ans[j + 1]] && ans[j] > ans[j + 1])
					swap(ans+j, ans+j + 1);
			}
		}
		printf("%d", ans[0] + 1);
		for (int i = 1; i < n; i++)
			printf(" %d", ans[i] + 1);
		putchar('\n');
		if (t != 0)
			putchar('\n');
	}
	return 0;
}
#include <stdio.h>

int main() {
    int a = 3;
    int b = 4; 
    int m, M, r;
    int i = 0;
    //printf("Digite os valores de a e b: ");
    //scanf("%d %d", &a, &b);
    if (a<b){
        m = a;
        M = r = b;
    }
    else{
        m = b;
        M = r = a;
    }
    while(i<m-1){
        r = r + M;
        i = i + 1;
    }
    printf("O resultado é: %d", r);
    return 0;
}
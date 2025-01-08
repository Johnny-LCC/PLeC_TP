#include <stdio.h>

int main() {
    int a = 3;
    int b = 4; 
    int m, M, r;
    int i = 0;
    if (a<b){
        m = a;
        M = b;
        r = b;
    }
    else{
        m = b;
        M = a;
        r = a;
    }
    while(i<m-1){
        r = r + M;
        i = i + 1;
    }
    printf("O resultado é: %d", r);
    return 0;
}
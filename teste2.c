#include <stdio.h>

int f(){
    return 3;
}

int main(){
    int a, b;
    printf("Val: ");
    scanf("%d", &a);
    b = f();
    if (a>b){
        b = a*b;
    }
    printf("A:%d B:%d\n", a, b);
    return 0;
}
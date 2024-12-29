#include <stdio.h>

int main(){
    int a = 5;
    int b = 6;
    int c = a - b; //Subtracao
    if (c != b && a >= b){
        printf("%d", c);
    }
    else{
        printf("%d %d", a, b);
    }
    return 0;
}
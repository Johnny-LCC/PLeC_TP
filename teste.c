#include <stdio.h>

int main(){
    a = 5;
    b = 6;
    c = a - b; //Subtracao
    if (c != b && a >= b){
        printf("%d", c);
    }
    else{
        printf("%d %d", a, b);
    }
    return 0;
}
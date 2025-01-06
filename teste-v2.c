#include <stdio.h>

int main(){
    int a,b,c;
    a = 5; b= 6; 
    c = a - b; 
    if (c != b || a >= b){ 
        printf("c"); 
    } 
    else{ 
        printf("a b"); 
    } 
    return 0; 
}
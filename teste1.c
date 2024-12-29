#include <stdio.h>

int func(int a, int b, int x, int y) {
    
    if (a == 0) {
        x = 0;
        y = 1;
        return b;
    }

    int x1, y1; 
    int gcd = func(b % a, a, &x1, &y1);
    
    x = y1 - (b / a) * x1;
    y = x1;
    return gcd;
}

int main() {
    int a, b;
    printf("Digite os valores de a e b: ");
    scanf("%d %d", &a, &b);
    int x, y;
    int gcd = func(a, b, &x, &y);
    printf("GCD(%d, %d) = %d\n", a, b, gcd);
    printf("Coeficientes: x = %d, y = %d\n", x, y);
    return 0;
}

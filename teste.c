#include <stdio.h>

int main(){
    int a = 5; //PUSHI 5
    int b = 6; //PUSHI 6
    int c = a - b; // PUSHI 0, START, PUSHG 0, PUSHG 1, SUB, STOREG 2
    if (c != b && a >= b){ // PUSHG 2, PUSHG 1, EQUAL, PUSHG 0, PUSHG 1, SUPEQ, AND, JZ Else
        printf("%d", c); // PUSHS "C", WRITES
    } // JUMP Fim
    else{ //Else: NOP
        printf("%d %d", a, b); // PUSHS "A B", WRITES
    } // Fim: NOP
    return 0; // STOP
}

/*
PUSHI 5
PUSHI 6
PUSHI 0
START
PUSHG 0
PUSHG 1
SUB
STOREG 2
PUSHG 2
PUSHG 1
EQUAL
PUSHG 0
PUSHG 1
SUPEQ
AND
JZ Else
PUSHS "C" //PUSHG 2 \n STRI
WRITES
JUMP Fim
Else: NOP
PUSHS "A B"
WRITES
Fim: NOP
STOP
*/

// ATOI -> READ
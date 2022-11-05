#include <stdio.h>
#include <stdlib.h>

int main()
{
    int vct[] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,8,19,20,21};
    int * pVct = &vct[5];
    pVct = (int *) malloc(10 * sizeof(int));
    pVct = (int *) realloc(pVct, 21 * sizeof(int));
    printf("\n%p", sizeof(pVct));

    free(pVct);

    return 0;
}
//

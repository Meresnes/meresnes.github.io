#include <stdio.h>
#include <stdlib.h>
/*Сортировка прямым обменом*/
#define n 10
int main(int argc, char const *argv[])
{
    int a[n];
    srand(time(NULL));
    /*Заполнение массива случайными значениями*/
    printf("Array A: ");
    for (int i = 0; i < n; i++)
    {
        a[i] = rand() % 20;
        printf("%d ", a[i]);
    }
    /*Сортировка*/
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = n - 1; j > i; j--)
        {
            if (a[j - 1] > a[j])
            {
            int k = a[j - 1];
            a[j - 1] = a[j];
            a[j] = k;
            }
        }
    }
    printf("\nSorted array: ");
    for (int i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }
    printf("\nMax = %d",a[n-1]);

    return 0;
}

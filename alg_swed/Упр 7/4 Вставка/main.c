#include <stdio.h>
#include <stdlib.h>
#include <time.h>
/*Количество элементов в массиве*/
#define n 11


/*Быстрая сортировка*/


int main(int argc, char const *argv[]) {
  int a[n], i,x,j;
  srand(time(NULL));
  /*Заполнение массива случайными числами*/
  printf("Array a: ");
  for (i = 0; i < n; i++) {
    a[i] = rand() % 20;
    printf("%d ", a[i]);
  }
  for(i = 1 ;i < n;i++)
  {
      x = a[i];
      j = i;
      while(j > 0 && a[j-1] > x){
        a[j]=a[j-1];
        j--;

      }
    a[j]=x;
  }
  printf("\nSorted array: ");
  for (i = 0; i < n; i++)
  {
    printf("%d ", a[i]);
  }
  if (n % 2 == 0)
    printf("\nCant be posible to count median\n");
  else
    printf("\nMedian of array: %d\n", a[n / 2]);
  return 0;
}

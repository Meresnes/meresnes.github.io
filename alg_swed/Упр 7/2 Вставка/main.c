#include <stdio.h>
#include <stdlib.h>
/*Сортировка вставками*/
#define n 10
int main(int argc, char const *argv[])
{
  int a[n], i,x,j;
  srand(time(NULL));
 /*Заполнение массива случайными значениями*/
  printf("Array A: ");
  for (i = 0; i < n; i++)
  {
    a[i] = rand() % 20+1;
    printf("%d ", a[i]);
  }
  /*Сортировка*/
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
  printf("\nmin = %d , almostmin = %d",a[0],a[1]);
    return 0;
}

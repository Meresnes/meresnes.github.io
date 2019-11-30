#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define n 10

int main(int argc, char const *argv[])
{
  int a[n], i;
  srand(time(NULL));
  /*Заполнение массива случайными числами*/
  for (i = 0; i < n; i++)
  {
    a[i] = rand() % 10;
    printf("%d ", a[i]);
  }

  int min = a[0], max = a[0];
  /*Проходим по массиву, сравнивая max и min c элементами массива*/
  for (i = 1; i < n; i++)
  {
    if (a[i] > max)
      max = a[i];
    if (a[i] < min)
      min = a[i];
  }
  printf("\n%d - Min element\n%d - Max element\n", min, max);
  return 0;
}

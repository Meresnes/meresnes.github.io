#include <stdio.h>
#include <stdlib.h>
#include <time.h>
/*Количество элементов в массиве*/
#define n 10
/*Граница интервала в котором берутся случайные числа */
#define k 20


int main(int argc, char const *argv[]) {
  int array[n], i;
  srand(time(NULL));
  //Заполнение массива случайными числами
  printf("Массив A = ");
  for (i = 0; i < n; i++) {
    array[i] = rand() % k;
    printf("%d ", array[i]);
  }
  //min - минимальный элемент
  int min = array[0];
  for (i = 1; i < n; i++)
    if (array[i] < min)
      min = array[i];
  //almostmin - ближайший к минимальному элемент
  int almostmin = min + k;
  for (i = 1; i < n; i++)
    if (array[i] < almostmin && array[i] != min)
      almostmin = array[i];
  printf("\n\n%d - минимальный элемент\n%d -ближайший к минимальному элемент\n",
         min, almostmin);
  return 0;
}

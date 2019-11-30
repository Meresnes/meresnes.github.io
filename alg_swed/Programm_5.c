#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//Количество элементов в массиве (Константа)
#define n 10
//Граница интервала в котором берутся случайные числа (Константа)
#define k 25
int main(int argc, char const *argv[]) {

int a[n],i;
srand(time(NULL));
for (i = 0; i < n; i++) {
    a[i] = rand() % k;
    printf("%d ", a[i]);
  }

//min - минимальный элемент
int min = a[0];

for (i = 1; i < n; i++)
    if (a[i] < min)
        min = a[i];
//ближайший к минимальному элемент
int closest = min + k;

for (i = 1; i < n; i++)
    if (a[i] < closest && a[i] != min)
      closest = a[i];
  printf("\n\n%d - minimal element\n%d - closest to minimal element\n",min, closest);
  return 0;
}

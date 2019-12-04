#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//кол-во элементов в массиве
#define n 10
//граница интервала из списка чисел
#define k 20
//сортировка прямым обменом (пузырьком)
void bubble(int *array ,int len){
    for(int i = 0;i < len - 1; i++){
        for(int j = 0; j < len - 1; j++){
            if (array[j] > array[j + 1]){
                int b = array[j];
                array[j] = array[j + 1];
                array[j + 1] = b;
            }
        }
    }
}
int main(int argc, char const *argv[]){
  int array[n], i;
  srand(time(NULL));
  //Заполнение массива случайными числами
  printf("Массив А:\n");
  for (i = 0; i < n; i++) {
    array[i] = rand() % k - k / 2;
    printf("%d ", array[i]);
  }
  //сортировка массива
  bubble(array,n);
  //вывод значений
  printf("\n\nОтсортированный массив:\n");
  for (i = 0; i < n; i++){
    printf("%d ", array[i]);
  }
  printf("\n\nБлижайший к минимальному: %d\n", array[1]);

  return 0;


}
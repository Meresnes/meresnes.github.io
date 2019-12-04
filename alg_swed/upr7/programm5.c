#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//кол-во элементов в массиве
#define n 10
//граница интервала из списка чисел
#define k 20
//сортировка вставками
void insert_sort(int *array,int len){
    for(int i = 1; i < len; i++){
        int z = i;
        while((z > 0) && (array[z-1] > array[z])){
            int b = array[z-1];
            array[z-1] = array[z];
            array[z] = b;
            z = z - 1;
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
  insert_sort(array,n);
  //вывод значений
  printf("\n\nОтсортированный массив:\n");
  for (i = 0; i < n; i++){
    printf("%d ", array[i]);
  }
  printf("\n\nМедианна массива: %d\n", array[n/2]);
  scanf("%d",&i);
  return 0;


}
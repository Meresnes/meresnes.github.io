#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//кол-во элементов в массиве
#define n 10
//граница интервала из списка чисел
#define k 10
//быстрая сортировка
void quickSort(int *array,int left,int right){
  int pivot; 
  int l_hold = left;
  int r_hold = right; 
  pivot = array[left];

  while(left < right){
    while((pivot <= array[right]) && (left< right))
        right--;
    if (left != right){
        array[left] = array[right];
        left++;
    }
    while ((array[left] <= pivot) && (left < right))
      left++;
    if (left != right){
      array[right] = array[left];
      right--;
    }
  }
  array[left] = pivot;
  pivot = left;
  left = l_hold;
  right = r_hold;
  if (left < pivot)
    quickSort(array, left, pivot - 1);
  if (right > pivot)
    quickSort(array, pivot + 1, right);
}

int main(int argc, char const *argv[]){
  int array[n], i, index[n];
  srand(time(NULL));
  //Заполнение массива случайными числами
  printf("Массив А:\n");
  for (i = 0; i < n; i++) {
    array[i] = rand() % k ;
    printf("%d ", array[i]);
    index[i] = 0;
  }
  //сортировка массива
  quickSort(array,0,n-1);
  //вывод значений
  printf("\n\nОтсортированный массив:\n");
  for (i = 0; i < n; i++){
    printf("%d ", array[i]);
  }

  //Количество повторений записывается в массив index
  int t = 1;
  for (i = 0; i < n; i++) {
    if (array[i] == array[i + 1])
      t += 1;
    else {
      index[i] = t;
      t = 1;
    }
  }
  /*Вывод количества повторений*/
  int max_index = index[0];
  for (i = 0; i < n; i++) {
    if (index[i] > 1)
      printf("\nЧисло %d повторяется в массиве %d разa\n", array[i], index[i]);
    if (max_index < index[i])
      max_index = index[i];
  }
  if (max_index == 1)
    printf("\nВ массиве нет повторяющихся элементов\n");

  scanf("%d",&i);
  return 0;
}
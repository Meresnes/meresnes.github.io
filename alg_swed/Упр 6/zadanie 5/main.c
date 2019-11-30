#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define n 10

int main(int argc, char const *argv[])
{
  int a[n], i;
  srand(time(NULL));
  /*���������� ������� ���������� �������*/
  for (i = 0; i < n; i++)
  {
    a[i] = rand() % 10;
    printf("%d ", a[i]);
  }
  /*�������������� ������� ������������ �������� - ������ ������� �������*/
  int min = a[0], almostmin = a[1];
  /*�������� �� �������, ��������� max � min c ���������� �������*/
  for (i = 0; i < n; i++)
  {
    if (a[i] < almostmin && a[i] < min)
    {
      almostmin = min;
      min = a[i];
    } else if (a[i] > min && a[i] < almostmin)
    {
      almostmin = a[i];
    }
  }
  printf("\nmin = %d  , almost min = %d  \n", min, almostmin);
  return 0;
}

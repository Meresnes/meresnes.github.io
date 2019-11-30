   /* ���������� ������஢���� �����㦥���  � � � � � - */
   /* � � � � � � �  �।��� �㭪樨 y=f(x)  �� x, ���- */
   /* ��饬�� � ����筮� �।��쭮� �窥.                */
   /*                                                     */
   /* ����: �.�.���檨� (18.04.2013)                     */
   /* --------------------------------------------------- */
   #include<stdio.h>
   #include<math.h>
   #include<conio.h>
      double f (double);
   /* --------------- */
   int main()
   {
      double x0,x1,
             delta=0.1,
             M=10000;
      /* ------------------------------------------------- */
      printf("������ �।����� ���: "); scanf("%lg",&x0);
      x1=x0-delta;
      while (fabs(f(x1))<M)
      {
        delta=delta/2; x1=x0-delta;
        printf("(%7g,%7g)\n",x1,f(x1));
      }
      printf("�������: %g\n",f(x1));
      getch();
      return 0;
   }
   /* ------------- */
   double f (double x)
   {
      return (x-1.0)/(x*x-2.0*x+1.1);
   }

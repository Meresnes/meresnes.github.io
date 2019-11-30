   -- ���������� �������஢���� ��⥭樠�쭮 ��᪮�����
   -- ᯨ᪮� �� ४��७⭮�� ᮮ⭮襭�� ��ண� ���浪�
   -------------------------------------------------------

   -- *****************************************
   -- �㭪�� �����頥� ��⮪ �� ४��७⭮�� 
   -- ᮮ⭮襭�� ��ண� ���浪�
   --
   --  f(x )=f0, f(x )=f1, f(x )=2*x   -x
   --     0         1         n     n-1  n-2
   --
   -------------------------------
   f1 x0 x1 = x0 : f1 x1 (2*x1-x0)

   -- *****************************************
   -- �㭪�� �����頥� ��⮪ �� ४��७⭮��
   -- ᮮ⭮襭�� ��ண� ���浪�
   --
   --  f(x )=f0, f(x )=f1, f(x )=x   ^2 -x   ^2
   --     0         1         n   n-1     n-2
   --
   -----------------------------------
   f2 x0 x1 = x0 : f2 x1 (x1^2 - x0^2)

   -- **********************************
   -- ��� ��ਠ�� ॠ����樨 ���᫥���
   -----------------------------------------------
   f3 x0 x1 k = x0 : f3 x1 (x1^2 - x0 + k^2) (k+1)
   -----------------------------------------------
   f31 n | n==0 = 1 
         | n==1 = 2
         | True = (f31 (n-1))^2 - f31 (n-2) + n^2

   ----------------
   f7 n | n==0 = -1 
        | n==1 =  1
        | True = f7 (n-1) `div` f7 (n-2)

   test7 = map f7 [0..12]

   ----------------
   f8 n | n==0 = -1 
        | n==1 =  1
        | True = f7 (n-1) `div` f7 (n-2)

   test8 = map f8 [0..12]

   -- ***************************
   -- ��㤠�� ��⮢� �ਬ���:
   ------------------------------
   test1 = take 12 (f1 1 3)
   test2 = take 12 (f2 0 1)
   test3 = take 12 (f3 1 2 2) == take 12 (map f31 [0..])

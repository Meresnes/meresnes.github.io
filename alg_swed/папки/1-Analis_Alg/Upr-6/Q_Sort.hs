   -- ���������� ॠ����樨  ����ன  ���஢��
   -- ������⮢ �����஢������ ᯨ᪠ (�� �.�����)
   -- ********************************************
   import List

   -------------------------------
   quickSort:: Ord a => [a] -> [a]
   quickSort []     = [] 
   quickSort (x:xs) =   quickSort [y | y <- xs, y<x]
                     ++ [x]
                     ++ quickSort [y | y <- xs, y>=x]

   -- ***************************
   -- ��㤠�� ��⮢� �ਬ���:
   --------------------------------------------------
   test1 =   quickSort (reverse [1..400]) == [1..400]
          && quickSort [6,5,4,3,2,1]      == [1,2,3,4,5,6]
          && quickSort [6,2,4,4,2,6]      == [2,2,4,4,6,6]
          && quickSort [1,2,3,4,5,6]      == [1,2,3,4,5,6]
          && quickSort [0]                == [0]
   --------------------------------------------- 
   test2 = quickSort (map (\x -> sin x) [1..10])
   test3 = quickSort [500,499..1]
   test4 = sort      [500,499..1]

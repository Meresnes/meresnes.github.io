   { ��� ���ᨢ �[1..20], �������� ���ண� �⫨�� �� 0. }
   { ��ᯮ�����  ��  � ⠪�� ���浪�, �⮡� ���묨 �뫨 }
   { �� ������⥫��, �  ��⥬  ����⥫�� ��������; }
   { ���� ���冷� ᫥�������  ���  ������⥫���, ⠪ � }
   { ����⥫��� ������⮢ ������ ��࠭�����.          }
   { �ᯮ�짮���� ���� ���ᨢ �� ࠧ�蠥���.            }
   { ---------------------------------------------------- }
   {                 ���᭥��� � �襭��                  }
   { �ࠢ������ �������� �� ���.                          }
   { �᫨ ��� ������� ������⥫��  ��� ���� �������- }
   { ���, � ��ன ����⥫��, � ����  ᫥������  ���� }
   { (2-�� � 3-� ��������) � �த������ �ࠢ�����.        }
   { �᫨ �� ���� ������� ����⥫��, � ��ன - ����- }
   { ��⥫��, � ���塞 �� ���⠬�  �  �����  �ࠢ������, }
   { ��稭�� � ��ࢮ�� �������.                          }
   { �⠪, �� �ᯮ����  ������ ���ᨢ�, ��  �ᯮ������  }
   { �������� � �ॡ㥬�� ���浪�.                        }
   {                                                      }
   { �����: ����ᮢ� �.�., ���᪨� �.�. (1990)           }
   { ---------------------------------------------------- }
   PROGRAM Primer_4;
      Uses CRT;
      const P=8;
        var a      : Array [1..p] of Integer;
            b      : Boolean;
            i,j,t,y: Integer;
   BEGIN
      Write('������ ���ᨢ (8 ������⮢): ');
      For i:=1 to P do Read(a[i]);
      b:=TRUE; t:=P;
      While b=TRUE do
        begin
          b:=FALSE;
          For j:=1 to t-1 do
            If (a[j]<0) AND (a[j+1]>0)
              then begin
                     y:=a[j]; a[j]:=a[j+1]; a[j+1]:=y;
                     b:=TRUE; t:=j
                   end
        end;
      WriteLn;
      For i:=1 to P do
        Write(a[i],' ');
      WriteLn;
      ReadKey
   END.
   -------------------------------------------
   ����஢���� �஢���� ��� ⠡���� �[1..20]:

   1 2 3 -7 -8 -9 56  4 6 57 89  7  4 -9 -7 -5 -43  -5 -7  8
   1 2 3 56  4  6 57 89 7  4  8 -7 -8 -9 -9 -7  -5 -43 -5 -7

   -1 -2 -3 -4 -5 -6 -7 -8 -9 10 -11 -12 -13 -14 -15 -16 -17 -18
   10 -1 -2 -3 -4 -5 -6 -7 -8 -9 -11 -12 -13 -14 -15 -16 -17 -18
   -19 -20
   -19 -20

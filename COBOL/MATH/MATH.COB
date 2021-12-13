       IDENTIFICATION DIVISION.
           PROGRAM-ID. MATH.
           AUTHOR. NICOLO` MAFFI.
           INSTALLATION. 12/12/2021.
           DATE-WRITTEN. 12/12/2021.
           DATE-COMPILED. 12/12/2021.
           SECURITY. DON`T KNOW.
       DATA DIVISION.
           WORKING-STORAGE SECTION.
               77 NUM1 PIC S9(4)V9(3).
               77 NUM2 PIC S9(4)V9(3).
               77 RIS  PIC S9(8)V9(3). 
       PROCEDURE DIVISION.
           DISPLAY "FIRST OPERATOR: " WITH NO ADVANCING
           ACCEPT NUM1

           DISPLAY "SECOND OPERATOR: " WITH NO ADVANCING
           ACCEPT NUM2

           ADD NUM2 TO NUM1 GIVING RIS
           DISPLAY NUM1 " + " NUM2 " = " RIS

           SUBTRACT NUM2 FROM NUM1 GIVING RIS
           DISPLAY NUM1 " - " NUM2 " = " RIS

           MULTIPLY NUM1 BY NUM2 GIVING RIS
           DISPLAY NUM1 " * " NUM2 " = " RIS

           IF NUM2 IS EQUALS TO ZERO THEN
               DISPLAY "ERROR: DIVISION BY ZERO!"
           ELSE
               DIVIDE NUM2 INTO NUM1 GIVING RIS
               DISPLAY NUM1 " / " NUM2 " = " RIS
           END-IF
       STOP RUN.

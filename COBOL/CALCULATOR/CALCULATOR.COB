       IDENTIFICATION DIVISION.
       PROGRAM-ID. CALCULATOR.
       AUTHOR. NICOLO' MAFFI.
       INSTALLATION. WINDOWS SUBSYSTEM FOR LINUX.
       DATE-WRITTEN. 17/12/2021.
       DATE-COMPILED. 17/12/2021.
       SECURITY. CONFIDENTIAL.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
           77 NUM1 PIC S9(4)V9(2).
           77 NUM2 PIC S9(4)V9(2).
           77 RES  PIC S9(8)V9(2).
           77 Q    PIC S9(4).
           77 R    PIC S9(4).
           77 CMD  PIC X(4).
       PROCEDURE DIVISION.
           MAIN-PROCEDURE.
               DISPLAY "ENTER THE OPERATION: " WITH NO ADVANCING
               ACCEPT CMD

               IF CMD IS EQUALS TO "+" THEN
                   DISPLAY "ENTER NUMBER 1: " WITH NO ADVANCING
                   ACCEPT NUM1

                   DISPLAY "ENTER NUMBER 2: " WITH NO ADVANCING
                   ACCEPT NUM2

                   COMPUTE RES = NUM1 + NUM2
                   DISPLAY "RESULT: " RES

                   GO TO MAIN-PROCEDURE
               END-IF

               IF CMD IS EQUALS TO "-" THEN
                   DISPLAY "ENTER NUMBER 1: " WITH NO ADVANCING
                   ACCEPT NUM1

                   DISPLAY "ENTER NUMBER 2: " WITH NO ADVANCING
                   ACCEPT NUM2

                   COMPUTE RES = NUM1 - NUM2
                   DISPLAY "RESULT: " RES

                   GO TO MAIN-PROCEDURE
               END-IF

               IF CMD IS EQUALS TO "*" THEN
                   DISPLAY "ENTER NUMBER 1: " WITH NO ADVANCING
                   ACCEPT NUM1

                   DISPLAY "ENTER NUMBER 2: " WITH NO ADVANCING
                   ACCEPT NUM2

                   COMPUTE RES = NUM1 * NUM2
                   DISPLAY "RESULT: " RES

                   GO TO MAIN-PROCEDURE
               END-IF

               IF CMD IS EQUALS TO "/" THEN
                   DISPLAY "ENTER NUMBER 1: " WITH NO ADVANCING
                   ACCEPT NUM1

                   DISPLAY "ENTER NUMBER 2: " WITH NO ADVANCING
                   ACCEPT NUM2

                   IF NUM2 IS EQUALS TO ZEROS THEN
                       DISPLAY "ERROR: DIVISION BY ZERO."
                   ELSE
                       COMPUTE RES = NUM1 / NUM2
                       DISPLAY "RESULT: " RES
                   END-IF

                   GO TO MAIN-PROCEDURE
               END-IF

               IF CMD IS EQUALS TO "MOD" THEN
                   DISPLAY "ENTER NUMBER 1: " WITH NO ADVANCING
                   ACCEPT NUM1

                   DISPLAY "ENTER NUMBER 2: " WITH NO ADVANCING
                   ACCEPT NUM2

                   DIVIDE NUM2 INTO NUM1 GIVING Q REMAINDER R
                   DISPLAY "RESULT: " R

                   GO TO MAIN-PROCEDURE
               END-IF

               IF CMD IS EQUALS TO "POW" THEN
                   DISPLAY "ENTER BASE: " WITH NO ADVANCING
                   ACCEPT NUM1

                   DISPLAY "ENTER EXPONENT: " WITH NO ADVANCING
                   ACCEPT NUM2

                   COMPUTE RES = NUM1 ** NUM2
                   DISPLAY "RESULT: " RES

                   GO TO MAIN-PROCEDURE
               END-IF

               IF CMD IS EQUALS TO "ROOT" THEN
                   DISPLAY "ENTER RADICAND: " WITH NO ADVANCING
                   ACCEPT NUM1

                   DISPLAY "ENTER ROOT INDEX: " WITH NO ADVANCING
                   ACCEPT NUM2

                   COMPUTE RES ROUNDED = NUM1 ** (1 / NUM2)
                   DISPLAY "RESULT: " RES

                   GO TO MAIN-PROCEDURE
               END-IF

               IF CMD IS EQUALS TO "EXIT" THEN
                   DISPLAY "CLOSING PROGRAM."
                   GO TO END-PROGRAM
               ELSE
                   DISPLAY "ERROR: " CMD " COMMAND NOT FOUND."
                   GO TO MAIN-PROCEDURE
               END-IF.
           
           END-PROGRAM.
       STOP RUN.

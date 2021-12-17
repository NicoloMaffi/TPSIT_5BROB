       IDENTIFICATION DIVISION.
       PROGRAM-ID. INPUT.
       AUTHOR. NICOLO` MAFFI.
       INSTALLATION. RASPBERRY PI.
       DATE-WRITTEN. 12/12/2021.
       DATE-COMPILED. 12/12/2021.
       SECURITY. CONFIDENTIAL.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
           77 NUM1               PIC S9(2).
           77 NUM2               PIC S9(3)V9(3).
           01 FISCAL-CODE.
               02 P-NAME.
                   03 LAST-NAME  PIC A(3).
                   03 FIRST-NAME PIC A(3).
               02 BIRTH-DATE.
                   03 YEAR       PIC 9(2).
                   03 MONTH      PIC A.
                   03 B-DAY      PIC 9(2).
               02 DISTRICT       PIC X(4).
               02 CONTROL-CODE   PIC 9.
       PROCEDURE DIVISION.
           DISPLAY "ENTER AN INTEGER: " WITH NO ADVANCING
           ACCEPT NUM1
           DISPLAY "YOU HAVE ENTERED: " NUM1 "!"

           DISPLAY "ENTER A FLOATING-POINT: " WITH NO ADVANCING
           ACCEPT NUM2
           DISPLAY "YOU HAVE ENTERED: " NUM2 "!"

           DISPLAY "ENTER YOUR FISCAL CODE: " WITH NO ADVANCING
           ACCEPT FISCAL-CODE
           DISPLAY LAST-NAME " " FIRST-NAME " " BIRTH-DATE
       STOP RUN.

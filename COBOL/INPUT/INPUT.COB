       IDENTIFICATION DIVISION.
           PROGRAM-ID. INPUT.
           AUTHOR. NICOLO` MAFFI.
           INSTALLATION. 12/12/2021.
           DATE-WRITTEN. 12/12/2021.
           DATE-COMPILED. 12/12/2021.
           SECURITY. DON`T KNOW.
       DATA DIVISION.
           WORKING-STORAGE SECTION.
               77 NUM1              PIC S9(2).
               77 NUM2              PIC S9(3)V9(3).
               01 CODICE-FISCALE.
                   02 NOMINATIVO.
                       03 COGNOME   PIC A(3).
                       03 NOME      PIC A(3).
                   02 DATA-NASCITA.
                       03 ANNO      PIC 9(2).
                       03 MESE      PIC A.
                       03 GIORNO    PIC 9(2).
                   02 COMUNE        PIC X(4).
                   02 COD-CONTROL   PIC 9.
       PROCEDURE DIVISION.
           DISPLAY "ENTER AN INTEGER: " WITH NO ADVANCING
           ACCEPT NUM1
           DISPLAY "YOU HAVE ENTERED: " NUM1 "!"

           DISPLAY "ENTER A FLOATING-POINT: " WITH NO ADVANCING
           ACCEPT NUM2
           DISPLAY "YOU HAVE ENTERED: " NUM2 "!"

           DISPLAY "ENTER YOUR FISCAL CODE: " WITH NO ADVANCING
           ACCEPT CODICE-FISCALE
           DISPLAY COGNOME " " NOME " " DATA-NASCITA
       STOP RUN.

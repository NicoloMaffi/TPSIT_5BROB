       IDENTIFICATION DIVISION.
       PROGRAM-ID. EDITED-PIC.
       AUTHOR. NICOLO' MAFFI.
       INSTALLATION. RASPBERRY PI.
       DATE-WRITTEN. 18/12/2021.
       DATE-COMPILED. 18/12/2021.
       SECURITY. CONFIDENTIAL.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
           77 START-NUM     PIC 9(8)V99 VALUE 00001123.55.
           77 NO-ZERO       PIC ZZZZZZZ9.99.
           77 NO-ZERo-COMMA PIC ZZ,ZZZ,ZZ9.99.
           77 DOLLAR        PIC $$,$$$,$$9.99.
           77 BIRTH-DAY     PIC 9(8) VALUE 21121974.
           77 DATE-FORMAT   PIC 99/99/9999.
       PROCEDURE DIVISION.
           DISPLAY NO-ZERO
           MOVE START-NUM TO NO-ZERO
           DISPLAY NO-ZERO

           DISPLAY "--------------------"

           DISPLAY NO-ZERO-COMMA
           MOVE START-NUM TO NO-ZERO-COMMA
           DISPLAY NO-ZERO-COMMA

           DISPLAY "--------------------"

           DISPLAY DOLLAR
           MOVE START-NUM TO DOLLAR
           DISPLAY DOLLAR

           DISPLAY "--------------------"

           DISPLAY DATE-FORMAT
           MOVE START-NUM TO DATE-FORMAT
           DISPLAY DATE-FORMAT

           DISPLAY "--------------------"

           MOVE BIRTH-DAY TO DATE-FORMAT
           DISPLAY DATE-FORMAT
       STOP RUN.

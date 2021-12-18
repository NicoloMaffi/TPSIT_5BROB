       IDENTIFICATION DIVISION.
       PROGRAM-ID. FIGURATIVES-COSTANTS.
       AUTHOR. NICOLO' MAFFI.
       INSTALLATION. RASPBERRY PI.
       DATE-WRITTEN. 17/12/2021.
       DATE-COMPILED. 17/12/2021.
       SECURITY. CONFIDENTIAL.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
           77 NUM   PIC 9(4) VALUES IS 30.
           77 ALPHA PIC A(4) VALUE IS HIGH-VALUE.
           77 STR   PIC X(4) VALUE ARE ZEROS.
       PROCEDURE DIVISION.           
           DISPLAY NUM
           DISPLAY ALPHA
           DISPLAY STR

           DISPLAY "--------------------"

           MOVE ZERO TO NUM
           MOVE SPACES TO ALPHA
           MOVE SPACE TO STR
           DISPLAY NUM
           DISPLAY "|" ALPHA "|"
           DISPLAY "|" STR "|"

           DISPLAY "--------------------"

           MOVE LOW-VALUE TO NUM
           MOVE LOW-VALUES TO ALPHA
           MOVE LOW-VALUE TO STR
           DISPLAY "|" NUM "|"
           DISPLAY "|" ALPHA "|"
           DISPLAY "|" STR "|"

           DISPLAY "--------------------"

           MOVE HIGH-VALUE TO NUM
           MOVE HIGH-VALUES TO ALPHA
           MOVE HIGH-VALUE TO STR
           DISPLAY NUM
           DISPLAY ALPHA
           DISPLAY STR

           DISPLAY "--------------------"

           MOVE QUOTE TO ALPHA
           MOVE QUOTES TO STR
           DISPLAY ALPHA
           DISPLAY STR

           MOVE ALL "{" TO STR
           DISPLAY STR
       STOP RUN.

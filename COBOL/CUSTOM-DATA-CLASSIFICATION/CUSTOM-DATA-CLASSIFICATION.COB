       IDENTIFICATION DIVISION.
       PROGRAM-ID.  CUSTOM-DATA-CLASSIFICATION.
       AUTHOR. NICOLO' MAFFI.
       INSTALLATION. RASPBERRY PI.
       DATE-WRITTEN. 17/12/2021.
       DATE-COMPILED. 17/12/2021.
       SECURITY. CONFIDENTIAL.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SPECIAL-NAMES.
           CLASS GOOD-SCORE IS "A" THRU "C", "D".
       DATA DIVISION.
       WORKING-STORAGE SECTION.
           77 SCORE       PIC X VALUE IS ZEROS.
           77 AGE         PIC 999 VALUE IS 0.
           01 CAN-VOTE    PIC 9 VALUE IS ZERO.
               88 CAN-VOTE-FLAG VALUE 1.
               88 CANT-VOTE-FLAG VALUE 0.
           01 TEST-NUMBER PIC x VALUE IS "0".
               88 IS-PRIME VALUE "2", "3", "5", "7".
               88 IS-ODD VALUE "1", "3", "5", "7", "9".
               88 IS-EVEN VALUE "0", "2", "4", "6", "8".
               88 IS-NUMERIC VALUE "0" THRU "9".
       PROCEDURE DIVISION.
           DISPLAY "ENTER YOUR AGE: " WITH NO ADVANCING
           ACCEPT AGE

           IF AGE IS GREATER THAN 17 THEN
               SET CAN-VOTE-FLAG TO TRUE
           ELSE
               SET CANT-VOTE-FLAG TO TRUE
           END-IF
           DISPLAY "VOTE: " CAN-VOTE

           IF AGE LESS THAN 20 AND AGE > 12 THEN
               DISPLAY "YOU ARE A TEENAGER!"
           END-IF

           IF AGE < 10 OR AGE = 13 THEN
               DISPLAY "DON'T KNOW!"
           END-IF
           
           DISPLAY "ENTER YOUR SCORE: " WITH NO ADVANCING
           ACCEPT SCORE

           IF SCORE IS GOOD-SCORE THEN
               DISPLAY "YOU PASSED!"
           ELSE
               DISPLAY "YOU FAILED!"
           END-IF

           IF SCORE IS NOT NUMERIC THEN
               DISPLAY "BAD SCORE"
           END-IF

           IF SCORE IS ALPHABETIC THEN
               DISPLAY "ALSO DAB SCORE"
           END-IF

           IF SCORE IS ALPHABETIC-LOWER THEN
               DISPLAY "BAD AGAIN"
           END-IF

           IF SCORE IS ALPHABETIC-UPPER THEN
               DISPLAY "AND BAD AGAIN"
           END-IF

           DISPLAY "ENTER A NUMBER: " WITH NO ADVANCING
           ACCEPT TEST-NUMBER

           PERFORM UNTIL NOT IS-NUMERIC
               EVALUATE TRUE
                   WHEN IS-PRIME DISPLAY "PRIME NUMBER"
                   WHEN IS-ODD DISPLAY "ODD NUMBER"
                   WHEN IS-EVEN DISPLAY "EVENE NUMBER"
                   WHEN IS-NUMERIC DISPLAY "NUMBER"
                   WHEN OTHER DISPLAY "OTHER"
               END-EVALUATE

               ACCEPT TEST-NUMBER
           END-PERFORM
       STOP RUN.

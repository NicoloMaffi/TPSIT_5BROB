       IDENTIFICATION DIVISION.
       PROGRAM-ID. FILES-3.
       AUTHOR. NICOLO' MAFFI.
       INSTALLATION. RASPBERRY PY.
       DATE-WRITTEN. 19/12/2021.
       DATE-COMPILED. 19/12/2021.
       SECURITY. CONFIDENTIAL.
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT CUSTOMERS-FILE ASSIGN TO "CUSTOMERS.dat"
               ORGANIZATION IS LINE SEQUENTIAL
               ACCESS IS SEQUENTIAL.
       DATA DIVISION.
       FILE SECTION.
       FD CUSTOMERS-FILE.
           01 CUSTOMER-DATA.
               02 ID-NUMBER      PIC 9(5).
               02 CUSTOMER-NAME.
                   03 F-NAME     PIC X(20).
                   03 L-NAME     PIC X(20).
       WORKING-STORAGE SECTION.
           01 WS-CUSTOMER-DATA.
               02 WS-ID-NUMBER      PIC 9(5).
               02 WS-CUSTOMER-NAME.
                   03 WS-F-NAME     PIC X(20).
                   03 WS-L-NAME     PIC X(20).
           77 EOF                   PIC A.
       PROCEDURE DIVISION.
           OPEN INPUT CUSTOMERS-FILE
               PERFORM UNTIL EOF IS EQUALS TO '1'
                   READ CUSTOMERS-FILE INTO WS-CUSTOMER-DATA
                       AT END MOVE '1' TO EOF
                       NOT AT END DISPLAY WS-CUSTOMER-DATA
                   END-READ
               END-PERFORM
           CLOSE CUSTOMERS-FILE
       STOP RUN.

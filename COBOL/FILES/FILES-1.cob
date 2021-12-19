       IDENTIFICATION DIVISION.
       PROGRAM-ID. FILES-1.
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
       CONFIGURATION SECTION.
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
       PROCEDURE DIVISION.
           OPEN OUTPUT CUSTOMERS-FILE
               MOVE 00001 TO ID-NUMBER.
               MOVE 'DOUG' TO F-NAME.
               MOVE 'THOMAS' TO L-NAME.
               WRITE CUSTOMER-DATA
               END-WRITE.
           CLOSE CUSTOMERS-FILE
       STOP RUN.

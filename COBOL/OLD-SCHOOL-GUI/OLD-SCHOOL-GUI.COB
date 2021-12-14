       IDENTIFICATION DIVISION.
           PROGRAM-ID. OLD-SCHOOL-GUI.
           AUTHOR. NICOLO` MAFFI.
           INSTALLATION. RASPBERRY PI.
           DATE-WRITTEN. 13/12/2021.
           DATE-COMPILED. 13/12/2021.
           SECURITY. CONFIDENTIAL.
       DATA DIVISION.
           WORKING-STORAGE SECTION.
               01 PERSON.
                   02 LAST-NAME  PIC A(30).
                   02 FIRST-NAME PIC A(30).
                   02 P-ADDRESS  PIC X(30).
                   02 CITY       PIC A(30).
           SCREEN SECTION.
               01 INIT-VIEW.
                   02 BLANK SCREEN BACKGROUND-COLOR 1
                       FOREGROUND-COLOR 10.
               01 INPUT-PERSON.
                   02 VALUE "LAST NAME   : " LINE 6 COLUMN 20.
                   02 PIC X(25) USING LAST-NAME REVERSE-VIDEO.
                   02 VALUE "FIRST NAME  : " LINE 7 COLUMN 20.
                   02 PIC X(25) USING FIRST-NAME REVERSE-VIDEO.
                   02 VALUE "ADDRESS     : " LINE 8 COLUMN 20.
                   02 PIC X(30) USING P-ADDRESS REVERSE-VIDEO.
                   02 VALUE "CITY        : " LINE 9 COLUMN 20.
                   02 PIC X(20) USING CITY REVERSE-VIDEO.
       PROCEDURE DIVISION.
               DISPLAY INIT-VIEW

               DISPLAY INPUT-PERSON
               ACCEPT INPUT-PERSON
       STOP RUN.

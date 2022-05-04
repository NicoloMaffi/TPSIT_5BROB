import requests, sqlite3

#Costanche che indicoano gli url delle varie web API
URL_API_ID_GRANDEZZA = "http://127.0.0.1:5000/api/v1/get_id_grandezza?nome={}"
URL_API_ID_STAZIONE = "http://127.0.0.1:5000/api/v1/get_id_stazione?nome={}"
URL_API_MISURAZIONE = "http://127.0.0.1:5000/api/v1/put_misurazione?val={}&idGrand={}&idStaz={}&data={}"
URL_API_STATISTICHE = "http://127.0.0.1:5000/api/v1/get_statistiche?idStaz={}&idGrand={}"

#Costanti che definiscono i messaggi di errore che le web API ritornano
STATUS_CODE_OK = "OK"
STATUS_CODE_ERROR = "ERROR"
STATUS_CODE_NOT_FOUND = "NOT FOUND"

#Funzione che permette di inserire una misura nel database sul server
def inserire_misura():
    #NOTA: i parametri inseriti dall'utente (compresa la data) possono inserire degli spazi (carattere blank -> " ")
    #Per evitare che la query string non legga correttamente i dati inseriti occorre sistituire nelle stringe il carattere
    # spazio con il carattere del più -> "+"
    #(se si inseriscono i parametri tra virgolette al posto di fare questa operaione, le virgolette rimarranno nel db)

    #Inserimento del nome della stazione dove si effettua la misurazione
    #A seconda dei messaggi che il server restituisce vengono stampati dei messaggi opportuni
    input_utente = input("Nome stazione: ")
    r = requests.get(URL_API_ID_STAZIONE.format(input_utente)).json()
    if r["STATUS_CODE"] == STATUS_CODE_ERROR:
        print("Error: Errore del server. Controllare la correttezza della query string!")
        return
    elif r["STATUS_CODE"] == STATUS_CODE_NOT_FOUND:
        print("Warning: Dati inseriti non trovati!")
        return
    else:
        id_stazione = r["ID"] #Caso di successo

    #Inserimento del nome della grandezza su cui si effettua la misurazione
    #A seconda dei messaggi che il server restituisce vengono stampati dei messaggi opportuni
    input_utente = input("Nome grandezza: ")
    r = requests.get(URL_API_ID_GRANDEZZA.format(input_utente.replace(" ", "+"))).json()
    if r["STATUS_CODE"] == STATUS_CODE_ERROR:
        print("Error: Errore del server. Controllare la correttezza della query string!")
        return
    elif r["STATUS_CODE"] == STATUS_CODE_NOT_FOUND:
        print("Warning: Dati inseriti non trovati!")
        return
    else:
        id_grandezza = r["ID"] #Caso di successo

    #Inserimento del valore della misurazione (constrollo di errori sul tipo di dato inserito)
    try:
        valore = float(input("Valore misurato: "))
    except:
        print("Error: Errore inserire un valore corretto della misurazione!")
        return

    #Inseriento della data ed ora della misurazione
    data = input("Data (formato AAAA-MM-GG hh:mm:ss): ")

    #Chiamata della web api che inserisce i valori (inseriti dall'utente) nel database
    #Stampa dei messaggi opportuni a seconda dei messaggi che il server restituisce
    r = requests.get(URL_API_MISURAZIONE.format(valore, id_grandezza, id_stazione, data.replace(" ", "+"))).json()
    if r["STATUS_CODE"] == STATUS_CODE_ERROR:
        print("Error: Errore del server. Controllare la correttezza della query string e dei dati inseriti!")
    else:
        print("\nL'operazione è andata a buon fine!")

#Funzione che permette di ottenere delle statistiche sulla stazione e grandezza inserite
def statistiche():
    #Inserimento del nome della stazione
    #A seconda dei messaggi che il server restituisce vengono stampati dei messaggi opportuni
    input_utente = input("Nome stazione: ")
    r = requests.get(URL_API_ID_STAZIONE.format(input_utente.replace(" ", "+"))).json()
    if r["STATUS_CODE"] == STATUS_CODE_ERROR:
        print("Error: Errore del server. Controllare la correttezza della query string!")
        return
    elif r["STATUS_CODE"] == STATUS_CODE_NOT_FOUND:
        print("Error: Errore del client. Il nome della stazione inserito non è stato trovato!")
        return
    else:
        id_stazione = r["ID"] #Caso di successo

    #Inserimento del nome della grandezza
    #A seconda dei messaggi che il server restituisce vengono stampati dei messaggi opportuni
    input_utente = input("Nome grandezza: ")
    r = requests.get(URL_API_ID_GRANDEZZA.format(input_utente.replace(" ", "+"))).json()
    if r["STATUS_CODE"] == STATUS_CODE_ERROR:
        print("Error: Errore del server. Controllare la correttezza della query string!")
        return
    elif r["STATUS_CODE"] == STATUS_CODE_NOT_FOUND:
        print("Error: Errore del client. Il nome della grandezza inserito non è stato trovato!")
        return
    else:
        id_grandezza = r["ID"]

    #Stampa dei messaggi di errore (se c'è ne sono) o dei risultati
    r = requests.get(URL_API_STATISTICHE.format(id_stazione, id_grandezza)).json()
    if r["STATUS_CODE"] == STATUS_CODE_ERROR:
        print("Error: Errore del server. Controllare la correttezza della query string!")
    elif r["STATUS_CODE"] == STATUS_CODE_NOT_FOUND:
        print("Warning: Dati inseriti non trovati o informazioni richieste non presenti!")
    else:
        print(f"\nMEDIA DEI VALORI: {r['DATA'][0]}")
        print(f"VALORE MASSIMO:   {r['DATA'][1]}")
        print(f"VALORE MINIMO:    {r['DATA'][2]}")

#Funzione main del programma (con la scelta delle opzioni possibili)
def main():
    while True:
        scelta = input(
            "\nCLIENT PER INTERROGAZIONE SERVER STAZIONE METEOROLOGICA\n\n" \
            "\t+----------------------+\n" \
            "\t| SCEGLIERE UN'OPZIONE |\n" \
            "\t+----------------------+\n" \
            "\t| 1.Inserire misura    |\n" \
            "\t| 2.Statistiche        |\n" \
            "\t| 3.esci               |\n" \
            "\t+----------------------+\n\n" \
            "opzione> "
        )

        print("\n", end='')

        if scelta == "1":
            inserire_misura()
        elif scelta == "2":
            statistiche()
        elif scelta == "3":
            break
        else:
            print(f"Errore: Opzione '{scelta}' non trovata!")
        
        input()   

if __name__ == "__main__":
    main()
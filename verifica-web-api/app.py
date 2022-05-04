import flask, sqlite3

app = flask.Flask(__name__)

#Path relativo del database (utilizzato per accedere ai dati)
DATABASE_PATH = "./meteo_db.db"

#Costanti che definiscono i messaggi di errore che le web API ritornano
STATUS_CODE_OK = "OK"
STATUS_CODE_ERROR = "ERROR"
STATUS_CODE_NOT_FOUND = "NOT FOUND"

#Funzione che effettua una query di select al database sqlite3, restituisce un risultato opportuno e gestisce gli eventuali errori
def sqlite3_query(query, params = ()):
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        curs = conn.cursor()
        rows = curs.execute(query, params).fetchall()
        conn.close()

        return rows
    except Exception as e:
        return None

#Funzione che effettua una query di update al database sqlite3, restituisce un risultato opportuno e gestisce gli eventuali errori
def sqlite3_update(query, params = ()):
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        curs = conn.cursor()
        curs.execute(query, params)
        conn.commit()
        conn.close()

        return True
    except:
        return False

#Web api per richiedere l'id della grandezza
@app.route("/api/v1/get_id_grandezza", methods = ["GET"])
def get_id_grandezza():
    result = {"STATUS_CODE": STATUS_CODE_ERROR, "ID": None}

    if flask.request.method == "GET" and "nome" in flask.request.args:
        #Catura dei parametri nella query string
        nome_grandezza = flask.request.args.get("nome")

        rows = sqlite3_query("SELECT id_misura FROM grandezze WHERE grandezza_misurata = ?", (nome_grandezza,))

        #Impostazione del messaggio di errore a seconda del risultato della query
        if rows == []:
            result["STATUS_CODE"] = STATUS_CODE_NOT_FOUND
        elif rows is not None:
            result["STATUS_CODE"] = STATUS_CODE_OK
            result["ID"] = rows[0][0]

    #Restituzione messaggio e dato richiesto
    return flask.jsonify(result)

#Web api per richiedere l'id della stazione
@app.route("/api/v1/get_id_stazione", methods = ["GET"])
def get_id_stazione():
    result = {"STATUS_CODE": STATUS_CODE_ERROR, "ID": None}

    if flask.request.method == "GET" and "nome" in flask.request.args:
        #Catura dei parametri nella query string
        nome_stazione = flask.request.args.get("nome")

        rows = sqlite3_query("SELECT id_stazione FROM stazioni WHERE nome = ?;", (nome_stazione,))

        #Impostazione del messaggio di errore a seconda del risultato della query
        if rows == []:
            result["STATUS_CODE"] = STATUS_CODE_NOT_FOUND
        elif rows is not None:
            result["STATUS_CODE"] = STATUS_CODE_OK
            result["ID"] = rows[0][0]

    #Restituzione messaggio e dato richiesto
    return flask.jsonify(result)

#Web api per richiedere l'input di una misurazione nel db
@app.route("/api/v1/put_misurazione", methods = ["GET"])
def put_misurazione():
    result = {"STATUS_CODE": STATUS_CODE_ERROR}

    if flask.request.method == "GET" and all(e in ["val", "idGrand", "idStaz", "data"]  for e in flask.request.args):
        #Catura dei parametri nella query string
        valore = flask.request.args.get("val")
        id_grandezza = flask.request.args.get("idGrand")
        id_stazione = flask.request.args.get("idStaz")
        data = flask.request.args.get("data")

        #Query di inserimento nel database (con gestione degli errori e dei relativi messaggi)
        if sqlite3_update("INSERT INTO misurazioni VALUES (NULL, ?, ?, ?, ?);", (id_stazione, id_grandezza, data, valore)):
            result["STATUS_CODE"] = STATUS_CODE_OK

    #Ritorno del messaggio
    return flask.jsonify(result)

#Web api per richiedere le statistiche di una stazione e grandezza richiesta
@app.route("/api/v1/get_statistiche", methods = ["GET"])
def get_statistiche():
    result = {"STATUS_CODE": STATUS_CODE_ERROR, "DATA": None}

    if flask.request.method == "GET" and all(e in ["idStaz", "idGrand"]  for e in flask.request.args):
        #Catura dei parametri nella query string
        id_stazione = flask.request.args.get("idStaz")
        id_grandezza = flask.request.args.get("idGrand")

        #Query con funzioni di aggregazione per calcolare media, max e min dei dati in input
        rows = sqlite3_query("SELECT AVG(valore), MAX(valore), MIN(valore) FROM misurazioni WHERE id_stazione = ? AND id_grandezza = ?;", (id_stazione, id_grandezza))

        #Impostazione del messaggio di errore a seconda del risultato della query
        if rows == [] or None in rows[0]:
            result["STATUS_CODE"] = STATUS_CODE_NOT_FOUND
        elif rows is not None:
            result["STATUS_CODE"] = STATUS_CODE_OK
            result["DATA"] = rows[0]

     #Restituzione messaggio e dato richiesto
    return flask.jsonify(result)

if __name__ == "__main__":
    app.run(debug = True, host = "127.0.0.1")
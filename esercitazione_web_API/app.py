import flask, sqlite3, random

DATABASE_PATH = './operations.db'

app = flask.Flask(__name__)

@app.route("/api/v1/graboperation", methods = ["GET"])
def grab_operation():
    clientId = None
    result = {
        "state": "ERROR",
        "operationId": None,
        "operation": None
    }

    if flask.request.method == "GET":
        clientId = flask.request.args.get("clientId")

    if clientId is None:
        return flask.jsonify(result)

    conn = sqlite3.connect(DATABASE_PATH)
    curs = conn.cursor()
    records = curs.execute("SELECT operationId, operation FROM operations WHERE result IS NULL AND clientId = ?;", (clientId,)).fetchall()
    conn.close()

    if records == []:
        return flask.jsonify(result)

    randomOperation =  random.choice(records)

    result["state"] = "OK"
    result["operationId"] = randomOperation[0]
    result["operation"] = randomOperation[1]

    return flask.jsonify(result)

@app.route("/api/v1/compute", methods = ["GET"])
def put_result():
    operationId = None
    result = None
    result_api = {
        "state": "ERROR"
    }

    if flask.request.method == "GET":
        operationId = flask.request.args.get("operationId")
        result = flask.request.args.get("result")

    if operationId is None or result is None:
        return flask.jsonify(result_api)

    conn = sqlite3.connect(DATABASE_PATH)
    curs = conn.cursor()
    curs.execute("UPDATE operations SET result = ? WHERE operationId = ?;", (result, operationId))
    conn.commit()
    conn.close()

    result_api["state"] = "OK"

    return flask.jsonify(result_api)

if __name__ == "__main__":
    app.run(debug = False, host = "127.0.0.1")
import flask

app = flask.Flask(__name__)

BOOKS = [
    {
        'id': 0,
        'title': 'Il nome della Rosa',
        'author': 'Umberto Eco',
        'year_published': '1980'
    },
    {
        'id': 1,
        'title': 'Il problema dei tre corpi',
        'author': 'Liu Cixin',
        'year_published': '2008'
    },
    {
        'id': 2,
        'title': 'Fondazione',
        'author': 'Isaac Asimov',
        'year_published': '1951'
    },
]

@app.route("/", methods=["GET"])
def index():
    return "<h1>Biblioteca Online</h1> <p>Prototipo di web API.</p>"

#/<api>/<versione>/<resources = attinge a risorse>/nome_risorsa/...
@app.route('/api/v1/resources/books/all', methods=["GET"])
def api_all():
    return flask.jsonify(BOOKS)

@app.route('/api/v1/resources/books', methods=["GET"])
def api_book():
    if 'id' in flask.request.args:
        id = int(flask.request.args["id"])
    else:
        return "Error: No id in field provided. Please specify!"

    result = []
    for book in BOOKS:
        if book['id'] == id:
            result.append(book)

    return flask.jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')
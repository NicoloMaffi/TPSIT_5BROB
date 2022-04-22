import flask

app = flask.Flask(__name__)
app.secret_key = "secret key!"

true_password = "Fr1"
keep_logged = ""

def log_in_html(message):
    return f"\
    <!DOCTYPE html>\
    <html lang='en'>\
    <head>\
        <title>Prova di bruteforce - Log in</title>\
    </head>\
    <body>\
        <form action='/' method='POST'>\
            <input type='text' name='username' placeholder='Username' autocomplete='off'>\
            <br><br>\
            <input type='password' name='password' placeholder='Password'>\
            <br><br>\
            <button type='submit'>Submit</button>\
            <br><br>\
            <input type='checkbox' name='keep_me_logged'> Keep me logged\
        </form>\
        <br><br>\
        <b>{message}</b>\
    </body>\
    </html>\
    "

def home_html(username):
    return f"\
    <!DOCTYPE html>\
    <html lang='en'>\
    <head>\
        <title>Prova di bruteforce - Home</title>\
    </head>\
    <body>\
        <form action='/home' method='POST'>\
            <h1>Benvenuto {username}</h1>\
            <button type='submit'>Log out</button>\
        </form>\
    </body>\
    </html>\
    "

@app.route("/", methods = ["GET", "POST"])
def index():
    global keep_logged

    if "username" in flask.session:
        return flask.redirect(flask.url_for("home"))

    if keep_logged != "":
        flask.session["username"] = keep_logged
        return flask.redirect(flask.url_for("home"))

    if flask.request.method == "POST":
        password = flask.request.form.get("password")
        username = flask.request.form.get("username")
        keep_me_logged = flask.request.form.get("keep_me_logged")

        if username == "" or password == "":
            return log_in_html("Please fill every fields!")

        if password == true_password:
            if keep_me_logged is not None:
                keep_logged = username

            flask.session["username"] = username
            return flask.redirect(flask.url_for("home"))
        else:
            return log_in_html("Wrong password!")
    
    return log_in_html("")

@app.route("/home", methods = ["GET", "POST"])
def home():
    if "username" not in flask.session:
        return flask.redirect(flask.url_for("index"))

    if flask.request.method == "POST":
        return flask.redirect(flask.url_for("log_out"))

    username = flask.session.get("username")

    return home_html(username)

@app.route("/log_out")
def log_out():
    global keep_logged

    if "username" in flask.session:
        keep_logged = ""
        flask.session.pop("username")

    return flask.redirect(flask.url_for("index"))

if __name__ == "__main__":
    app.run(debug = False, host = "127.0.0.1")
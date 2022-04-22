import hashlib
import flask
import sqlite3
from sympy import *
import datetime

DATABASE_PATH = './data.db'

NO_ERROR = 0
EMPTY_FIELDS_ERROR = -1
WRONG_UNAME_ERROR = -2
WRONG_PASSWD_ERROR = -3

serverweb = flask.Flask(__name__)

x, y, z, t = symbols('x y z t')

def login_checker(username, password):
    if username == "" or password == "":
        return EMPTY_FIELDS_ERROR

    conn = sqlite3.connect(DATABASE_PATH)
    curs = conn.cursor()

    row = curs.execute(f"SELECT password FROM users WHERE username = '{username}';").fetchall()

    if row == []:
        conn.close()
        return WRONG_UNAME_ERROR
    
    if password != row[0][0]:
        conn.close()
        return WRONG_PASSWD_ERROR

    conn.close()

    return NO_ERROR

@serverweb.route('/', methods=['POST', 'GET'])
def index():
    error_mssg = None

    if flask.request.method == 'POST':
        if flask.request.form.get('login'):
            username = flask.request.form.get('username')
            password = flask.request.form.get('password')

            error_code = login_checker(username, password)

            if error_code == EMPTY_FIELDS_ERROR:
                error_mssg = "Please fill every fields!"
            elif error_code == WRONG_UNAME_ERROR:
                error_mssg = "Invalid username. Please try again!"
            elif error_code == WRONG_PASSWD_ERROR:
                error_mssg = "Invalid password. Please try again!"
            else:
                resp = flask.make_response(flask.redirect(flask.url_for('calculator')))
                resp.set_cookie("username", username)

                return resp

    return flask.render_template('index.html', error=error_mssg)

def save_calculation(data):
    username = flask.request.cookies.get("username")
    input_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if data is None:
        return username

    conn = sqlite3.connect(DATABASE_PATH)
    curs = conn.cursor()

    curs.execute(f"INSERT INTO calculation_history VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", (None, username, data[0], data[1], data[2], data[3], data[4], data[5], input_date))
    conn.commit()

    conn.close()

    return username

@serverweb.route('/calculator', methods=['POST', 'GET'])
def calculator():
    result = None
    data = None

    if flask.request.method == 'POST':
        function = flask.request.form.get('function')
        upper_extreme = flask.request.form.get('upper_extreme')
        lower_extreme = flask.request.form.get('lower_extreme')
        integration_variable = flask.request.form.get('integration_variable')
        integration_type = ""

        if function == "":
            resp = flask.make_response(flask.render_template('calculator.html', result="Error: Enter the function expression!"))
            resp.set_cookie("username", save_calculation(data))

            return resp

        if integration_variable == "":
            integration_variable = "x"

        if flask.request.form.get('definite_integral'):
            if upper_extreme == "" or lower_extreme == "":
                resp = flask.make_response(flask.render_template('calculator.html', result="Error: Enter both lower and upper extreme!"))
                resp.set_cookie("username", save_calculation(data))

                return resp

            result = integrate(function, (eval(integration_variable), lower_extreme, upper_extreme))
            integration_type = "definite"
        elif flask.request.form.get('indefinite_integral'):
            result = integrate(function, eval(integration_variable))
            integration_type = "indefinite"

        data = [integration_type, function, integration_variable, upper_extreme, lower_extreme, str(result)]

        result = f"Result: {result}"

    resp = flask.make_response(flask.render_template('calculator.html', result=result))
    resp.set_cookie("username", save_calculation(data))

    return resp

if __name__ == "__main__":
    serverweb.run(debug=True, host="127.0.0.1")
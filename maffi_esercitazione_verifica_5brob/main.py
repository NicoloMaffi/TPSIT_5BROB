import flask
import sqlite3
import socket

DATABASE_PATH = "./data.db"

serverweb = flask.Flask(__name__)

@serverweb.route('/', methods=['POST', 'GET'])
def index():
    result = ""

    if flask.request.method == 'POST':
        if flask.request.form.get("scan"):
            ip_addr = flask.request.form.get("ipaddr")
            min_port = int(flask.request.form.get("minport"))
            max_port = int(flask.request.form.get("maxport"))

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conn = sqlite3.connect(DATABASE_PATH)
            curs = conn.cursor()

            port = min_port
            while port <= max_port:
                scan_res = sock.connect_ex((ip_addr, port))

                try:
                    protocol = socket.getservbyport(port, "tcp")
                except OSError:
                    protocol = "Not found"

                curs.execute("INSERT INTO conn_tests VALUES (?, ?, ?, ?)", (None, ip_addr, port, scan_res))
                conn.commit()

                curs.execute("INSERT OR IGNORE INTO port_protocols VALUES (?, ?)", (port, protocol))
                conn.commit()

                port += 1

            conn.close()
            sock.close()

            result = "Scansione delle porte conclusa"
        elif flask.request.form.get("showres"):
            return flask.redirect(flask.url_for('showres'))

    return flask.render_template('index.html', result=result)

@serverweb.route('/showres', methods=['POST', 'GET'])
def showres():
    data_scan = []
    data_prot = []

    conn = sqlite3.connect(DATABASE_PATH)
    curs = conn.cursor()

    data_scan = curs.execute("SELECT * FROM conn_tests;").fetchall()
    data_prot = curs.execute("SELECT * FROM port_protocols;").fetchall()

    conn.close()

    return flask.render_template('showres.html', data_scan=data_scan, data_prot=data_prot)

if __name__ == "__main__":
    serverweb.run(debug=False, host="127.0.0.1")
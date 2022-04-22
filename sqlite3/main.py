import sqlite3

def main():
    conn = sqlite3.connect("./data.db")
    curs = conn.cursor()

    #curs.execute("INSERT INTO hw_info VALUES ('192.168.0.23', 'QW:ER:RT:YU:IO:PA'), ('192.168.0.56', 'SD:FG:HJ:KL:ZX:CV'), ('192.168.0.167', 'BN:NM:GH:SD:OP:ER')")
    #conn.commit()

    print(curs.execute("SELECT users.*, hw_info.* FROM users;").fetchall())

if __name__ == "__main__":
    main()
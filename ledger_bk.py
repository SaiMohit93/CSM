import sqlite3

def create():
    con = sqlite3.connect("ledger.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Contact(id INTEGER PRIMARY KEY,Name TEXT,Age INTEGER, Gender TEXT,Phone INTEGER,Mail TEXT,Address TEXT)")
    con.commit()
    con.close()
def viewall():
    con = sqlite3.connect("ledger.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Contact")
    rows = cur.fetchall()
    con.close()
    return rows

def search(Name="",Age="",Gender="",Phone="",Mail="",Address=""):
    con = sqlite3.connect("ledger.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Contact WHERE Name=? OR Age=? OR Gender=? OR Phone=? OR Mail=? OR Address=?",(Name,Age,Gender,Phone,Mail,Address))
    rows = cur.fetchall()
    con.close()
    return rows
def add(Name,Age,Gender,Phone,Mail,Address):
    con = sqlite3.connect("ledger.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Contact VALUES(NULL,?,?,?,?,?,?)",(Name,Age,Gender,Phone,Mail,Address))
    con.commit()
    con.close()
def update(id,Name,Age,Gender,Phone,Mail,Address):
    con = sqlite3.connect("ledger.db")
    cur = con.cursor()
    cur.execute("UPDATE Contact SET Name=?,Age=?,Gender=?,Phone=?,Mail=?,Address=? WHERE id=?",(Name,Age,Gender,Phone,Mail,Address,id))
    con.commit()
    con.close()
def delete(id):
    con = sqlite3.connect("ledger.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Contact WHERE id=?",(id,))
    con.commit()
    con.close()
create()
#print(search(category="social"))

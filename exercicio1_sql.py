import sqlite3

conn = sqlite3.connect('exercicio1_sql.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'mbox.txt'

arquivo = open(fname)

for line in arquivo:
    if not line.startswith("From: "):
        continue

    pieces = line.split()
    email = pieces[1]
    dom = email.split("@")
    org = dom[1]

    cur.execute("SELECT count FROM Counts WHERE org = ? ", (org,))
    row = cur.fetchone()

    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,))
    else:
        cur.execute('''UPDATE Counts SET count = count + 1 WHERE org = ?''', (org,))
    
    conn.commit()
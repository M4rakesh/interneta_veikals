import sqlite3 as db

with db.connect('namat.db') as con:
    cur=con.execute("""SELECT * FROM Nomnieks""")
    nomnieki = cur.fetchall()
    cur=con.execute("""SELECT * FROM Produkts""")
    produkti= cur.fetchall()
    for i in produkti:
        print(i)
    for i in nomnieki:
        print(i)
        print(i[1], 'ar personas kodu = ',
              i[3],'\n')

    
import sqlite3 as db

with db.connect('namat.db') as con:
    cur=con.execute("""SELECT * FROM Nomnieks""")
    nomnieki = cur.fetchall()
    cur=con.execute("""SELECT * FROM Produkts""")
    produkti= cur.fetchall()
    cur=con.execute("""SELECT vards FROM Nomnieks WHERE tel_nr = '12314125423' """)
    nomniek_telef=cur.fetchall()
    for i in produkti:
        print(i)
    for i in nomnieki:
        print(i)
        print(i[1], 'ar personas kodu = ',
              i[3],'\n')
    for i in nomniek_telef:
        print(i)
        cur=con.cursor()
    cur.execute("""SELECT vards,uzvards,tel_nr,beig_datums
        FROM Nomnieks
        INNER JOIN Noma
        ON Noma.id_nomnieks = Nomnieks.id_nomnieks""")
    nomniek=cur.fetchall()
    for i in nomniek:
        print(i)
    cur.execute("""SELECT vards,uzvards,beig_datums
        FROM Nomnieks
        INNER JOIN Noma
        ON Noma.id_nomnieks = Nomnieks.id_nomnieks
        WHERE Nomnieks.tel_nr = '26478493' """)
    nomniek=cur.fetchall()
    for i in nomniek:
        print(i)
    cur.execute("""SELECT vards,uzvards,beig_datums,nomas_cena_diena
        FROM Nomnieks
        INNER JOIN Noma
        ON Noma.id_nomnieks = Nomnieks.id_nomnieks
        INNER JOIN Produkts
        ON Noma.id_produkts = Produkts.id_produkts
        WHERE Nomnieks.tel_nr = '26478493' """)
    nomniek=cur.fetchall()
    sum=0
    for k in nomniek:
        print(k)
        sum= sum + int(k[3])
    print('\nPar izmantotam precēm diena jāmaksa',sum)
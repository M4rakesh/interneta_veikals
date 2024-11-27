import sqlite3

conn = sqlite3.connect('test.db')

print("Datubāze ir izveidota!")

print("Datubāze ir atverta")
'''conn.execute("UPDATE COMPANY set SALARY = 420.00 where ID=2")
conn.commit()
print("Kopēju izmaiņu skaits: ",conn.total_changes)'''
conn.execute("DELETE from COMPANY where ID = 2;")
conn.commit()
print("Dzēstu vienību skaits: ",conn.total_changes)

cursor= conn.execute("SELECT * from COMPANY")
for ieraksts in cursor:
    print("ID=",ieraksts[0])
    print("NAME=",ieraksts[1])
    print("AGE=",ieraksts[2])
    print("ADDRESS=",ieraksts[3])
    print("SALARY=",ieraksts[4],"\n")
print("Dati ir veiksmigi nolasiti")
'''conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES(1,'Paul',32,'California',20000.00)")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES(2,'Dainis',19,'Gornica',777.00)")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES(3,'Jups',45,'Latvia',12000.00)")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES(4,'Ahmed',21,'Dagda',100000.00)")'''
conn.commit()
"""conn.execute('''CREATE TABLE COMPANY (
             ID INT PRIMARY KEY  NOT NULL,
             NAME      TEXT      NOT NULL,
             AGE       INT       NOT NULL,
             ADDRESS   CHAR(50),
             SALARY    REAL);''')
print("Tabula ir izveidota!")"""

conn.close()
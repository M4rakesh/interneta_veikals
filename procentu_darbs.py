import sqlite3

conn = sqlite3.connect('biblioteka.db')

print("Datubāze ir izveidota!")
cursor= conn.execute("SELECT * FROM Gramatas ORDER BY gads ASC")
for ieraksts in cursor:
    print("garmatas_id=",ieraksts[0])
    print("nosaukums=",ieraksts[1])
    print("gads=",ieraksts[2])
    print("autora_id=",ieraksts[3],"\n")
cursor= conn.execute("SELECT * FROM Gramatas WHERE = 'a'")
for ieraksts in cursor:
    print("garmatas_id=",ieraksts[0])
    print("nosaukums=",ieraksts[1])
    print("gads=",ieraksts[2])
    print("autora_id=",ieraksts[3],"\n")


"""conn.execute('''CREATE TABLE autors (
             autora_id      INT PRIMARY KEY  NOT NULL,
             vards          TEXT      NOT NULL,
             uzvards        TEXT       NOT NULL);''')"""
"""conn.execute("INSERT INTO Gramatas (gramatas_id,nosaukums,gads,autora_id)\
             VALUES(1,'Atnāciet rīt','2024',2)")
conn.execute("INSERT INTO Gramatas (gramatas_id,nosaukums,gads,autora_id)\
             VALUES(2,'Lulū un eņģelis','2024',1)")
conn.execute("INSERT INTO autors (autora_id,vards,uzvards)\
             VALUES(1,'Dace','Rukšāne')")
conn.execute("INSERT INTO autors (autora_id,vards,uzvards)\
             VALUES(2,'Dace','Judina')")
conn.execute("INSERT INTO Gramatas (gramatas_id,nosaukums,gads,autora_id)\
             VALUES(3,'Sibīrijas bērni 1949','2022',3)")
conn.execute("INSERT INTO autors (autora_id,vards,uzvards)\
             VALUES(3,'Daugule','Zane')")"""

conn.commit()


conn.close()
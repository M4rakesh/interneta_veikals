import sqlite3
conn=sqlite3.connect('first.db')
cursor=conn.cursor()

cursor.execute('SELECT * FROM Pasutijums')
orders = cursor.fetchall()
print("Pāsūtījumi:")
for order in orders:
    print(order)
cursor.execute(''' SELECT
    Detalas.Detalas_id,
    Pasutijums.datums,
    Klients.Vards,
    Produkti.nosaukums,
    Detalas.daudzums,
    Produkti.cena * Detalas.daudzums AS summa FROM Detalas JOIN
    Pasutijums ON Detalas.Pasutijuma_id = Pasutijums.Pasutijuma_id JOIN     Klients ON Klients.Klienta_id = Pasutijums.Klienta_id JOIN    Produkti ON Detalas.produkts_id = Produkti.Produkts_id    ''')

order_details = cursor.fetchall()
print("\nPAsūtījuma detaļas: ")
for detail in order_details:
    print(detail)


produkts_id=int(input("Ievadi produkta ID: "))
nosaukums=input("Ievadiet produkta nosaukumu: ")
cena=float(input("Ievadi produkta cenu: "))
noliktava=input("Ievadiet niliktavas statusu(piemēram,'ir' bai 'nav')")
cursor.execute('''INSERT INTO Produkti 
               (produkts_id,nosaukums,cena,noliktava)VALUES(?,?,?,?)''', (produkts_id,nosaukums,cena,noliktava))
print("Produkts pievienots")
Klienta_id=int(input("Ievadi klienta ID: "))
Vards=input("Ievadiet Klienta vardu: ")
epasts=input("Ievadiet klienta e-pastu: ")
telefons=input("Ievadiet klienta telefonu: ")
cursor.execute('''INSERT INTO Klients (Klienta_id,Vards,epasts,telefons)VALUES(?,?,?,?)''',
               (Klienta_id,Vards,epasts,telefons))
print("Klients pievienots")
Pasutijuma_id=int(input("Ievadi pasutijuma id: "))
datums=input("Iediet datumu piemeram(12.09.24): ")
kopsumma=float(input("Ievadiet produkta kopsummu: "))
Klienta_id=int(input("Ievadiet klienta ID: "))
cursor.execute('''INSERT INTO Pasutijums JOIN Produkti JOIN Detalas
               (Pasutijuma_id,datums,kosumma,Klienta_id)VALUES(?,?,?,?)''',
               (Pasutijuma_id,datums,kopsumma,Klienta_id))
print("Pasutijums pievienots")
conn.commit()
conn.close()
import sqlite3

conn = sqlite3.connect("aircraft.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM Sensors")
rows = cursor.fetchall()
print("Počet záznamů:", len(rows))

conn.close()


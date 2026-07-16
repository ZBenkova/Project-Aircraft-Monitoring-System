import sqlite3

conn = sqlite3.connect("aircraft.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO Sensors (aircraft, temperature, oil_pressure, fuel_level)
VALUES (?, ?, ?, ?)
""", ("OK-ABC", 85.3, 52.1, 78.4))

conn.commit()
conn.close()

print("Data byla uložena.")
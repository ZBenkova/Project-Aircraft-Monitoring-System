import sqlite3

conn = sqlite3.connect("aircraft.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Sensors (
    id INTEGER PRIMARY KEY,
    aircraft TEXT,
    temperature REAL,
    oil_pressure REAL,
    fuel_level REAL
)
""")

conn.commit()
conn.close()

print("Database created successfully.")
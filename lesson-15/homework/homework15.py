import sqlite3

conn = sqlite3.connect('Roster.db')
cursor = conn.cursor()

create_table = """CREATE TABLE IF NOT EXISTS Roster (
    name TEXT,
    species TEXT,
    age INT
);"""
cursor.execute(create_table)

insert_data = """INSERT INTO Roster VALUES 
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29);"""
try:
    cursor.execute(insert_data)
except sqlite3.IntegrityError:
    pass 

conn.commit()

update_data = """UPDATE Roster SET name = 'Ezri Dax' WHERE name = 'Jadzia Dax';"""
cursor.execute(update_data)
conn.commit()

cursor.execute("SELECT * FROM Roster")
results = cursor.fetchall()

for name, species, age in results:
    print(f"Name: {name}, Species: {species}, Age: {age}")

conn.close()

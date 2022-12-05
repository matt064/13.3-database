from create_tables import engine, measure, stations

# wybor 5 pierwszych kolumn z tabel
conn = engine.connect()

result = conn.execute("SELECT * FROM measure LIMIT 5")
row = result.fetchall()

print(row)
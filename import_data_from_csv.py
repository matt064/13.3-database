import csv
from create_tables import engine, stations


ins = stations.insert()
conn = engine.connect()

# import z pliku clean_stations

with open('clean_stations.csv', 'r') as f:
    stations_csv = csv.DictReader(f)
    for row in stations_csv:
        conn.execute(ins, row)








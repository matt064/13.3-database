import csv
from create_tables import engine, measure


#import z pliku clean_measure

ins = measure.insert()
conn = engine.connect()

with open('clean_measure.csv', 'r') as m:
    measure_csv = csv.DictReader(m)
    for row in measure_csv:
        conn.execute(ins, row)

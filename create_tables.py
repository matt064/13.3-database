from sqlalchemy import create_engine 
from sqlalchemy import Table, MetaData, Column, Integer, Text, Float, String, ForeignKey


# polaczenie z baza danych i stowrzenie tabel

engine = create_engine('sqlite:///database.db')

print(engine.driver)

meta = MetaData()

stations = Table(
   'stations', meta,
   Column('station', Text, primary_key=True),
   Column('latitude', Float),
   Column('longitude', Float),
   Column('elevation', Float),
   Column('name', Text),
   Column('country', Text),
   Column("state", Text)
)

measure = Table(
    'measure', meta,
    Column('station', Text, ForeignKey('stations.station')), 
    Column('date', String),
    Column('precip', Float),
    Column('tobs', Integer)
)


meta.create_all(engine)
print(engine.table_names())

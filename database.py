import sqlite3 as lite
import pandas as pd
import sys

conn = lite.connect('getting_started.db')
c = conn.cursor()

cities = (
    ('New York City', 'NY'),
    ('Boston', 'MA'),
    ('Chicago', 'IL'),
    ('Miami', 'FL'),
    ('Dallas', 'TX'),
    ('Seattle', 'WA'),
    ('Portland', 'OR'),
    ('San Francisco', 'CA'),
    ('Los Angeles', 'CA')
)

weather = (
    ('New York City', 2013, 'July', 'January', 62 ),
    ('Boston', 2013, 'July', 'January', 59 ),
    ('Chicago', 2013, 'July', 'January', 59 ),
    ('Miami', 2013, 'August', 'January', 84 ),
    ('Dallas', 2013, 'July', 'January', 77 ),
    ('Seattle', 2013, 'July', 'December', 61 ),
    ('Portland', 2013, 'July', 'December', 63),
    ('San Francisco', 2013, 'September', 'December', 64 ),
    ('Los Angeles', 2013, 'September', 'December', 75 )
)

with conn:
        c = conn.cursor()
        c.execute("drop table if exists cities")
        c.execute("drop table if exists weather")
        c.execute("create table cities (name text, state text)")
        c.executemany("insert into cities values(?,?)", cities)
        c.execute("create table weather (city text, year integer, warm_month text, cold_month text, average_high integer)");
        c.executemany("insert into weather values(?,?,?,?,?)", weather)
        c.execute("select name, state, year, warm_month, cold_month from cities inner join weather on name = city")
        rows = c.fetchall()
        cols = [desc[0] for desc in c.description]
        df = pd.DataFrame(rows, columns=cols)

        warmestInJuly = df[df['warm_month'] == 'July']
        warmestInJulyList = warmestInJuly.name.tolist()
        months = ''

        for index, line in enumerate(warmestInJulyList):
            print(line)
            months+= ', ' +line

        print('The cities that are warmest in July are' + months +'.')

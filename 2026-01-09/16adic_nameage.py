import sqlite3

# build the database
connection = sqlite3.connect('ages.sqlite')
cursor = connection.cursor()

# empty the database
cursor.execute(
    '''
    DROP TABLE IF EXISTS ages
    ''')
cursor.execute(
    '''
    CREATE TABLE Ages (
        name VARCHAR(128),
        age INTEGER
    )
    ''')

# Insert data
cursor.execute('DELETE FROM Ages')

data = [
    ('Nikolina', 36),
    ('Erdehan', 14),
    ('Kararose', 25),
    ('Jarvi', 40),
    ('Mabruka', 27),
    ('Jeni', 27)
]

cursor.executemany(
    'INSERT INTO Ages (name, age) VALUES (?, ?)',
    data
)


cursor.execute(
    '''
    SELECT hex(name || age) AS X FROM Ages ORDER BY X
    '''
)

print(cursor.fetchall()[0][0])
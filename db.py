import duckdb

# Create a DuckDB database connection
conn = duckdb.connect('ducks.duckdb')

# Create the table'ducks'
conn.execute('''
CREATE TABLE ducks (
    id VARCHAR,
    color VARCHAR,
    firstname VARCHAR,
    lastname VARCHAR,
    gender VARCHAR
)
''')

# Insert data into the table 'ducks'
data = [
    ('kA0KgL', 'red', 'Marty', 'McFly', 'male'),
    ('dx3ngL', 'teal', 'Duckota', 'Fanning', 'female'),
    ('FQ4dU1', 'yellow', 'Duck', 'Norris', 'male'),
    ('JqS7ZZ', 'red', 'James', 'Pond', 'male'),
    ('ZM5uJL', 'black', 'Darth', 'Wader', 'male'),
    ('05FuKa', 'yellow', 'Clint', 'Beakwood', 'male'),
    ('wKq9zD', 'yellow', 'Mary', 'Quackens', 'female'),
    ('QCAb5l', 'orange', 'Ducky', 'Balboa', 'male'),
    ('eKiyA5', 'orange', 'Captain', 'Quack', 'male'),
    ('YiSGQl', 'teal', 'Wonder', 'Duck', 'female')
]

# Insert data into the table
for row in data:
    conn.execute('''
    INSERT INTO ducks (id, color, firstname, lastname, gender) VALUES (?, ?, ?, ?, ?)
    ''', row)

# Close the connection
conn.close()

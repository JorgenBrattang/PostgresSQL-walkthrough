import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# query 2 - select "Name" from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# query 3 - select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# query 4 - select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# query 5 - select only the albums with "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# query 6 - select all tracks where the composer is "Queen" from the "Track"
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["test"])

# SELECT * FROM "Track" WHERE "Composer" = 'Queen';

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (singel)
# results  = cursonr.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)

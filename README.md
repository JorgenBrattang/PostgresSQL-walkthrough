Install PostgreSql.sql

### Then to access the psql command write this is the terminal:
```
set_pg
```

### After that run the psql
```
psql
```


### list the databases
```
\l
```

### Change databases, you will have the names of the databases from the \l command.
```
\c postgres

or

\c chinook
```

### Install the sql file
```
\i Chinook_PostgreSql.sql
```

### Connect directly towards a database
```
psql -d chinook
```

### Read the database
```
\dt
```

### Sample database
```
            List of relations
 Schema |     Name      | Type  | Owner  
--------+---------------+-------+--------
 public | Album         | table | gitpod
 public | Artist        | table | gitpod
 public | Customer      | table | gitpod
 public | Employee      | table | gitpod
 public | Genre         | table | gitpod
 public | Invoice       | table | gitpod
 public | InvoiceLine   | table | gitpod
 public | MediaType     | table | gitpod
 public | Playlist      | table | gitpod
 public | PlaylistTrack | table | gitpod
 public | Track         | table | gitpod
(11 rows)
```

### Access a certain part
```
SELECT * FROM "Artist";
```

### To move back simple press Q
```
Q
```

### Select more specific
```
SELECT "Name" FROM "Artist";
```

### Select even more specific (Same output)
```
SELECT * FROM "Artist" WHERE "Name" = 'Queen';
SELECT * FROM "Artist" WHERE "ArtistId" = 51;
```

### From another one
```
SELECT * FROM "Album" WHERE "ArtistId" = 51;
SELECT * FROM "Track" WHERE "Composer" = 'Queen';
```
import sqlite3

dbs = sqlite3.connect('base.db')
print("DB connected")

dbs.execute(
    "create table owner( name TEXT, email TEXT)"
)
dbs.execute(
    ''' create table card(
        title TEXT,
        id integer primary key not null,
        content TEXT,
        status INTEGER,
        deadline DATETIME,
        parent_list integer,
        
        Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(parent_list) references list(id)
        );''')

dbs.execute(''' create table list(
        title TEXT,
        id integer primary key not null,
        color TEXT,
        owner TEXT,
                FOREIGN KEY(owner) references owner(email));

''')

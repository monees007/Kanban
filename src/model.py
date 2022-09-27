import sqlite3

dbs = sqlite3.connect('base.db')
print("DB connected")

dbs.execute(
    ''' create table card(
        title Varchar,
        # id int primary key not null,
        content varchar,
        status boolean,
        deadline date,
        parent_list int,
        date_created date);''')

dbs.execute(''' create table list(
        title Varchar,
        id int primary key not null,
        color VARCHAR, 
);

''')

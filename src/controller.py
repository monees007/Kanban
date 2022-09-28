from main import app
from model import dbs


def show_card(id):
    pass


def auto_incrementer(t):
    c, l = 0, 0
    if t == 'c':
        c += 1
        return c
    elif t == 'l':
        l += 1
        return l


@app.route("/delete/c<id>")
def delete(id):
    dbs.execute(f"delete from card where id={id};")


@app.route("/new/t=<title>##c=<content>##s=<status>##d=<deadline>##p=<parent_list>##c=<date_created>")
def new(title, content, status, deadline, parent_list, date_created):
    dbs.execute(
        f"insert into card(title, content,status,deadline,parent_list,date_created) values({title}, {content}, {status}, {deadline}, {parent_list}, {date_created});")


@app.route("/create/list##title=<title>##id=<id>##color=<color>")
def create_list(title, color):
    dbs.execute(f"insert into list(title,id, color) values({title},{id},{color});")


@app.route("/delete/l<int :i>")
def delete_list(id):
    dbs.execute(f"delete from list where id={id};")

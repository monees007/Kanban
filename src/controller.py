from main import app
from model import dbs


def showcard():
    pass


@app.route("/delete/<string: id>")
def delete():
    pass


@app.route("/new/<string: type>")
def new():
    pass


def create_list(title, mid, color):
    dbs.execute(f"insert into list(title, id, color) values({title},{color});")


def delete_list():


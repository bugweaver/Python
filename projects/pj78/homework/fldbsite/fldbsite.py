import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, session, redirect, g
from FDataBase import FDataBase

DATABASE = '/tmp/course.db'
DEBUG = True
SECRET_KEY = '428440dba36b4f3e6b6ad05b7bb90c7f53368506'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(DATABASE=os.path.join(app.root_path, 'course.db'))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template(template_name_or_list="index.html", menu=dbase.get_menu(), courses=dbase.get_courses_annonce())


@app.route('/add_course', methods=["POST", "GET"])
def add_course():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['description']) > 10:
            res = dbase.add_course(request.form['name'],
                                   request.form['description'],
                                   request.form['price'],
                                   request.form['url'])
            if not res:
                flash("Ошибка добавления курса", category='error')
            else:
                flash("Курс добавлен успешно", category='success')
        else:
            flash("Ошибка добавления курса", category='error')

    return render_template('add_course.html', menu=dbase.get_menu(), title="Добавление курса")


@app.route("/course/<alias>")
def show_course(alias):
    db = get_db()
    dbase = FDataBase(db)
    title, course = dbase.get_course(alias)

    return render_template("course.html", menu=dbase.get_menu(), title=title, post=course)


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == "__main__":
    app.run(debug=True)

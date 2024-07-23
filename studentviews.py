from flask import Blueprint, g, session, url_for, redirect
from flask import render_template, request, flash
import re
import sqlite3
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, RadioField, TextAreaField, SelectMultipleField, IntegerField
from wtforms.validators import DataRequired, ValidationError

from views import myform

view = Blueprint('view', __name__)
generale = Blueprint('generale', __name__)
lecturee = Blueprint('lecturee', __name__)
departmente = Blueprint('departmente', __name__)
home = Blueprint('home', __name__)

me = ["123544566", "546464", "678855665"]


@view.route('/login', methods=['GET', 'POST'])
def shome():
    form = myform()

    if request.method == 'POST':
        name = request.form.get("username")
        password = request.form.get("password")

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("""
                                         SELECT * FROM students WHERE id =? AND password =?
                                         """, (name,password))
        g.user_data = c.fetchall()

        conn.commit()
        conn.close()
        k = "me"
        session["try1"] = name

        if request.form.get('evaluate') == 'Proceed':
            unit1 = request.form.get("unit1")
            unit2 = request.form.get("unit2")
            course = request.form.get("course")


            return redirect(url_for("lecturee.lectureev", unit1=unit1, unit2=unit2, course=course))
        elif request.form.get('homeb') =='Reset Password':
            return render_template('departmentevaluation.html', form = form)
        elif request.form.get('homeb') =='Reset':
            name = request.form.get("username")
            password = request.form.get("password")
            password2 = request.form.get("password2")
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute("UPDATE students SET password = ? WHERE id = ? AND password = ? ", (password2,name, password))
            conn.commit()
            conn.close()
            return redirect(url_for("view.shome"))
        if len(g.user_data) == 0:
            flash('Incorrect credentials. Please try again.', 'error')
            return redirect(url_for("view.shome"))
        else:
            return render_template('studentpage.html', form=form, name=name, g=g)


    return render_template('studentlogin.html', form=form)


@generale.route('/general', methods=['GET', 'POST'])
def general():
    return render_template('generalevaluation.html')


@lecturee.route('/lecturee', methods=['GET', 'POST'])
def lectureev():
    if "try1" in session:
        try1 = session["try1"]
        unit1 = request.args.get('unit1', 'default_value1')
        unit2 = request.args.get('unit2', 'default_value2')
        course1 = request.args.get('course', 'default_course').strip()
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("""
                                                            SELECT * FROM lectures WHERE department = ? AND unit1 = ? OR unit2=? AND department=?
                                                            OR department=? AND unit2 =? OR department=? AND unit1 =?
                                                        """,
                  (course1, unit1, unit1, course1, course1, unit2, course1, unit2))
        t = c.fetchall()

        conn.commit()
        conn.close()
        conn = sqlite3.connect('question.db')
        c = conn.cursor()
        c.execute("""

                                           SELECT * FROM selectq WHERE unit = ? OR unit=?
                                                     """, (unit1, unit2))
        l = c.fetchall()
        c.execute("""

                                   SELECT * FROM radioq WHERE unit = ? OR unit=?
                                             """, ( unit1, unit2))
        j = c.fetchall()

        c.execute("""   SELECT * FROM textq WHERE unit = ? OR unit=?
                                             """, (unit1, unit2))
        p = c.fetchall()
        c.execute("""   SELECT * FROM rate WHERE unit = ? OR unit=?
                                                     """, (unit1, unit2))
        a = c.fetchall()
        c.execute("""   SELECT * FROM que5 WHERE unit = ? OR unit=?
                                                     """, (unit1, unit2))
        u = c.fetchall()
        c.execute("""   SELECT * FROM que6 WHERE unit = ? OR unit=?
                                                     """, (unit1, unit2))
        h = c.fetchall()
        conn.commit()
        conn.close()
        z = l
        p = p
    que1 = l[0][4]

    class queform(FlaskForm):
        que1 = SelectField(l[0][4],
                           choices=[(l[0][5]), (l[0][6]), (l[0][7]), (l[0][8])])
        select2 = SelectField((l[1][4]),
                              choices=[(l[1][5]), (l[1][6]), (l[1][7]), (l[1][8])])
        radio1 = RadioField((j[0][4]), choices=[(j[0][5]), (j[0][6]), (j[0][7])])
        radio2 = RadioField(j[1][4], choices=[(j[1][5]), (j[1][6]), (j[1][7])])
        querry1 = TextAreaField((p[1][4]), validators=[DataRequired()])
        querry2 = TextAreaField((p[0][4]), validators=[DataRequired()])
        querry4 = IntegerField(a[0][1])
        querry7 = TextAreaField(a[0][2])
        querry5 = SelectField((u[0][1]),
                              choices=[(u[0][2]), (u[0][3]), (u[0][4]), (u[0][5])])
        querry6 = RadioField((h[0][1]), choices=[(h[0][2]), (h[0][3])])
        querry42 = IntegerField(a[0][1])
        querry72 = TextAreaField(a[1][1])
        querry52 = SelectField((u[1][1]),
                                      choices=[(u[1][2]), (u[1][3]), (u[1][4]), (u[1][5])])
        querry62 = RadioField((h[1][1]), choices=[(h[1][2]), (h[1][3])])


    form = queform()
    if request.form.get('submit') == 'submit':
        selectansw1 = form.que1.data
        selectansw2 = form.select2.data
        radioansw1 = form.radio1.data
        radioansw2 = form.radio2.data
        textansw1 = form.querry1.data
        textansw2 = form.querry2.data
        lecture1 = request.form.get("lecturer1")
        lecture2 = request.form.get("lecturer2")
        unit3 = request.form.get("unit3")
        unit4 = request.form.get("unit4")
        sque1 = request.form.get("sque1")
        rque1 = request.form.get("rque1")
        tque1 = request.form.get("tque1")
        id1 = request.form.get("id1")
        id2 = request.form.get("id2")
        sque2 = request.form.get("sque2")
        rque2 = request.form.get("rque2")
        tque2 = request.form.get("tque2")
        que4 = request.form.get("tque4")
        q4answ= form.querry4.data
        que7 = request.form.get("tque7")
        q7answ=form.querry7.data
        que5 = request.form.get("tque5")
        q5answ = form.querry5.data
        que6 = request.form.get("tque6")
        q6answ = form.querry6.data
        que42 = request.form.get("tque4")
        q42answ = form.querry42.data
        que72 = request.form.get("tque72")
        q72answ = form.querry7.data
        que52 = request.form.get("tque52")
        q52answ = form.querry52.data
        que62 = request.form.get("tque62")
        q62answ = form.querry62.data
        conn = sqlite3.connect('answers.db')
        c = conn.cursor()
        c.execute("""
                  INSERT INTO answer(id1,  name1,unit1, sque1,sansw1, rque1, ransw1, tque1,
                   tansw1, que4,answ4, que7, answ7, que5,answ5, que6, answ6
                   ,id2, name2, unit2, sque2,sansw2 , rque2, ransw2, tque2, tansw2
                   , que42,answ42, que72, answ72, que52, answ52, que62, answ62) 
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?,?,?, ?,?,?,?,?,?,?,?,?,?)
                  """, (id1,lecture1,unit3,sque1,selectansw1,rque1,radioansw1,tque1,textansw1,que4, q4answ, que7, q7answ, que5, q5answ, que6,q6answ,
                        id2,lecture2,unit4,sque2,selectansw2,rque2,radioansw2,tque2,textansw2, que42, q42answ, que72, q72answ, que52, q52answ, que62, q62answ))
        c.execute("""
                          INSERT INTO answer2(id,  name,unit, sque,sansw, rque, ransw, tque,
                           tansw, que4,answ4, que7, answ7, que5,
                                  answ5, que6, answ6) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",(id1, lecture1,unit3,sque1,
                                                                selectansw1,rque1,radioansw1,tque1,textansw1, que4, q4answ, que7, q7answ, que5, q5answ, que6,q6answ))

        c.execute("""
                                  INSERT INTO answer2(id,  name,unit, sque,sansw, rque, ransw, tque,
                                   tansw, que4,answ4, que7, answ7, que5,
                                  answ5, que6, answ6) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                  (id2, lecture2, unit4, sque2, selectansw2, rque2, radioansw2, tque2, textansw2, que42, q42answ, que72, q72answ, que52, q52answ, que62, q62answ))
        c.execute("""
                                  INSERT INTO answ3(id,  lecturer,unit, que4,answ4, que7, answ7, que5,
                                  answ5, que6, answ6) VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
                  (id1, lecture1, unit3, que4, q4answ, que7, q7answ, que5, q5answ, que6,q6answ))
        c.execute("""
                                          INSERT INTO answ3(id,  lecturer,unit, que4,answ4, que7, answ7, que5,
                                           answ5, que6, answ6) VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
                  (id1, lecture1, unit3, que42, q42answ, que72, q72answ, que52, q52answ, que62, q62answ))
        conn.commit()
        conn.close()

        return redirect(url_for("view.shome"))

    return render_template('lectureevaluation.html', form=form, try1=try1, unit1=unit1, unit2=unit2, course=course1, t=t,
                           l=l, p=p,j=j, a=a, h=h, u=u, x=t)


@departmente.route('/department', methods=['GET', 'POST'])
def dpt():
    return render_template('departmentevaluation.html')


@home.route('/home', methods=['GET', 'POST'])
def hpage():
    form = myform()
    if request.form.get('evaluate') == 'Proceed':
        return render_template("chooseunit.html", form=form)
    elif request.form.get('chooseunit') == 'Proceed':
        return render_template('lectureevaluation.html', form=form)

    return render_template("studentpage.html", form=form)

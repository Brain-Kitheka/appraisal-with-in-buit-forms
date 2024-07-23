from flask import Blueprint, url_for, redirect
from flask import render_template, request, flash
import sqlite3
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired


class myform(FlaskForm):
    conn = sqlite3.connect('question.db')
    c = conn.cursor()
    c.execute("""
       SELECT question FROM textq WHERE id = 'Q1' 
       """)
    g = c.fetchall()
    c.execute("""
          SELECT * FROM radioq WHERE id = 'Q1' 
          """)
    m = c.fetchall()
    c.execute("""
              SELECT * FROM selectq WHERE id = 'Q1' 
              """)
    n = c.fetchall()

    conn.commit()
    conn.close()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("""
              SELECT * FROM students
              """)
    q = c.fetchall()
    conn.commit()
    conn.close()
    textarea3 = TextAreaField("update Question", validators=[DataRequired()])
    p1 = StringField("Option 1")
    p2 = StringField("Option 2")
    p3 = StringField("Option 3")
    p4 = StringField("Option 4")
    updatetxt3 = SubmitField("update")
    textarea2 = TextAreaField("update Question")
    p = StringField("Option 1")
    p5 = StringField("Option 2")
    p6 = StringField("option 3")
    updatetxt2 = SubmitField("update")
    textarea1 = TextAreaField("update Question", validators=[DataRequired()])
    updatetxt1 = SubmitField("update")
    deletelec = SubmitField("Remove Lecture")
    course = SubmitField("Next")
    unitevaluation1 = SubmitField("Next")
    submit = SubmitField("Save Form")
    password1 = StringField("Enter password")
    studentusername = StringField("Enter username")
    lectureid = StringField("Lecture ID")
    lectureunit = StringField("Target unit")
    que4 = TextAreaField("(Rating) range 1-5")
    que7 = TextAreaField("recommended to follow up about rating question")
    que5 = TextAreaField("question for multiple selection")
    q5answ1 = StringField("option 1")
    q5answ2 = StringField("option 2")
    q5answ3 = StringField("option 3")
    q5answ4 = StringField("option4")
    que6 = TextAreaField("boolean questions question")
    q6answ1 = StringField("option 1")
    q6answ2 = StringField("option 2")
    target = StringField("Target Unit")


views = Blueprint('views', __name__)
reports = Blueprint('reports', __name__)
lectures = Blueprint('lectures', __name__)
students = Blueprint('students', __name__)
courses = Blueprint('courses', __name__)
forms = Blueprint('forms', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    form = myform
    if request.method == 'POST':
        name = request.form.get("username")
        password = request.form.get("password")

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("""
                                                 SELECT * FROM admin WHERE id =? AND password =?
                                                 """, (name, password))
        p = c.fetchall()
        if request.form.get('homeb') =='Reset Password':
            return render_template('departmentevaluation.html', form = form)
        if request.form.get('homeb') =='Reset':
            name = request.form.get("username")
            password = request.form.get("password")
            password2 = request.form.get("password2")
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute("UPDATE admin SET password = ? WHERE id = ? AND password = ? ", (password2,name, password))
            conn.commit()
            conn.close()
            return redirect(url_for("views.home"))
        if len(p) == 0:
            flash('Incorrect credentials. Please try again.', 'error')
            return redirect(url_for("views.home"))
        else:
           return redirect(url_for('reports.report'))
    return render_template('home.html')



@reports.route('/reports', methods=['GET', 'POST'])
def report():
    global p
    conn = sqlite3.connect('answers.db')
    c = conn.cursor()
    c.execute("""
        SELECT * FROM answer
        """)
    k = c.fetchall()
    c.execute("""
            SELECT * FROM answ3
            """)
    p = c.fetchall()
    grouped_data = {}
    for entry in k:
        identifier = entry[0]
        if identifier not in grouped_data:
            grouped_data[identifier] = []
        grouped_data[identifier].append(entry[1:])

    conn.commit()
    conn.close()
    if request.form.get('submit') == 'Search':
        username = request.form.get("lecturename").strip()
        unit = request.form.get("unitname").strip()
        conn = sqlite3.connect('answers.db')
        c = conn.cursor()
        c.execute("""
             SELECT * FROM answer2 WHERE id = ? AND unit=? 
             """, (username, unit))
        k = c.fetchall()
        c.execute("""
                    SELECT * FROM answ3 WHERE id = ? AND unit=? 
                    """, (username, unit))
        Z = c.fetchall()

        conn = sqlite3.connect('question.db')
        c = conn.cursor()

        c.execute("""
                                                 SELECT * FROM selectq WHERE unit = ? 
                                             """, (unit,))
        l = c.fetchall()

        c.execute("""

                                   SELECT * FROM radioq WHERE unit=?
                                             """, (unit,))
        j = c.fetchall()
        c.execute("""

                                           SELECT * FROM que5 WHERE unit=?
                                                     """, (unit,))
        x = c.fetchall()
        c.execute("""

                                           SELECT * FROM que6 WHERE unit=?
                                                     """, (unit,))
        t = c.fetchall()

        conn.commit()
        conn.close()

        def count_a(list_of_tuples):
            count = 0
            for tuple in list_of_tuples:
                for element in tuple:
                    if element == l[0][5]:
                        count += 1
            return count

        l1f = count_a(k)

        def count_a(list_of_tuples):
            count = 0
            for tuple in list_of_tuples:
                for element in tuple:
                    if element == l[0][6]:
                        count += 1
            return count

        l2f = count_a(k)

        def count_a(list_of_tuples):
            count = 0
            for tuple in list_of_tuples:
                for element in tuple:
                    if element == l[0][7]:
                        count += 1
            return count

        l3f = count_a(k)

        def count_a(list_of_tuples):
            count = 0
            for tuple in list_of_tuples:
                for element in tuple:
                    if element == l[0][8]:
                        count += 1
            return count

        l4f = count_a(k)

        def count_a(list_of_tuples):
            count = 0
            for tuple in list_of_tuples:
                for element in tuple:
                    if element == j[0][5]:
                        count += 1
            return count

        j1f = count_a(k)

        def count_a(list_of_tuples):
            """Counts the number of `a` in a list of tuples."""
            count = 0
            for tuple in list_of_tuples:
                for element in tuple:
                    if element == j[0][6]:
                        count += 1
            return count

        j2f = count_a(k)

        def count_a(list_of_tuples):
            """Counts the number of `a` in a list of tuples."""
            count = 0
            for tuple in list_of_tuples:
                for element in tuple:
                    if element == j[0][7]:
                        count += 1
            return count

        j3f = count_a(k)

        def count_a(list_of_tuples):
            count = 0
            for tuple in list_of_tuples:
                for element in tuple:
                    if element == x[0][2]:
                        count += 1
            return count

        q51 = count_a(k)
        def count_a(list_of_tuples):
            count = 0
            for tuple in list_of_tuples:
                for element in tuple:
                    if element == x[0][3]:
                        count += 1
            return count

        q52 = count_a(k)
        def count_a(list_of_tuples):
            count = 0
            for tuple in list_of_tuples:
                for element in tuple:
                    if element == x[0][4]:
                        count += 1
            return count

        q53 = count_a(k)
        def count_a(list_of_tuples):
            count = 0
            for tuple in list_of_tuples:
                for element in tuple:
                    if element == x[0][5]:
                        count += 1
            return count

        q54 = count_a(k)
        def count_a(list_of_tuples):
            count = 0
            for tuple in list_of_tuples:
                for element in tuple:
                    if element == t[0][2]:
                        count += 1
            return count

        q61 = count_a(k)
        def count_a(list_of_tuples):
            count = 0
            for tuple in list_of_tuples:
                for element in tuple:
                    if element == t[0][3]:
                        count += 1
            return count

        q62 = count_a(k)

        a1 = [(l1f, l2f, l3f, l4f)]
        a2 = [(j1f, j2f, j3f)]
        q5 =[(q51, q52, q53, q54)]
        q6 = [(q61, q62)]
        if len(k) == 0:
            flash('Record not available. Please try again.', 'error')
            return redirect(url_for("reports.report"))


        return render_template('oldforms.html', answ1=k, j=j, l=l, a1=a1, a2=a2, Z=Z,
                               q5=q5, q6=q6,x=x, t=t,username=username)
    if request.form.get('clear') == 'Clear all Reports':
        conn = sqlite3.connect('answers.db')
        c = conn.cursor()
        c.execute("""
               DELETE FROM answer
               """)
        c.execute("""
                           DELETE FROM answer2
                           """)
        c.execute("""
               DELETE FROM answ3
               """)
        conn.commit()
        conn.close()

    return render_template('reports.html', answ1=k, answ2=p)


@lectures.route('/lectures', methods=['GET', 'POST'])
def lecturer():
    form = myform()
    name = form.p.data
    id = form.p1.data
    department = form.p3.data
    unit1 = form.p6.data
    unit2 = form.p4.data
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("""
       SELECT * FROM lectures
       """)
    o = c.fetchall()
    conn.commit()
    conn.close()
    if request.form.get('add') == 'Add':
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("""
                            INSERT INTO lectures (name, id, department, unit1, unit2)
                            VALUES (?, ?, ?, ?, ?)
                        """, (name, id, department, unit1, unit2))
        conn.commit()
        conn.close()

    elif request.form.get('remove') == 'Remove':
        form = myform()
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("""
               SELECT * FROM lectures
               """)
        z = c.fetchall()
        conn.commit()
        conn.close()
        id = request.form.get("lid").strip()
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("""
               DELETE FROM lectures WHERE id = ?
               """, (id,))
        conn.commit()
        conn.close()

    return render_template('lectures.html', form=form, lectures=o)


@courses.route('/courses', methods=['GET', 'POST'])
def course():
    form = myform()
    conn = sqlite3.connect('question.db')
    c = conn.cursor()
    c.execute("""
            SELECT * FROM textq
            """)
    k = c.fetchall()
    conn.commit()
    conn.close()
    if request.form.get('register') == 'Submit':
        name = form.p5.data
        unit1 = form.p4.data
        conn = sqlite3.connect('question.db')
        c = conn.cursor()

        c.execute("""
                                  INSERT INTO selectq (name, unit)
                                  VALUES (?, ?)
                              """, (name, unit1))

        c.execute("""
                                         INSERT INTO radioq (name, unit)
                                         VALUES (?,?)
                                     """, (name, unit1))

        c.execute("""
                                         INSERT INTO textq (name, unit)
                                         VALUES (?, ?)
                                     """, (name, unit1))
        c.execute("""
                                          INSERT INTO rate ( unit)
                                          VALUES (?)
                                      """, (unit1,))
        c.execute("""
                                          INSERT INTO que5 (unit)
                                          VALUES ( ?)
                                      """, (unit1,))
        c.execute("""
                                          INSERT INTO que6 (unit)
                                          VALUES ( ?)
                                      """, (unit1,))

        conn.commit()
        conn.close()
        return redirect(url_for('forms.create_form'))
    return render_template('courses.html', form=form, k =k)


@students.route('/students', methods=['GET', 'POST'])
def student():
    form = myform()
    stname = form.p.data
    stid = form.p1.data
    stcourse = form.p3.data
    unit2 = form.p4.data
    department = form.p6.data
    password = "kabarak123"
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("""
           SELECT * FROM students
           """)
    o = c.fetchall()
    conn.commit()
    conn.close()
    if request.form.get('add') == 'Add':
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("""
                   SELECT * FROM students
                   """)
        k = c.fetchall()
        conn.commit()
        conn.close()
        form = myform()
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("""
                                INSERT INTO students (name, id,course,  unit1, unit2,password)
                                VALUES (?, ?, ?, ?, ?, ?)
                            """, (stname, stid, stcourse, department, unit2, password))
        conn.commit()
        conn.close()
    if request.form.get('remove') == 'Remove':
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("""
                   SELECT * FROM students
                   """)
        k = c.fetchall()
        conn.commit()
        conn.close()
        form = myform()
        id = request.form.get("sid").strip()
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("""
                                       DELETE FROM students WHERE id =?
                                   """, (id,))
        conn.commit()
        conn.close()
        return render_template('students.html', form=form, students=k)

    else:
        stname = None
    return render_template('students.html', students=o, form=form)


@forms.route('/forms', methods=['GET', 'POST'])
def create_form():
    name = None
    language = None
    radio = None
    form = myform()
    if request.form.get('add') == 'Save form':
        target = form.target.data
        name = form.p.data
        name1 = form.p5.data
        name2 = form.p6.data
        data2 = form.textarea2.data
        data = form.textarea1.data
        form.p.data = ''
        unit = form.lectureunit.data
        sltq = form.textarea3.data
        slt1 = form.p1.data
        slt2 = form.p2.data
        slt3 = form.p3.data
        slt4 = form.p4.data
        que4 = form.que4.data
        que7 = form.que7.data
        que5 = form.que5.data
        q5answ1 = form.q5answ1.data
        q5answ2 = form.q5answ2.data
        q5answ3 = form.q5answ3.data
        q5answ4 = form.q5answ4.data
        que6 = form.que6.data
        q6answ1 = form.q6answ1.data
        q6answ2 = form.q6answ2.data
        conn = sqlite3.connect('question.db')
        c = conn.cursor()
        c.execute("UPDATE textq SET question = ? WHERE unit = ?", (data, unit))

        c.execute(
            "UPDATE radioq SET question = ?, option1 = ?, option2 = ?, option3 = ? WHERE unit= ?",
            (data2, name, name1, name2, unit))

        c.execute("""
                  UPDATE selectq SET question = ?, option1 = ?, option2 = ?, option3 = ?, option4 = ? 
                  WHERE unit = ?""",
                  (sltq, slt1, slt2, slt3, slt4, unit))
        c.execute(
            "UPDATE que5 SET que5 = ?, q5answ1 = ?, q5answ2 = ?, q5answ3 = ?, q5answ4 =? WHERE unit= ?",
            (que5, q5answ1, q5answ2, q5answ3, q5answ4, unit))
        c.execute(
            "UPDATE que6 SET que6 = ?, q6answ1 = ?, q6answ2 = ? WHERE unit= ?",
            (que6, q6answ1, q6answ2, unit))
        c.execute(
            "UPDATE rate SET que4 = ?, que7 =? WHERE unit= ?",
            (que4, que7, unit))

        conn.commit()
        conn.close()

    return render_template('forms.html', name2=name, form=form)

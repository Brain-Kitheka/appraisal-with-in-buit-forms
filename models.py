import sqlite3
import os

queid = "Admin3"
target = "department"
question = "Question"
option1 = "option1"
option2 = "option2"
option3 = "option3"
option4 = "option4"
name = "Admin3"
password = "Admin"
ID = "098"
department = "IT"
unit = "INTE 423"
unit1 = "INTE 423"
unit2 = "INTE 424"
course1 = "Information Technology"
answer = "Not always punctual to class"
q1 = "what is you name"
answ1 = "Brain"
q2 = "what is you school"
answ2 = "Kabarak"
q3 = "what is you Course"
answ3 = "Information technology"


def questionsdb():
    print('you wise')
    if os.path.exists('jjsjdhdhh.db'):
        pass
    else:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("""
                          CREATE TABLE admin(id TEXT,  name TEXT,password TEXT)
       """)
        #c.execute("""
                   #CREATE TABLE answ3(id TEXT, lecturer TEXT, unit TEXT,  que4 TEXT,  answ4 TEXT,  que7 TEXT,  answ7 TEXT, que5 TEXT, answ5 TEXT, que6 TEXT, answ6 TEXT)
                   #""")
       # c.execute("""
                          #CREATE TABLE que6(unit TEXT, que6 TEXT,  q6answ1 TEXT,  q6answ2 TEXT)
                          #""")
       # c.execute("""
                  # CREATE TABLE answer2(id TEXT,  name TEXT,unit  TEXT, sque TEXT,sansw TEXT, rque TEXT, ransw TEXT, tque TEXT,
                   # tansw TEXT)
                  # """)
        #c.execute("""
                   #CREATE TABLE selectq(name TEXT,  id TEXT,department  TEXT, unit TEXT,
             #question TEXT,  option1 TEXT, option2 TEXT, option3 TEXT, option4 TEXT)
                  # """)
        #c.execute("""
                          # CREATE TABLE textq(name TEXT,  id TEXT,department  TEXT, unit TEXT,
                     #question TEXT)
                         #  """)

        conn.commit()
        conn.close()


#questionsdb()


def printr():
    print('men!!')
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("""
                                                     SELECT * FROM admin
                                                     """)
    t = c.fetchall()
    conn.commit()
    conn.close()
    print(t)


printr()
def delete():
    conn = sqlite3.connect('answers.db')
    c = conn.cursor()
    c.execute(""" DELETE FROM answ3
     """)

    conn.commit()
    conn.close()
    print("i done it")
#delete()

def insertdb():
    print("keep going it is your time")
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("""
            INSERT INTO admin (id, name, password)
            VALUES (?, ?, ?)
        """, (queid, name, password))

    conn.commit()
    conn.close()
#insertdb()

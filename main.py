from flask import Flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mdujksjkejedjije'

   
    from views import views, reports, lectures,courses, students, forms

    app.register_blueprint(views, url__prefix='/')
    app.register_blueprint(reports, url__prefix="/reports")
    app.register_blueprint(courses, url__prefix="/courses")
    app.register_blueprint(lectures, url__prefix="/lectures")
    app.register_blueprint(students, url__prefix="/students")
    app.register_blueprint(forms, url__prefix="/forms")

    from studentviews import departmente, view, generale,lecturee, home

    app.register_blueprint(view, url__prefix='/login')
    app.register_blueprint(departmente, url__prefix="/department")
    app.register_blueprint(generale, url__prefix="/general")
    app.register_blueprint(lecturee, url__prefix="/lecturee")
    app.register_blueprint(home, url__prefix="/home")

    return app

app = create_app()
if __name__ =='__main__':
    app.run(debug=True)
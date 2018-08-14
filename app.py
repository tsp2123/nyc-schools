from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__) #this makes a new flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schools.db' #There is a SQLLite database called schools.db 
db = SQLAlchemy(app) #Here we make our database

class School(db.Model): #Here we make our model
  __tablename__ = 'schools' #This code will let SQLAlchemy autodetect our columns
  __table_args__ = {
    'autoload': True,
    'autoload_with': db.engine
  }
  dbn = db.Column(db.String, primary_key=True)



@app.route("/")
def hello():
	schools = School.query.all()
	return render_template("list.html" , schools=schools)

@app.route("/schools/")
def schools():
	schools = School.query.all()
	return render_template("list.html" , schools=schools)


@app.route("/schools/<dbn>/")
def school(dbn):
  school = School.query.filter_by(dbn=dbn).first()
  return render_template("show.html", school=school)

# @app.route("/search")
# def search():
#   name = request.args.get('query')
#   schools = School.query.filter(School.school_name.contains(name)).all()
#   return render_template("list.html", schools=schools)
#If this is running from the command line
# Do something
if __name__ == '__main__':
  app.run(debug=True)
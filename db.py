from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
POSTGRES = {
    'user': 'postgres',
    'pw': 'root',
    'db': 'flask_db',
    'host': 'localhost',
    'port': '5432',
}

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#db.init_app(app)

#app.config(app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost/flask_db")
#'postgresql://postgres:root@localhost/flask_db')
db = SQLAlchemy(app)


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(120), unique=True)
	alias = db.Column(db.String(80))

	def __init__(self, username, email):
		self.username = username
		self.email = email
		self.alias = alias

	def __repr__(self):
		return '<User %r>' % self.username

db.create_all()
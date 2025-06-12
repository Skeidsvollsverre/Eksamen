#alle nødvendige moduler ligger under, husk å installere på forhånd med brew/pip3!
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
#Her intializer du MariaDB databasen
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+pymysql://brukernavn123:123@127.0.0.1/todo'
app.config['SECRET_KEY'] = '123' #Passordet til MariaDB
# Lager en variabel for SQLalchemy
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content=db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

def __repr__(self):
    return '<Task %r>' % self.id
#Routen for selve siden, bruker port 8000
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)



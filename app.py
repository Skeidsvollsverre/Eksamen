#alle nødvendige moduler ligger under, husk å installere på forhånd med brew/pip3!
from flask import Flask, render_template, request, redirect
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
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

#Routen for å legge til tasks, bruker port 8000
#Den henter info fra formen som ligger i index, bruker id for å identifisere
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

#Routen for å slette tasks
#Hvis den ikke møter requirement så for du bare 404 error
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)



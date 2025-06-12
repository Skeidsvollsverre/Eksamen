#alle nødvendige moduler ligger under, husk å installere på forhånd med brew/pip3!
from flask import Flask, render_template, request, redirect
from datetime import datetime
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'

# File to store tasks
TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        tasks = load_tasks()
        
        # Create new task
        new_task = {
            'id': len(tasks) + 1,
            'content': task_content,
            'date_created': datetime.now().strftime('%Y-%m-%d')
        }
        
        tasks.append(new_task)
        save_tasks(tasks)
        return redirect('/')
    else:
        tasks = load_tasks()
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != id]
    save_tasks(tasks)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)



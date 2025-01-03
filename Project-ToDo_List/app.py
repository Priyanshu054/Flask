from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A simple in-memory list to store tasks
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task') # Get task from the input form
    if task:
        tasks.append(task)  # Add task to the list
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)  # Delete task by index
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)

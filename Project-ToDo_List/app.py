from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A simple in-memory list to store tasks
tasks = []

@app.route('/')   # Home route
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])   # Route to add a new task
def add_task():
    task = request.form.get('task') # Get task from the input form
    if task:
        tasks.append(task)  # Add task to the list
    return redirect(url_for('index'))   # Redirect to home route after adding task

@app.route('/delete/<int:task_id>')   # Route to delete a task by its index
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)  # Delete task by index
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    # Run the Flask development server with debugging enabled
    # The server will be accessible on all network interfaces (0.0.0.0) at port 5000

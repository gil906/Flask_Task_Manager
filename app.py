from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create an empty list to store tasks
tasks = []


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    tasks.append(task)
    return redirect(url_for('index'))


@app.route('/delete', methods=['POST'])
def delete():
    task = request.form.get('task')
    tasks.remove(task)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)


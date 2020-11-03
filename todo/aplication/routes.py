from aplication import app, db
from aplication.models import Todo

@app.route('/add')
def add():
    new_todo = Todo(name="New To-do", status = '0')
    db.session.add(new_todo)
    db.session.commit()
    return "Added new to-do to database"

@app.route('/read')
def read():
    all_todo = Todo.query.all()
    todo_string = ""
    for todo in all_todo:
        todo_string += "<br>"+ todo.name
    return todo_string

@app.route('/update/<name>')
def update(name):
    first_todo = Todo.query.first()
    first_todo.name = name
    db.session.commit()
    return first_todo.name

@app.route('/delete/<int:id>')
def delete(id):
    todo_to_delete = Todo.query.get(id)
    db.session.delete(todo_to_delete)
    db.session.commit()
    return "Deleted Task"

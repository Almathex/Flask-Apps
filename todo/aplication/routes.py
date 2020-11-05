from flask import Flask, render_template, redirect, url_for
from aplication import app, db
from aplication.models import ToDo
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from aplication.forms import TodoForm
@app.route('/')
def index():
    return render_template('index.html', todoList = ToDo.query.all())

@app.route('/add', methods=['GET', 'POST'])
def add():
    error = ""
    form = Form()

    if request.method == 'POST':
        task = form.task.data
        l

        if len(first_name) == 0:
            error = "Please supply a task."
        else:
            return 'thank you'
    db.session.add(form)
    db.session.commit()
    return render_template('index.html', form=form, message=error)

@app.route('/complete/<idNum>')
def complete(idNum):
    task= ToDo.query.get(idNum)
    task.complete=1
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/incomplete/<idNum>')
def incomplete(idNum):
    task= ToDo.query.get(idNum)
    task.complete=0
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<idNum>/<newTask>')
def update(idNum,newTask):
    task= ToDo.query.get(idNum)
    task.task=newTask
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<idNum>')
def delete(idNum):
    task_1= ToDo.query.get(idNum)
    db.session.delete(task_1)
    db.session.commit()
    return redirect(url_for('index'))

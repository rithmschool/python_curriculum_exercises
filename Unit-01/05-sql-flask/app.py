from flask import Flask, request, redirect, url_for, render_template
from flask_modus import Modus
from db import find_all_snacks, create_snack, remove_snack, edit_snack, find_snack

app = Flask(__name__)
modus = Modus(app)

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/snacks', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        create_snack(request.form['name'], request.form['kind'])
        return redirect(url_for('index'))
    return render_template('index.html', snacks=find_all_snacks())

@app.route('/snacks/new')
def new():
    return render_template('new.html')

@app.route('/snacks/<int:id>/edit')
def edit(id):
    found_snack = find_snack(id)
    return render_template('edit.html', snack=found_snack)

@app.route('/snacks/<int:id>', methods = ["GET", "PATCH", "DELETE"])
def show(id):
    if request.method == 'PATCH':
        edit_snack(request.form['name'], request.form['kind'], id)
        return redirect(url_for('index'))
    if request.method == 'DELETE':
        remove_snack(id)
        return redirect(url_for('index'))
    return render_template('show.html', snack=find_snack(id))

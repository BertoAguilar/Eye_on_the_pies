from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import user, pie
from flask_app.models.pie import Pie

@app.route('/create/pie', methods=['POST'])
def create_pie():
    if not Pie.validate_pie(request.form):
        return redirect('/dashboard')
    data = {
        'users_id': session['user_id'],
        'name': request.form['name'],
        'filling': request.form['filling'],
        'crust': request.form['crust']
    }
    pie.Pie.save(data)
    return redirect('/dashboard')

@app.route('/pies/<int:id>')
def view_pie(id):
    return render_template("view.html")

@app.route('/delete/pies/<int:id>')
def destroy_pie(id):
    pie.Pie.destroy_pie(id)
    return redirect('/dashboard')
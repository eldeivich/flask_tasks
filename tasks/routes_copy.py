from tasks import app
from flask import render_template, request, url_for, redirect

import csv

@app.route("/")
def index():
    if request.method == 'GET':
        <leer tareas en fichero .data/tareas.dat
        return render_template("index.html", tareas)

@app.route("/newtask", methods['GET', 'POST'])
def newtask():
    if request.method == 'GET':
        return render_template('task.html')


    fdatos = open('./data/tareas.dat', 'w')
    csvwriter = csv.writer(fdatos, delimiter=",", quotechar='"')

    title = request.values.get('title')
    desc = request.values.get('desc')
    date = request.values.get('date')

    print('method:', request.method)
    print('parametros:', request.values)

    csvwriter.writerow([title, desc, date])

    fdatos.close
    return redirect(url_for("index"))

    



    '''
    recuperar parametros
    abrir fichero
    añadir registros
    devolver respuesta todo correcto
    '''
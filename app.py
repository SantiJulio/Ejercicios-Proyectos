from datetime import datetime,time,date, timedelta
from flask import Flask, request, render_template,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import Trabajador, Registrohorario

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/registro_entrada', methods = ['POST','GET'])
def registrar_entrada():
    if request.method == 'POST':
        legajo = request.form['legajo']
        dni = request.form['dni4']
        dependencia = request.form['dependencia']

        if not dni or not legajo or not dependencia:
            return render_template('error.html', error = 'Ingrese todos los datos')

        existe = Trabajador.query.filter(Trabajador.dni.like(f"%{dni}"), Trabajador.legajo == legajo).first()
        if existe:
            buscarentrada = Registrohorario.query.filter(Registrohorario.idtrabajador == existe.id, Registrohorario.fecha == datetime.now().date(), Registrohorario.horasalida == None).first()
            if not buscarentrada:
                nuevoregistro = Registrohorario(fecha = datetime.now().date(), horaentrada = datetime.now().time().replace(microsecond=0), horasalida = None, idtrabajador = existe.id, dependencia = dependencia)
                db.session.add(nuevoregistro)
                db.session.commit()
                return render_template('aviso.html',mensaje = 'Entrada registrada con exito!')
            else:
                return render_template('aviso.html',mensaje = 'El trabajador todavia no registra su salida!')
        else:
            return render_template('error.html',error = 'El trabajador no esta registrado en la pagina!')
    else:
        return render_template('registro_entrada.html')

###registro_existente_entrada = Registrohorario.query.filter_by(
###    idtrabajador=trabajador.id,
###    fecha=date.today()
###).first()

###if registro_existente_entrada and registro_existente_entrada.horasalida is None:
###    flash("Ya tiene una entrada registrada hoy y no registró la salida.")
###    return redirect(url_for('registrar_entrada'))

@app.route('/registrar_salida', methods=['POST', 'GET'])
def registrar_salida():
    if request.method == 'POST':
        legajo = request.form['legajo']
        dni = request.form['dni4']

        if not dni or not legajo:
            return render_template('error.html', error='Ingrese todos los datos')

        existe = Trabajador.query.filter(Trabajador.dni.like(f"%{dni}"), Trabajador.legajo == legajo).first()
        if existe:
            buscarentrada = Registrohorario.query.filter(Registrohorario.idtrabajador == existe.id, Registrohorario.fecha == datetime.now().date(), Registrohorario.horasalida == None).first()
            
            if buscarentrada:
                return render_template('confirmar_salida.html', trabajador=existe, registro=buscarentrada)
            else:
                return render_template('aviso.html', mensaje='El trabajador no registró su entrada hoy o ya registró la salida.')
        else:
            return render_template('error.html', error='El trabajador no está registrado en la página.')
    else:
        return render_template('registrar_salida.html')

@app.route('/confirmar_salida', methods=['POST'])
def confirmar_salida():
    registro_id = request.form.get('registro_id')

    if not registro_id:
        return render_template('error.html', error='No se recibió ID de registro.')

    registro = Registrohorario.query.get(registro_id)

    if not registro:
        return render_template('error.html', error='Registro no encontrado.')

    if registro.horasalida is not None:
        return render_template('aviso.html', mensaje='La salida ya fue registrada.')

    registro.horasalida = datetime.now().time().replace(microsecond=0)
    db.session.commit()
    return render_template('aviso.html', mensaje='Salida registrada con éxito.')

@app.route('/consultar_registros', methods=['GET', 'POST'])
def consultar_registros():
    if request.method == 'POST':
        legajo = request.form['legajo']
        dni = request.form['dni4']
        fecha_inicio = request.form['fecha_inicio']
        fecha_fin = request.form['fecha_fin']

        if not legajo or not dni or not fecha_inicio or not fecha_fin:
            return render_template('error.html', error="Todos los campos son obligatorios.")

        trabajador = Trabajador.query.filter(Trabajador.legajo == legajo, Trabajador.dni.like(f"%{dni}")).first()
        if not trabajador:
            return render_template('error.html', error="Trabajador no encontrado.")

        registros = Registrohorario.query.filter(Registrohorario.idtrabajador == trabajador.id, Registrohorario.fecha >= fecha_inicio, Registrohorario.fecha <= fecha_fin).order_by(Registrohorario.fecha.asc()).all()

        if not registros:
            return render_template('aviso.html', mensaje="No se encontraron registros en el período indicado.")

        return render_template('mostrar_registros.html', trabajador=trabajador, registros=registros)

    return render_template('consultar_registros.html')

from datetime import datetime, timedelta

@app.route('/informe_general', methods=['GET', 'POST'])
def informe_general():
    if request.method == 'POST':
        legajo = request.form['legajo']
        dni = request.form['dni4']
        fecha_inicio = request.form['fecha_inicio']
        fecha_fin = request.form['fecha_fin']
        funcion = request.form['funcion']
        dependencia = request.form['dependencia']

        admin = Trabajador.query.filter(Trabajador.legajo == legajo, Trabajador.dni.like(f"%{dni}"), Trabajador.funcion == 'AD').first()

        if not admin:
            return render_template('error.html', error="No tiene permisos para acceder a este informe.")

        filtros = [Registrohorario.fecha >= fecha_inicio, Registrohorario.fecha <= fecha_fin]

        if funcion != 'TODOS':
            filtros.append(Trabajador.funcion == funcion)
        if dependencia != 'TODOS':
            filtros.append(Registrohorario.dependencia == dependencia)

        registros = db.session.query(Registrohorario).join(Trabajador).filter(*filtros).order_by(Trabajador.apellido.asc()).all()

        for r in registros:
            if r.horaentrada and r.horasalida:
                entrada = datetime.combine(r.fecha, r.horaentrada)
                salida = datetime.combine(r.fecha, r.horasalida)
                r.horas_trabajadas = (salida - entrada).seconds // 3600
            else:
                r.horas_trabajadas = None

        return render_template('mostrar_informe_general.html', registros=registros)

    return render_template('informe_general.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
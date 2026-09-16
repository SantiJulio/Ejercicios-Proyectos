import os
from datetime import datetime
from flask import Flask, current_app, render_template, request, session, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = Flask(__name__) 
app.config.from_pyfile('config.py')

# Configuración para la subida de archivos
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

from modelo import db, Trabajo, Evaluador, Organizador#LAS IMPORTACIONES DE MODELOS DEBEN IR AQUÍ ABAJO (Luego de crear 'app') 

from gestor import gestorCongreso 
GC = gestorCongreso()

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/enviar_trabajo', methods=['GET', 'POST'])
def enviar_trabajo():
    if request.method == 'POST':
        if (not request.form['titulo'] or not request.form['resumen'] or not request.form['areaTrabajo'] or not request.form['apellido'] or not request.form['nombre'] or not request.form['correoAutor'] or 'archivo' not in request.files):
            resultado = render_template('aviso.html', mensaje="Los Datos se Ingresaron de forma incorrecta...")
        else:
            titulo = request.form['titulo']
            resumen = request.form['resumen']
            areaT = request.form['areaTrabajo']
            apellido = request.form['apellido']
            nombre = request.form['nombre']
            correo = request.form['correoAutor']
            
            # Procesamos el archivo subido
            file = request.files['archivo']
            if file.filename == '':
                return render_template('aviso.html', mensaje="No se seleccionó ningún archivo...")
            
            # Limpiamos el nombre del archivo para que sea seguro
            nombre_archivo = secure_filename(file.filename)
            # Guardamos el archivo físicamente en la carpeta 'uploads'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], nombre_archivo))
            
            nuevosDatos = GC.registrarUsuario(titulo, resumen, areaT, apellido, nombre, correo, nombre_archivo)
            resultado = render_template('aviso.html', mensaje=f"Se registró el trabajo correctamente. Su Número asignado es el {nuevosDatos}!")
    else: 
        resultado = render_template('enviar_trabajo.html')
    return resultado 

@app.route('/consultar_trabajo', methods = ['GET','POST'])
def consultar_trabajo():
    if request.method == 'POST':
        if not request.form['id_trabajo'] or not request.form['correoAutor']:
            resultado = render_template('aviso.html',mensaje = "Los Datos se Ingresaron de forma incorrecta...")
        else:
            idT = request.form['id_trabajo']
            correo = request.form['correoAutor']
            encontrado = GC.buscarxIDyCorreo(idT,correo)
        if encontrado:
            resultado = render_template('consultar_trabajo.html', trabajo = encontrado)
        else:
            resultado = render_template('aviso.html', mensaje = "No se encontro ningun trabajo con los datos ingresados. ")
    else:
        resultado = render_template('consultar_trabajo.html')
    return resultado

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        rol = request.form['rol']
        correo = request.form['correo']
        clave = request.form['clave']
        
        if rol == 'organizador':
            usuario = GC.autenticarOrganizador(correo, clave)
        else:
            usuario = GC.autenticarEvaluador(correo, clave)
            
        if usuario:
            # Guardamos los datos clave en la sesión de Flask
            session['usuario_id'] = usuario.id
            session['usuario_rol'] = rol
            return render_template('aviso.html', mensaje=f"¡Bienvenido/a {usuario.nombre}! Has ingresado como {rol.capitalize()}.")
        else:
            return render_template('aviso.html', mensaje="Credenciales incorrectas o rol no coincidente.")
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear() # Limpia toda la sesión
    return render_template('aviso.html', mensaje="Sesión cerrada correctamente.")

@app.route('/ejecutar_procesoA', methods = ['GET','POST'])
def ejecutar_procesoA():
    if request.method == 'POST':
        cantAsignaciones = GC.asignarEvaluadoresAutomatico()
        if cantAsignaciones > 0:
            men = f"Proceso completado con exito. Se ha generado {cantAsignaciones} nuevas asignaciones de evaluacion."
        else:
            men = "El proceso finalizo correctamente, pero no se encontraron trabajos pendientes que cumplan con los requisitos de asignacion o cupos disponibles."
        return render_template('aviso.html', mensaje=men)
    else:
        resultado = render_template('ejecutar_procesoA.html')
    return resultado

@app.route('/bandeja_entrada', methods=['GET'])
def bandeja_entrada():
    if session.get('usuario_rol') == 'evaluador':
        evaluador_id = session.get('usuario_id')
        
        # Traemos el objeto Evaluador completo usando su ID
        evaluador_logueado = Evaluador.query.get(evaluador_id)
       
        # Extraemos sus asignaciones directamente desde el objeto evaluador
        asignaciones = evaluador_logueado.asignaciones       
        return render_template('bandeja_entrada.html', evaluador_logueado=evaluador_logueado, asignaciones=asignaciones)
    else:
        return render_template('aviso.html', mensaje="Acceso denegado.")

@app.route('/descargar/<filename>')
def descargar_archivo(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':     
    with app.app_context():   
        GC.crearBD()       
    app.run(debug=True)                      
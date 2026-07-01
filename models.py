from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Trabajador(db.Model):
    __tablename__ = 'trabajador'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    dni = db.Column(db.String(8), unique=True, nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    legajo = db.Column(db.String(20), unique=True, nullable=False)
    horas = db.Column(db.Integer, nullable=False)
    funcion = db.Column(db.String(90), nullable=True)
    registrohorario = db.relationship('Registrohorario', backref='trabajador', cascade="all, delete-orphan")

class Registrohorario(db.Model):
    __tablename__ = 'registrohorario'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    horaentrada = db.Column(db.Time, nullable=False)
    horasalida = db.Column(db.Time, nullable=True)
    dependencia = db.Column(db.String(80), nullable=False)
    idtrabajador = db.Column(db.Integer, db.ForeignKey('trabajador.id'))
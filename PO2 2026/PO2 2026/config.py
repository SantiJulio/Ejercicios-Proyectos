SECRET_KEY = "POO-ES-LA-MEJOR" #se usa en ciertas operaciones que requieren seguridad
SQLALCHEMY_DATABASE_URI = 'sqlite:///datos.sqlite3' #indica el nombre del archivo que contiene la base de datos
SQLACHMEMY_TRACK_MODIFICATIONS = False # esta carateristica rastrea las modificaciones de los objetos y emite señales, debe dejase en False debido a q requiere memoria adicional
from flask import Flask, render_template
from db import db

class programa:

    def __init__(self):

        self.app= Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///estudiantes.sqlite3" #conectar y/o crear a una base de datos

        self.app.add_url_rule('/nuevo', view_func=self.agregar) #Crear una ruta y su funcionalidad

        #Iniciar el servidor 
        with self.app_context():   #Busca los recursos disponibles para la aplicacion
            db.create_all()        #"Llamar" a la base de datos

        self.app.run(debug=True)


    def agregar(self):            #Agregar una funcionalidad
        return render_template('nuevoEstudiante.html')   #Construir una respuesta a partir de un objeto HTML





miprograma= programa()
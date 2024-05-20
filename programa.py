from flask import Flask, render_template, request, redirect, url_for
from db import db
from Estudiantes import Estudiante

class programa:

    def __init__(self):

        self.app= Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///estudiantes.sqlite3" #conectar y/o crear a una base de datos

        #Agregar el db a la aplicacion
        db.init_app(self.app)

        self.app.add_url_rule('/', view_func=self.buscarTodos)
        self.app.add_url_rule('/nuevo', view_func=self.agregar, methods=["GET", "POST"]) #Crear una ruta y su funcionalidad

        #Iniciar el servidor 
        with self.app.app_context():   #Busca los recursos disponibles para la aplicacion
            db.create_all()        #"Llamar" a la base de datos
            self.app.run(debug=True)

    def buscarTodos(self):

        return "TO DO: Tengo que buscar los registros de la tabla"

    def agregar(self):            #Agregar una funcionalidad

        #Verificar si debe enviar el formulario o procesar los datos

        if request.method=="POST":  #Procesar los datos que vienen del formulario
            
        #Crear un objeto de la clase estudiante con los valores del formulario
            nombre=request.form['nombre']
            email=request.form['email']
            codigo=request.form['codigo']
            miEstudiante= Estudiante(nombre, email, codigo)

        #Guardar el objeto en la base de datos db
            db.session.add(miEstudiante)
            db.session.commit()

            return redirect(url_for('buscarTodos'))



        return render_template('nuevoEstudiante.html')   #Construir una respuesta a partir de un objeto HTML





miprograma= programa()
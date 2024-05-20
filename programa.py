from flask import Flask, render_template

class programa:

    def __init__(self):

        self.app= Flask(__name__)

        self.app.add_url_rule('/nuevo', view_func=self.agregar) #Crear una ruta y su funcionalidad

        #Iniciar el servidor 
        self.app.run(debug=True)


    def agregar(self):            #Agregar una funcionalidad
        return render_template('nuevoEstudiante.html')   #Construir una respuesta a partir de un objeto HTML





miprograma= programa()
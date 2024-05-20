from flask import Flask

class programa:

    def __init__(self):

        self.app= Flask(__name__)

        self.app.add_url_rule('/nuevo', view_func=self.agregar) #Crear una ruta y su funcionalidad

        #Iniciar el servidor 
        self.app.run(debug=True)


    def agregar(self):            #Agregar una funcionalidad
        return "Hola mundo Flask"





miprograma= programa()
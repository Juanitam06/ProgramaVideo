
from db import db

#Definir un modelo

class Estudiante(db.Model): 

    #Nombre de tabla

    __tablename__="Estudiante"

    #Conjunto de atributos, campos de la tabla

#Toda tabla debe tener una "llave primaria" y debe ser un valor unico de preferencia un entero
    id=db.Column(db.Integer, primary_key=True)

    nombre=db.Column(db.String(50)) #Permite dar el nombre y tipo de dato de la columna
    email=db.Column(db.String(70))
    codigo=db.Column(db.String(15))

    #Metodo constructor para mapear datos a los campos definidos

    def __init__(self, nombre, email, codigo):

        self.nombre=nombre
        self.email=email
        self.codigo=codigo 
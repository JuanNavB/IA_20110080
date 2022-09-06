class Persona:                              #Se crea la clase

    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def p_data(self):                       #Se define una funcion
        print("Nombre: ", self.nombre, "\nApellidos: ", self.apellidos)#Se imprimen los resultados

class PersonasAvanzadas(Persona):#Herencia de la clase persona
    pass#Salta la clase ya que esta vacia

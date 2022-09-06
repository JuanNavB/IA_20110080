class Persona:                              #Se crea la clase

    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def p_data(self):                       #Se define una funcion
        print("Nombre: ", self.nombre, "\nApellidos: ", self.apellidos)#Se imprimen los resultados

class PersonasAvanzadas(Persona):#Herencia de la clase persona
    def __init__(self, nombre, apellidos, instagram):# se define el init
        self.nombre = nombre        #Se le da valor a los tributos
        self.apellidos = apellidos
        self.instagram = instagram

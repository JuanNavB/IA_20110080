class Persona:                              #Se crea la clase

    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def p_data(self):                       #Se define una funcion
        print("Nombre: ", self.nombre, "\nApellidos: ", self.apellidos)#Se imprimen los resultados

u001 = Persona("Juan de Dios", "Navarro Bedoy")#Se agregan los atributos
u002 = Persona("Argenis", "Cuellar")#Se agregan los atributos


u002.nombre = "Jose"        #Se les da nuevos valores a los atributos
del u001.nombre             #se borra el atributo del objeto
    
u001.p_data()                       #Se le da un valor a la funcion

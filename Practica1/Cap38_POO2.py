

class Usuario:#se crea la calse
	def __init__(self, nombre, apellidos):#se define la funcion
	    self.nombre = nombre                #Se le añade el valor a los objetos
    self.apellidos = apellidos

	def imprime_datos(self):    #Se define la funcion para imprimir
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)#Print de la funcion imprimir

usuario001 = Usuario('Enrique', 'Barros Fernández')#Se añaden valores para los self

usuario002 = Usuario('Javier', 'Gomila Reyes')
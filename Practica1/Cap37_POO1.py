class Persona:                              #Se crea la clase
    nombre = ""                             #Se añaden atributos
    apellidos = ""

    def p_data(self):                       #Se define una funcion
        print("Nombre: ", self.nombre, "\nApellidos: ", self.apellidos)#Se imprimen los resultados

u001 = Persona()#Se agregan los atributos

u001.nombre = "Juan de Dios"        #Se les da valores a los atributos
u001.apellidos = "Navarro Bedoy"    
u001.p_data()                       #Se le da un valor a la funcion


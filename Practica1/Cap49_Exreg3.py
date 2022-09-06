import re #Se importa la libreria
texto = "Bienvenidos a Programación fácil"#Se asigna el rexto
busqueda = re.split("a", texto)#Se selecciona el elemento para buscar
print(busqueda)#Se imprime la funcion
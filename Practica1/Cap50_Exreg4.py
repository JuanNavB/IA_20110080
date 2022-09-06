import re #Se importa la libreria
texto = "¿Quieres pizza?"#Se asigna el rexto
busqueda = re.findall("y", texto)#Se selecciona el elemento para buscar

if busqueda:                                    #se crea un if que evalua coincidencias
    print("Hay por lo menos una coincidencia")  #Se imprime el resultado
else:                                           #else del if
    print("No se enccontró ninguna funcion")    #Se imprime el resultado del if

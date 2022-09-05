from queue import PriorityQueue


vehiculos = {                       #creacion de el diccionario
	'Categoria': 'Pick up',
	'Modelo': 'Ford Raptor',
	'Precio': '65,000.00'
}

vehiculos2 = {                       #creacion de el diccionario
	'Categoria': 'Pick up',
	'Modelo': 'Ford Lobo',
	'Precio': '45,000.00'
}

del vehiculos2                      #Eliminacion del diccionario vehiculos 2
del vehiculos['Categoria']          #Eliminacion del elemento categoria
del vehiculos['Precio']             #Eliminacion del elemento precio

print(vehiculos['Modelo'])          #Impresion del modelo

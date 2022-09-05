vehiculos = {                       #creacion de el diccionario
	'Categoría': 'Pick up',
	'Modelo': 'Ford Raptor',
	'Precio': '65,000.00'
}
con = vehiculos['Modelo']           #Consulta del modelo
con2 = vehiculos['Precio']          #Consulta del precio

print("El " + con + " tiene un costo de: " + con2 + " dlls.")   #Impresion del precio y modelo

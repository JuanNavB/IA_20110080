edad = int(input('¿Cuál es tu edad?\n'))#se crea la variable de entrada edad

if edad <= 0:                               #se analiza el primer condicional
	print('Nadie puede tener esa edad.')    #se imprime resultado

elif edad <= 1 and edad < 18:               #se analiza el segundo condicional
	print('Eres menor de edad.')            #se imprime resultado

elif edad >= 18 and edad <=45:              #se analiza el tercer condicional
    print("Tienes entre 18 y 45 anios")     #se imprime resultado

elif edad > 100 and edad <=120:             #se analiza el cuarto condicional
    print("Tienes entre 100 y 120 anios")   #se imprime resultado

elif edad <= 100:                           #se analiza el quinto condicional
	print('Eres mayor de edad.')            #se imprime resultado

else:                                       #se analiza el else
	print('Edad no válida.')                #se imprime resultado
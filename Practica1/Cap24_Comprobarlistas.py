colors = input("Ingresa un color: \n")          #Se crea la variable de entrada colors
t_colors = ('rojo', 'azul', 'verde', 'amarillo')#se crea la tupla

if colors in t_colors[0]:                       #Condicional para el color "rojo"
    print("El color se encuentra en la tupla")

if colors in t_colors[1]:                       #Condicional para el color "azul"
    print("El color se encuentra en la tupla")

if colors in t_colors[2]:                       #Condicional para el color "verde"
    print("El color se encuentra en la tupla")

if colors in t_colors[3]:                       #Condicional para el color "amarillo"
    print("El color se encuentra en la tupla")

else:                                           #Fin de los condicinales y evaluacion de else
    print("No se encontro el color en la tupla.")
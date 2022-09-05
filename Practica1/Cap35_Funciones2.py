from ast import arg 


def pizza(*args): #Definicion de la funcion
    print("La pizza de ", args[0], " es mi favorita, aunque la pizza de ", args[1], " tambien es deliciosa.") #impresion del resultado

pizza("peperoni", "queso")#implementacion de los argumentos
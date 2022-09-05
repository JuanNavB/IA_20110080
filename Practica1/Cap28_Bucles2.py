x = 0                                                                   #se incia x en 0

while x <= 30:                                                          #bucle while empieza de 0 a 30
    x += 1                                                              #se fija el incremento

    if x == 4 or x == 6 or x == 10:                                     #Condicional para 4, 6, 10
        print("Se saltó el valor: ", x, "que pertenece a x.")           #Impresion del condicional

    if x == 15:                                                         #Condicional del break
        print("Se quebró la ejecución cuando x tenia valor de: ", x)    #impresion del break
        break                                                           #Punto de quiebre de la ejecucion
print(x)                                                                #impresion de x


import datetime # importa datetime

ahora = datetime.datetime.now()#Se crea la variable donde se alamacenará la funcion

print(ahora.strftime("Día de la semana abreviado: %a ")) #Se imprimen los resultados de la funcion
print(ahora.strftime("Día de la semana completo: %A "))#Se imprimen los resultados de la funcion
print(ahora.strftime("Mes abreviado: %b "))#Se imprimen los resultados de la funcion
print(ahora.strftime("Mes abreviado: %B "))#Se imprimen los resultados de la funcion
print(ahora.strftime("Fecha completa: %c "))#Se imprimen los resultados de la funcion
print(ahora.strftime("Siglo (empieza a contar desde cero): %C "))#Se imprimen los resultados de la funcion
print(ahora.strftime("Día del mes (01 - 31): %d "))#Se imprimen los resultados de la funcion
print(ahora.strftime("Día/hora/año: %D "))#Se imprimen los resultados de la funcion
print(ahora.strftime("Día del mes (1 - 31): %e "))#Se imprimen los resultados de la funcion
print(ahora.strftime("Año en dos dígitos: %g "))#Se imprimen los resultados de la funcion
print(ahora.strftime("Año en cuatro dígitos: %G "))#Se imprimen los resultados de la funcion
print(ahora.strftime("Mes abreviado: %h "))#Se imprimen los resultados de la funcion
print(ahora.strftime("Hora (00 - 23): %H "))#Se imprimen los resultados de la funcion
print(ahora.strftime("Hora (01 - 12): %I "))#Se imprimen los resultados de la funcion
print(ahora.strftime("Día del año: %j "))#Se imprimen los resultados de la funcion
print(ahora.strftime("Mes del 01 al 12: %m "))#Se imprimen los resultados de la funcion
print(ahora.strftime("Minuto: %M "))#Se imprimen los resultados de la funcion
print(ahora.strftime("Salto de línea: %n"))#Se imprimen los resultados de la funcion
print(ahora.strftime("AM o PM: %p "))#Se imprimen los resultados de la funcion
print(ahora.strftime("Hora + AM o PM: %r"))#Se imprimen los resultados de la funcion
print(ahora.strftime("Hora y minutos: %R"))#Se imprimen los resultados de la funcion
print(ahora.strftime("Segundos: %S"))#Se imprimen los resultados de la funcion
print(ahora.strftime("Tabulación: %t"))#Se imprimen los resultados de la funcion
print(ahora.strftime("Hora, minutos y segundos: %T"))#Se imprimen los resultados de la funcion
print(ahora.strftime("Día de la semana (número): %u"))#Se imprimen los resultados de la funcion
print(ahora.strftime("Semana del año (empieza en domingo): %U"))#Se imprimen los resultados de la funcion
print(ahora.strftime("Semana del año(Condiciones especiales): %V"))#Se imprimen los resultados de la funcion
print(ahora.strftime("Semana del año (empieza en lunes): %W"))#Se imprimen los resultados de la funcion
print(ahora.strftime("Día de la semana (empieza en domingo): %w"))#Se imprimen los resultados de la funcion
print(ahora.strftime("Día/mes/año de dos dígitos: %x"))#Se imprimen los resultados de la funcion
print(ahora.strftime("Hora/minutos/segundos: %X"))#Se imprimen los resultados de la funcion
print(ahora.strftime("Año corto: %y"))#Se imprimen los resultados de la funcion
print(ahora.strftime("Año largo: %Y"))#Se imprimen los resultados de la funcion
#1 leer dos numeros y los imprima de forma ascendente
# num1 = input("ingrese el num1")
# num2 = input("ingrese el num2")

# if type(num1) and type(num2) == "int":

#     if num1 < num2:
#         print(num1)
#         print(num2)
#     elif num2 < num1:
#         print(num2)
#         print(num1)
#     else:
#         print('los numeros son iguales')
# else: 
#     print('ingreso letras')
#------------------------------------------------------------------

#2 Determinar la cantidad total a pagar por una llamada telefonica, teniendo en cuenta lo siguiente:
#  - toda llamada que dure tres minutos o menos tiene un costo de 200 pesos
#  - cada minuto adicional a partir de los tres primeros es un paso de contador y cuesta 100 pesos
# print('recuerde que despues de pasado un segundo se cobra el minuto')
# tiempo =input("escriba el tiempo de la llamada")
# a = 200
# b = 100

# if type (tiempo) == "int":
#     if tiempo <= 3:
#         print(' el valor de la llamada es :', a)

#     else:
#         tiempo > 3
#         total = a+(tiempo - 3)* b
#         print(' el valor total de la llamada es :', total)
# else:
# print('Por favor ingrese solo numeros enteros para saber el costo de la llamada')
#----------------------------------------------------------------------------

#3 En una Granja existen N conejos, C1 blancos y C2 negros. Se venden X conejos negros y Y conejos blancos. Hacer un algoritmo que:
# Imprima la cantidad de conejos vendida
# Si P1 es el precio de venta de los conejos blancos y P2 es el precio de venta de los conejos negros, imprima el monto total de la venta.
#Imprima el color de los conejos que se vendieron más.
# Conejos = ("Digite la cantidad de conejos")
# ConejosB= input("digite la cantidad de conejos blancos vendidos")
# ConejosN= input("digite la cantidad de conejos negros vendidos")
# precioB = input("precio de los conejos blancos")
# precioN = input("precio de los conejos negros")

# conejosV = int(ConejosB) + int(ConejosN)
# VentaCB = int(ConejosB) * int(precioB)
# VentaCN = int(ConejosN) * int(precioN)
# VentaTotal= int(VentaCB) + int(VentaCN)
# if type(ConejosB) =="int" and type(ConejosN) =="int" and type(precioB) =="int"  and type(precioN) == "int":
    
# print('la cantidad de conejos vendida es:', conejosV)


#-----------------------------------------------------------------------
#4 Diseñe un algoritmo que permita calcular la nota definitiva para los estudiantes, determinadas sobre las siguientes condiciones:
#• NOTA PREVIOS será el promedio de los previos por el 60%. Cada estudiante tendrá 3 evaluaciones.
#• NOTA TRABAJOS será el promedio de los trabajos por el 40%. Cada estudiante presentara 2 trabajos.
#• NOTA FINAL será la suma de la nota de los previos y nota de los trabajos.
#• Nota mínima 1,0 nota máxima: 5,0
# print("inngrese la nota de sus tres evaluaciones")
# examen1 = float(input("digite su nota1"))
# examen2 = float(input("digite su nota2"))
# examen3 = float(input("digite su nota3"))
# notadeparciales = ((examen1*20/100) + (examen2*20/100) + (examen3*20/100))
# print('la nota de parciales es:', notadeparciales)
# print("ingrese la nota de sus dos trabajos")
# trab1 = float(input("digite su nota de trabajo1"))
# trab2 = float(input("digite su nota de trabajo2"))
# notadetrabajos = ((trab1*20/100) + (trab2*20/100))
# print('la nota de trabajos es:', notadetrabajos)
# notafinal = (notadeparciales + notadetrabajos)
# print('la nota final es:', notafinal)
#---------------------------------------------------------------------------------------

#5 Hacer un algoritmo que imprima el nombre de un artículo, clave, precio original,cantidad y su precio con descuento. 
#El descuento lo hace en base a la clave, si laclave es 1 el descuento es del 10% y si la clave es 2 el descuento es del 20% (solo
#existen dos claves).
# producto = ("ingrese el nombre del producto")
# clave = int(input("digite la clave"))
# precio = float(input("ingrese el precio"))
# cantidad = int(input("digite la cantidad"))

# if clave == 1:
#      descuento = cantidad * (precio * 0.1)
# else:
#     clave == 2
#     descuento = cantidad * (precio * 0.2)
# print('el nombre del prodcto es:', producto)
# print('la clave es:', clave)
# print('el precio original:', precio)
# print()




#6 Diseñar un algoritmo que lea por teclado un número comprendido entre 1 y 10. Se desea visualizar si el número es par o impar. En primer
#lugar, se deberá detectar si el número está comprendido en el rango válido (1 a 10) y a continuación
#si el número es 1, 3, 5, 7, 9, escribir un mensaje de “impar”; si es 2, 4, 6, 8, 10, escribir
#un mensaje de “par”.

try:

    numero = input("digite un numero del 1 al 10")

    match numero:
        case '1,3,5,7,9':
            print('el numero es impar')
        case '2,4,6,8,10':
            print('el numero es par')
except:
    print('el numero no esta en el rango de 1 a 10')
    

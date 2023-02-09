#Variables y Datos

#entrada y salida de datos


#letras
"""
name = input("Ingrese el nombre: ") 

#numereo entero
numberOne = int(input("Ingrese Numero: ")) 

#numero decimal
numberTwo = float(input("Ingrese Numero: ")) 

#suma
num1 = int(input("ingrese el primer numero: "))   
num2 = int(input("ingrese el segundo numero: "))
suma = num1 + num2 

#mostrar la información
print("El resultado de la suma es: ", suma)"""

#unir 
#print("hola", "grupo", "Desarrollo de Software", sep="+", end="\n") 

#concatenar
"""Nombre = "Karina "
Apellido = "Valencia"
#nombre_y_apellido = Nombre + Apellido #asi sale pegadas las palabras
#nombre_y_apellido = Nombre + ' ' + Apellido # asi sale con el espacio
nombre_y_apellido = Nombre + Apellido 
print(nombre_y_apellido)"""
#para separar las palabras funciona tambien dejando espacio en la palabra

#METODOS title(), upper(), lower()

#title coloca la primer letra de cada palabra en mayuscula
"""modulo =  "nuevas tecnologias de programacion"
modulo = modulo.title() 
print(modulo)"""

#upper coloca toda la palabra en mayuscula
"""modulo =  "nuevas tecnologias de programacion"
modulo = modulo.upper() 
print(modulo)"""

#lower coloca toda la palabra en minuscula
"""modulo =  "NUEVAS tecnologias de programacion"
modulo = modulo.lower() 
print(modulo)"""


#DIVIDIR STRING

#conocer numero de caracteres incluidos los espacios
"""frase = "El que no vino perdio el examen de GIT"
print(len(frase))"""

#imprime desde el caracter que indique siempre menos 1
"""frase = "El que no vino perdio el examen de GIT"
print(frase[0:20])"""

#float round

"""decimal_1 = 3.1543
decimal_2 = 45.895432548
resultado = decimal_1+decimal_2
print(round(resultado, 2))""" # el 2 es la cantidad de decimales, sin el 2 sale entero

#tabular y saltos de linea

#saltos de linea \n
#para que salga una linea por variable
"""a = "Lenguajes de programación
b = "Python"
c = "Java"
d = "HTML"
print(a)"""

#otra forma de colocar la linea independiente
"""print("Programas:\nPython\nJava\nHTML")"""

#Tabular \t cada \t es un espacio
print("""
seleccione una opcion:\n
\t1. suma
\t2. resta
\t3. division
\t4. raiz cuadrada
""")


txt = "¡hola! "
operacion = txt*4
print(operacion)



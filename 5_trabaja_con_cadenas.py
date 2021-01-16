#5

#TRABAJA CON CADENAS DE TEXTO #STRINGS

# Las cadenas pueden ser tratadas como listas
cadena = "Hola Estudiante"

# H o l a   E s t u d i  a  n  t  e
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14

letra = cadena [5]
print (letra) # E

letra2 = cadena [-5] # i iría hacia atrás desde la última posición que sería -1

letras = cadena [5:15] #Estudiante ; hay que poner una posición más porque imprime hasta la anterior seleccionada
print (letras)

# cadena [5] = "B" ; daría error porque a diferencia de las listas, las cadenas no se pueden mutar


# FUNCIONES DE CADENAS DE TEXTO
# Utilizar documentación para ver todos los comandos https://docs.python.org/3/library/index.html

# Algunos ejemplos:

modificada = cadena.capitalize() #primera mayúscula y resto en minúsculas
print (modificada)

modificada2 = cadena.upper() # todo en mayúscula
print (modificada2)

separando_terminos = cadena.split() #Nos separa cada término con espacios
print (separando_terminos)

cadena_con_comas = "Juan,Jose,Pedro,Marcos"
lista_nombres = cadena_con_comas.split(',') #indicamos que queremos que separe donde está la coma
print (lista_nombres)


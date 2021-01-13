#4.4

# OPERADORES LÓGICOS Y DE PERTENENCIA

# OPERADORES LÓGICOS
# Son aquellos que nos permiten comprobar se se cumplen comparaciones lógicas
# normalmente se hace con valores booleanos, pero python lo hace con otro tipo de datos

"""
or -> a or b -> ¿SE CUMPLE ALGUNA DE LAS DOS? ¿A o B? ; Solo será falso si ambos son falsos
and -> a and b -> ¿Se cumplen las dos? ¿Se cumplen a y b?; Solo será verdadero si ambos son verdaderos
not -> not x -> No se cumple x (contrario de x)
"""

verdadero = True
falso = False

print (verdadero or falso) #True
print (verdadero and falso) #False
print (not verdadero) #False
print (not falso) #True

print (verdadero and 0) #0
print (verdadero or 0) #True


# OPERADORES DE PERTENENCIA
# Son aquellos que evaluan si un objeto se encuentra dentro del otro

"""
in - > se encuentra en

not in -> no se encuentra en

"""

cadena = "Hola Mundo"

print ('z'in cadena) #False
print ('a'in cadena) #True
#3

# Tipos de datos: "NUMERICOS" y "CADENAS". Tambien cosideraremos los "BOOLEANOS"

# type (variable) nos da los datos de dicha variable. Ejemplo: si entero = 10 ; type (entero) = "int"
# id (variable) indica la posición memoria de dicha variable

# NUMÉRICOS
# Enteros (int) números sin comas
entero = 10

# Flotantes (float) números con comas, decimales
flotante = 10.05


# Complejos (complex)
complejo = (10.05+0j)


# Podemos jugar con los valores ej:

entero = 10
flotante = 10.05
complejo = (10.05 + 0j)

int (flotante) # convierte en entero un valor flotante
float (entero) # convierte en flotante un valor entero
complex (entero) # convierte en complejo un valor entero

# BOOLEANOS (bool)

verdadero = True
falso = False

int (True) #1
float (True) #1.0
int (False) #0
float (False) # 0.0

bool (0) #False
# bool (cualquier otro numero) = True



# CADENAS DE TEXTO

cadena = "Hola Mundo" #cadena está definida con str

type (cadena) # str

print (cadena)
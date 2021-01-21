# LISTAS
# Una lista es una colección de elementos. Las listas están ordenadas y son mutables.

compra = ["leche", "arroz", "fruta", "pan", "cereales","huevos"] # tenemos 6 ítems, pero empieza desde 0; 0-5; se llama número de índice

print (compra) #vemos toda la compra
print (compra[1]) # vemos el item 1, es decir el segundo, arroz
print (compra[0]) #leche
print (compra[-1]) # vamos hacia atrás ; es igual que el item 5, huevos
print (compra [2:5]) # imprimirá desde el item 3 hasta el anterior a 5 (CUIDADO CON ESTO): fruta, pan, cereales
print (compra [:4]) # imprimirá desde el principio hasta el anteroir al 4
print (compra [2:]) # imprimirá desde el segundo hasta el último


# FUNCIONES DE LAS LISTAS
# list, len, append, extend, insert, remove, clear, pop, index, count, sort, reverse, copy ... usemos la documentación!!!

saludos = list (("hola", "adios", "hasta_luego", "nos_vemos")) #otra forma de hacer una lista
print (saludos) # imprime la lista
print (len(saludos) , len(compra)) # nos imprime el numero de elementos de la lista
saludos.append("hasta_nunca") # añadimos elemento a la lista
print (saludos)
# saludos [1] = "holita" ; permite cambiar elementos, en este caso el 1 ("adios")

# Agregar listas
lista_completa = compra + saludos
print (lista_completa)

compra.extend(saludos) #de esta manera extendemos la lista compra con la de saludos
print (compra)

compra.insert (2, "yogures" ) # nos permite añadir un elemento en el índice seleccionado (posición)
print (compra)

compra.remove ("yogures") # eliminando un ítem de la lista
print (compra)

compra.pop() # elimina el ultimo item de la lista
print (compra)

print (compra.index ("pan")) # nos da el índice del item

print (compra.count("pan")) # te dice el número de veces que dicho item está en la lista

compra.sort() #ordena la lista en orden alfabético / de mayor a menor

print(compra)

compra2 = compra.copy() # nos permite copiar la lista con sus atributos en una VARIABLE DIFERENTE con ID diferente!
# Es la diferencia con simplemente igualarlo compra2 = compra
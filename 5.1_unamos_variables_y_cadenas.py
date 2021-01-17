#5.1

#Unamos ahora variables y cadenas y observemos el resultado

trabajadores = 2700
empresa = "Remotech"

#cadena = "Los 2700 trabajadores de la empresa Remotech recibiran paga extraordinaria"
# En este caso podemos concatenar las variables así:

#cadena = "Los" + trabajadores + "trabajadores de la empresa" + empresa + "recibiran paga extraordinaria"

#print (cadena) # da error y nos dice que no se pueden concatenar números enteros

# Para solventar este error convertimos la variable en cadena

cadena = "Los " + str(trabajadores) + " trabajadores de la empresa " + empresa + " recibiran paga extraordinaria" #no olvidamos añadir los espacios
print (cadena)

# .format es muy práctico. Evitamos tener que transformar la variable numerica a cadena. Observa

cadena = "Los {} trabajadores de la empresa {} recibiran paga extraordinaria".format(trabajadores, empresa)
print (cadena)


cadena = "Los {a} trabajadores de la empresa {b} recibiran paga extraordinaria".format(a=trabajadores, b=empresa)
print (cadena)

cadena = f"Los {trabajadores} trabajadores de la empresa {empresa} recibirán paga extraordinaria"
print (cadena)


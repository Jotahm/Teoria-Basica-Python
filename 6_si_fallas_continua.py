# SI ENCUENTRAS UN ERROR, CONTINÚA
# Por lo general, python no continúa al encontrar algún fallo. Habrá ocasiones en las que nos interese que si lo haga.

saludo = "Hola amigo"

try: # utilizamos este comando para la operación que vemos propensa a fallar
    operacion = int (saludo) # Intentamos hacer este texto "un entero" (fallará)

except: # creamos esta excepción para la operación que indica que nos devuelva un "-1" si esta falla.
    operacion = -1

print ("Primera operación" , operacion) # nos devuelve el código -1 con lo cual nos dice "la operación ha fallado"

print ("He llegado hasta aquí a pesar de que fallase la operación")
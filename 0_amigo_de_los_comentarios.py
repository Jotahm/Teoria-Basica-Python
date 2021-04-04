#0
# ACOSTUMBRATE A USAR LOS COMENTARIOS
# Permiten hacer mucho más facil la lectura de código
# Sobre todo si lo lee otra persona que no somos nosotros mismos
# Ejemplo del buen uso de comentarios: Aclaraciones


# Definimos nuestras variables:
numero1 = 10
numero2 = 20
numero1, numero2 = 10, 20 # Ahorramos una linea de codigo haciendo asignación múltiple

suma = numero1 + numero2 # Sumamos ambas variables

# Imprimimos el resultado en pantalla:
print (suma)

"""
Para hacer largos comentarios (sobre todo que utilicen varias lineas, utilizamos las triples comillas

Aprovechamos para enumerar los 12 mandamientos de Python:

1. Los nombres de los módulos deben estar en minúsculas (por ej., hola.py).

2. Los nombres de las clases deben usar CamelCase.

3. Los métodos y funciones deben usar minusculas_con_guion_bajo. # También es válido deEstaManera.

4. Los métodos privados para uso interno comienzan con _guion_bajo.

5. Los atributos de clase con __doble_guion_bajo.

6. Las constantes en el primer nivel del código (las que no se encuentran dentro de una función o una clase) 
deben usar LETRASMAYUSCULAS. Usar demasiadas constantes puede hacer que tu código sea menos reutilizable.

7. Si una variable en una función o método es tan temporal que no puedes darle un nombre, utiliza i para 
la primera, j para la segunda, y k para la tercera.

8. Indenta con cuatro espacios por nivel. Sin tabuladores. Si rompes este mandamiento serás lapidado en la 
plaza del pueblo.

9. Las líneas no deberían tener nunca más de 80 caracteres. Divide las líneas usando una barra invertida.
 No necesitas hacer esto si hay paréntesis, llaves o corchetes.

10. Espacio después de una coma (huevos, verdes, con, jamon).

11. Espacio antes y después de un operador (i = i + 1).

12. Escribe cadenas de documentación para todos los módulos, funciones, clases y métodos públicos. 
Python es una comunidad internacional, así que utiliza el inglés para las cadenas de documentación,
 los nombres de los objetos y los comentarios.
"""

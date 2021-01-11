#4.2

# Los operadores de relación son aquellos que evalúan si dos valores cumplen alguna condición

"""
Estos operadores preguntan si los valores son:
== Igual a
!= Distinto de
> Mayor que
< Menor que
>= Mayor o igual que
<= Menor o igual que
"""

numero1 = 10
numero2 = 5
numero3 = 10.0
numero4 = -10
numero5 = 5

igual = numero1 == numero2
print (igual) # como resultado nos dice False

igual2 = numero2 == numero5
print (igual2)

igual3 = numero1 == numero3
print (igual3)

distinto = numero1 != numero2
print (distinto)

distinto1 = numero1 != numero3
print (distinto1)

mayor_que = numero1 > numero3
print (mayor_que)

menor_que = numero1 < numero4
print (menor_que)

menor_igual_que = numero1 <= numero2
print (menor_igual_que)

mayor_igual_que = numero1 >= numero2
print (mayor_igual_que)
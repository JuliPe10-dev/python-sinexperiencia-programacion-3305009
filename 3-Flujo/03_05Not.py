'''
    NOT es un operador lógico que se utiliza para invertir el valor de una condición.
    Si la condición es verdadera, NOT la convierte en falsa, y si es falsa, la convierte en verdadera.
    La tabla de verdad del operador NOT es la siguiente:
    |A      | NOT A
    |True   | False
    |False  | True
'''

puerta_abierta = True
dia = True
dia_soleado = False

if not puerta_abierta:
    print("La puerta esta abierta")


if not dia:
    print("Es de día")
'''
    A pesar de que los ejemplos de la clase dicen que para que la puerta esté abierta, la variable puerta_abierta debe ser False,
    puede llegar a ser confuso, la mejor forma es pensar en que Not es una validacion contraria al caso, es decir
    Si la puerta no esta cerrada (false), entonces que el if not tenga el mensaje de que "se debe cerrar la puerta"
    para que cuando uno lea el codigo se lea de forma natural Si la puerta NO esta abierta, la accion es cerrarla.
'''
if not dia_soleado:
    print("No es un día soleado")


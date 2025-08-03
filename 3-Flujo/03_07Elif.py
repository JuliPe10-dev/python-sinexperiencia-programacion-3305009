'''
    El elif es una forma de simplificar el uso de múltiples if anidados.
    este es como decir, Si A no es verdadera, entonces verifica que B sea verdadera.
    Si B es verdadera, entonces ejecuta el bloque de código asociado a B.
    Si B no es verdadera, entonces verifica C, y así sucesivamente.
    Si ninguna de las condiciones es verdadera, se ejecuta el bloque de código del else.
'''

numero = int(input("Ingresar un número: "))
# Usando if anidados
if numero > 0:
    print("El número es positivo")
else:
    if numero == 0:
        print("El número es igual a 0")
    else:
        print("El número es negativo")

# Usando elif para simplificar el código
if numero > 0:
   print("El número es positivo")
elif numero == 0:
    print("El número es igual a 0")
else:
    print("El número es negativo")

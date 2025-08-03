'''
    El If es un Si ... Si algo es cierto, entonces haz algo
    Es una estructura de control que permite ejecutar un bloque de código si una condición es verdadera.
    En Python, se utiliza la palabra clave 'if' para iniciar una declaración condicional.
    El codigo que esta indentado debajo del if se ejecuta solo si la condición es verdadera.

    En este caso, si la luz está encendida, se imprime un mensaje.
'''

luz_encendida = False

if luz_encendida:
    print("La luz está encendida")
    print(f"El valor de la varible luz_encendida es {luz_encendida}")

pc_encendido = True

if pc_encendido:
    print("Mi computadora está encendida")

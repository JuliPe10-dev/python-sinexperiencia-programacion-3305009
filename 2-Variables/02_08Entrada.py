
'''
  En este ejercicio es para usar las entradas de datos
'''
# Valores predefinidos para la suma
numero_1 = 5
numero_2 = 10

resultado_suma = numero_1 + numero_2
print(f"El resultado de la suma es: {resultado_suma}")

# input permite al usuario ingresar datos desde la consola
# y devuelve el valor ingresado como una cadena de texto
numero_1 = input("Ingresar número uno: ")

numero_2 = input("Ingresar número dos: ")

# Convertimos las entradas a enteros antes de sumarlas
resultado_suma = int(numero_1) + int(numero_2)

print(f"El resultado de la suma es: {resultado_suma}")

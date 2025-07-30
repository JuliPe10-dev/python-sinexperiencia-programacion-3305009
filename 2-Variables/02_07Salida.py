'''
  En este ejercicio se muestra cómo imprimir texto y variables en pantalla.
  Se pueden usar diferentes métodos para formatear el texto.
'''

# Imprimir texto simple
print("¡Hola mundo!")

# Imprimir una variable
edad = 32
print(edad)

# Imprimir texto y variables juntos usando comas (,)
nombre = "Ana"
print("Mi nombre es",nombre,"y tengo",edad,"años de edad.")

# Imprimir texto y variables usando el método format
print("Mi nombre es {} y tengo {} años de edad.".format(nombre, edad))

# Imprimir texto y variables usando f-strings  
print(f"Mi nombre es {nombre} y tengo {edad} años de edad.")

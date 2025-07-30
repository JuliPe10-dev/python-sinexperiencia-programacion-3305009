'''
  Aqui tenemos diferentes funciones que nos permiten manipular
  cadenas de texto (strings) y verificar ciertas propiedades de ellas.
'''
# Asignamos una frase a una variable para los ejercicios
frase = "La programación es el arte de crear soluciones con código"

# Len nos permite saber la longitud de la cadena de texto
largo = len(frase)
print("La longitud de la frase es: {}".format(largo))

# upper convierte la cadena a mayúsculas
frase_mayuscula = frase.upper()
print(frase_mayuscula)

# lower convierte la cadena a minúsculas
frase_minuscula = frase.lower()
print(frase_minuscula)

# replace nos permite reemplazar un texto por otro en donde el primer 
# texto es lo que se busca y el segundo texto es lo que se va a poner en su lugar
nueva_frase = frase.replace("crear soluciones", "resolver problemas")
print(nueva_frase)

# split separa la cadena en un lista de palabras usando un determinador
# en este caso el espacio " " y da como resultado una lista
frase_espacios = frase.split(" ")
print(frase_espacios) 

# find me da la posición de la primera aparición de un texto dentro de la cadena
# si no lo encuentra devuelve -1 y empieza a contar desde 0
posicion = frase.find("programación")
print(posicion)

# isdigit verifica si todos los caracteres de la cadena son dígitos
numero_texto = "23"
is_digit = numero_texto.isdigit()
print(is_digit) 




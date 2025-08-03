'''
    Otro operador logico es el OR (o) que nos dice que si al menos una de las condiciones es verdadera, entonces el resultado es verdadero.
    Si ambas condiciones son falsas, entonces el resultado es falso.
    La tabla de verdad del operador OR es la siguiente:
    |A      | B       | A or B
    |True   | True    | True
    |True   | False   | True
    |False  | True    | True
    |False  | False   | False
'''

video_juego = 'Mario Bros'
leer = False
pelicula = False
visitar_parque = True

if video_juego == 'La era de los imperios' or leer == True or pelicula == True or visitar_parque == True:
    print('Estoy feliz con mi pasatiempo')
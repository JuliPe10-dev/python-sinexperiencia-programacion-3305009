
'''
    En la programación existe los operadores logicos que nos permite evaluar multiples condiciones al "mismo tiempo".
    En este caso veremos en AND (y) en donde nos dice que si la primera condicion es verdadera y la segunda también, entonces este par de condiciones es verdadero.
    Si alguna de las dos condiciones es falsa, entonces el resultado es falso.

    La tabla de verdad del operador AND es la siguiente:
    |A      | B       | A and B
    |True   | True    | True
    |True   | False   | False
    |False  | True    | False
    |False  | False   | False

'''
edad = 18
prueba_teorica = 80
prueba_practica = True
dictamen_medico = True
infracciones = True

if edad >= 18 and prueba_teorica >= 80 and prueba_practica == True and dictamen_medico == True and infracciones != True:
    print("Obtuviste la licencia de conducir")
else:
    print("Lo sentimos, no cumplieste con algunos de nuestros requerimientos")
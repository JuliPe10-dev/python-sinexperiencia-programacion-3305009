'''
OPERADORES DE COMPARACIÓN
Los operadores de comparación se utilizan para comparar dos valores y devolver un valor booleano (True o False) según el resultado de la comparación.
> : mayor que
< : menor que
>= : mayor o igual que
<= : menor o igual que
!= : diferente de
== : igual a
'''

# Signo >
a = 4
b = 6
resultado = a > b
print(f"a > b {resultado}")

# Signo <
a = 4
b = 6
resultado = a < b
print(f"a < b {resultado}")

# Signo >=
a = 6
b = 6
resultado = a >= b
print(f"a >= b {resultado}")

# Signo <=
a = 5
b = 6
resultado = a <= b
print(f"a <= b {resultado}")

# Signo ==
a = 5
b = 6
resultado = a == b
print(f"a == b {resultado}")

# Signo !=
a = 5
b = 6
resultado = a != b
print(f"a != b {resultado}")

# IF
a = 50
if a > 0:
    print("A es un número positivo.")

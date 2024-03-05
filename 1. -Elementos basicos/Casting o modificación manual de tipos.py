#Se puede modificar el tipo de dato de una variable
#Para ello se utilizan las funciones de Python: str, int, float, bool

cadena = "Esto es una cadena"
entero = 10
decimal = 10.1
booleano = True
print("Casting de int a str")
print(entero)
print (str(entero))         # Conversión del valor 10 a la cadena "10"
print("----------------------")
print("Casting de float a int")
print(decimal)
print (int(decimal))        # Conversión de float a int, con truncado de decimales
print("----------------------")
print("Casting de bool a float")
print(booleano)
print (float(booleano))     # Conversión de booleanos a valores numéricos 0 y 1
print("----------------------")
print("Casting de str a float. No funciona")
print(cadena)
print (float(cadena))       # Conversión no válida de una cadena a un número decimal
#Prueba
def hola_mundo():
    pass
    print("Hola mundo")

hola_mundo()

#Funcion con parametro
def imprimir_nombre(nombre):
    pass
    print("Hola", nombre)

imprimir_nombre("Miguel")

#Funcion con parametro por default
def imprimir_edad(edad=18):
    pass
    print("Tu edad es:",edad)
    
imprimir_edad()

#Funcion con retorno de valor
def suma(a=10, b=2):
    pass
    return a+b
print("El resultado de la suma es:",suma())

def resta(a=3, b=2):
    pass
    return a-b
print("El resultado de la resta es:",resta())

def multi(a=4, b=5):
    pass
    return a*b
print("El resultado de la multiplicacion es:",multi())

def operacion(a=5, b=10):
    pass
    return (a*a)-b
print("El resultado de la operación es:",operacion())

print("hola")
#los F strings
nombre="posk"
saludo=f"Soy {nombre}"
print(saludo)
#operadores de pertenencia (in / not in)
print("juan" in saludo)
print("juan" not in saludo)
#variables con CamelCase y snake_case
nombreCompleto="PP"
nombre_completo="pp"
#listas multi-tipo
lista=["posky",12,13.5,True]
#tuplas (no se pueden modificar)
tupla=("posky",12,13.5,True)
#conjuntos(set) (no se pueden modificar pero pueden alterar el orden)(tampoco puedo acceder por indice) (no muestra repetidos)
conjunto={"posky",12,13.5,True}
#diccionarios(dict) (par key value)
diccionario= {
    'edad':20,
    'pais':"argentina"
}
# operadores aritmeticos
a=6
b=3
#exponencial
c=a**b
#division baja (devuelve el entero de la div) (la division sola, devuelve un float) (redondea hacia abajo)
d= a//b
#el else if aqui es elif
if c==d:
    print("iguales")
elif c!=d:
    print("distintos")
#and & or |
#metodos de cadena SIEMPRE VA EL DATO.METODO()
#type(ver tipo de dato)
#dir(devuelve la lista de atributos validos del objeto pasado)
#upper(mayus)
#lower(minus)
# capitalize(primera en mayus)
# find(encuentra valor.sino devuelve 1)
# index(devuelve el indice del valor.sino devuelve excepcion)
# isnumeric
# isalpha
# count
# len
# endswith(cadena termina con)
# startswith(cena termina con)
# replace(valor por otro)
# split(separa por parametro)
#metodos diccionario:
#keys(devuelve las claves)
#get(devuelve valor de clave)
#clear(elimina todos los elementos)
#pop(elimina un elemento)
#items(itera el dict)
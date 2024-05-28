
import random
#Crea una funcion para crear una lista de numeros aleatorios
def listaAleatorios(n):
    lista = [random.randint(1, 1000) for _ in range(n)]
    return lista
#Crea un diccionario que tomara valores de la lista y lo elevara al cuadrado
def generar_diccionario_cuadrados(lista):
    #i+1 para que el indice se inicialice en 1
    diccionario = {i + 1: lista[i] ** 2 for i in range(len(lista))}
    return diccionario

#Obtener el número de elementos aleatorios
n = int(input("Ingrese cuántos números aleatorios desea obtener: "))
#Generar la lista de números aleatorios
numeros_aleatorios = listaAleatorios(n)

#Generar el diccionario de cuadrados
diccionario_cuadrados = generar_diccionario_cuadrados(numeros_aleatorios)

#Imprimir la lista de aleatorios
print("Lista de números aleatorios:")
print(numeros_aleatorios)

#Imprimir el diccionario de cuadrados
print("Diccionario de cuadrados:")
#Prueba
print(diccionario_cuadrados)
#intera por el indice (clave) e imprime el elemento (valor) al cuadrado del numero con la funcion diccionario_cuadrados.items()
for clave, valor in diccionario_cuadrados.items():
    #f para hacer en es formato
    print(f"{clave}: {valor}")


#Donde tome ayuda: https://parzibyte.me/blog/2020/05/15/lista-aleatoria-python/
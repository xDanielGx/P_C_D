#Hacer un diccionario de frutas ya guardada
frutas ={
    'manzana': 2.5,
    'banana': 1.8,
    'pera': 2.0,
    'uva': 3.0,
    'naranja': 4.0
}
#Funcion para obtener el precio final de la fruta solicitada
def precio_fruta(fruta, cantidad):
    if fruta in frutas:
        precio_unitario= frutas[fruta]
        precio_total = precio_unitario*cantidad
        return precio_total
    else:
        return "Error, la fruta no se encuentra en la lista"
#Crea un ciclo para la fruta
while True:
    #Se menciona las frutas
    print("manzana, banana, pera, uva, naranja")
    #Ingresar los parametros de lo que necesita
    nombre_fruta= input("Dame el nombre de la fruta: ").lower()
    cantidad_fruta = int(input("¿Cuantas frutas quieres? "))
    #Llamar a fucion precio_fruta
    precio_final = precio_fruta(nombre_fruta, cantidad_fruta)
    print("El precio final de la fruta ", nombre_fruta, "es ", precio_final)
    #Preguntar si quiere continuar
    continuar = input("¿Deseas continuar (s/n)").lower
    if continuar != "s":
        break
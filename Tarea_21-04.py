#Creamos un diccionario para almacenar las tablas de datos
tablas = {}

def crear_tabla():
    nombre_tabla = input("Ingrese el nombre para la nueva tabla: ")
    
    if nombre_tabla in tablas:
        print("Ya existe una tabla con ese nombre.")
    else:
        tablas[nombre_tabla] = [[], []]

def agregar_persona():
    nombre_tabla = input("Ingrese el nombre de la tabla donde desea agregar los datos: ")
    
    if nombre_tabla not in tablas:    #Verifica si la tabla existe
        print("La tabla especificada no existe. Por favor, cree la tabla primero.")
        return
    else:
        nombre = input("Ingrese el nombre de la persona: ")
        identificacion = input("Ingrese la identificación de la persona: ")
    
        tablas[nombre_tabla][0].append(nombre)
        tablas[nombre_tabla][1].append(identificacion)

#Pedimos al usuario que decida qué acción desea realizar
while True:
    print("\n-------------------------------------------------------------------------------------------------")
    print("\n¿Qué desea hacer?")
    print("1. Crear una nueva tabla")
    print("2. Agregar una persona a una tabla existente")
    print("3. Mostrar todas las tablas y sus datos")
    print("4. Salir")
    print("\n-------------------------------------------------------------------------------------------------")
    opcion = input("Ingrese el número de la opción deseada: ")
    
    if opcion == '1':
        crear_tabla()
    elif opcion == '2':
        agregar_persona()
    elif opcion == '3':
        print("\nTablas y sus datos:")
        for nombre_tabla in tablas:
            tabla = tablas[nombre_tabla]
            print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
            print(f"\nTabla: {nombre_tabla}")
            for i in range(len(tabla[0])):
                print("Nombre:", tabla[0][i])
                print("Identificación:", tabla[1][i])
                print()
            print("\n.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
            input("Presione Enter para continuar...")
    elif opcion == '4':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número válido.")
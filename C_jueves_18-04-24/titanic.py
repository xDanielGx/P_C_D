#Libreria necesaria
import pandas as pd
#cargar los datos desde la direccion
data_frame = ('titanic.csv')
titanic_df=pd.read_csv(data_frame)
#Imprimir los datos para verificar si cargo correctamente
print(titanic_df.head)

#Imprimos los datos de diferentes maneras
#La informacion, los 10 primeros y los 10 ultimos.
print("----------------------------------------------------------------")
print("\nDescibre los dimensiones de los datos de la data frame")
print(titanic_df.info())
print("\nDescibre los 10 primeros datos de la data frame")
print(titanic_df.head(10))
print("\nDescibre los 10 ultimos datos de la data frame")
print(titanic_df.tail(10))

#Funcion para llamar solamente los valores del pasajero con id 148
print("----------------------------------------------------------------")
print("\nNos proporciona los datos del pasajero con el id 148")
print(titanic_df.loc[147])

#Llamar las columna con indice pares
print("----------------------------------------------------------------")
print("\nNos permite visualizar las columnas con indices pares")
print(titanic_df[titanic_df.index % 2 == 0])

#llamamos los valores de la primera clase
print("----------------------------------------------------------------")
print("\nNos permite visualizar la informacion de la primera clase")
print(titanic_df[titanic_df['Pclass'] == 1]['Name'].sort_values())

#Obtenemos los porcentaje de los que sobrivivieron y los que no
print("----------------------------------------------------------------")
print("\nObtenemos los procentajes de los sobrevientes")
print('Porcentaje de personas que sobrevivieron:', round(titanic_df['Survived'].mean() * 100, 2), '%')
print('Porcentaje de personas que murieron:', round((1 - titanic_df['Survived'].mean()) * 100, 2), '%')

#Obtenemos los porcentajes de los sobrevientes de diferentes clases, mediante la media(mean)
print("----------------------------------------------------------------")
print("\nObtenemos los procentajes de los sobrevientes de diferentes clases")
print('Porcentaje de personas que sobrevivieron en primera clase:', round(titanic_df[titanic_df['Pclass'] == 1]['Survived'].mean() * 100, 2), '%')
print('Porcentaje de personas que sobrevivieron en segunda clase:', round(titanic_df[titanic_df['Pclass'] == 2]['Survived'].mean() * 100, 2), '%')
print('Porcentaje de personas que sobrevivieron en tercera clase:', round(titanic_df[titanic_df['Pclass'] == 3]['Survived'].mean() * 100, 2), '%')

print("----------------------------------------------------------------")
print("\nEliminamos la edades desconocidas e imprimir la edad media de las mujeres.")
#Eliminar del DataFrame los pasajeros con edad desconocida
titanic_df = titanic_df.dropna(subset=['Age'])
#Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase
print('Edad media de las mujeres que viajaban en primera clase:', round(titanic_df[(titanic_df['Sex'] == 'female') & (titanic_df['Pclass'] == 1)]['Age'].mean(), 2))
print('Edad media de las mujeres que viajaban en segunda clase:', round(titanic_df[(titanic_df['Sex'] == 'female') & (titanic_df['Pclass'] == 2)]['Age'].mean(), 2))
print('Edad media de las mujeres que viajaban en tercera clase:', round(titanic_df[(titanic_df['Sex'] == 'female') & (titanic_df['Pclass'] == 3)]['Age'].mean(), 2))

print("----------------------------------------------------------------")
print("\nHacemos una variable para validar la edad y sacamos el porcentaje si se cumple.")
#Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no
titanic_df['EsMenor'] = titanic_df['Age'] < 18
#Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase
print('Porcentaje de menores que sobrevivieron en primera clase:', round(titanic_df[(titanic_df['Pclass'] == 1) & (titanic_df['EsMenor'] == True)]['Survived'].mean() * 100, 2), '%')
print('Porcentaje de mayores de edad que sobrevivieron en primera clase:', round(titanic_df[(titanic_df['Pclass'] == 1) & (titanic_df['EsMenor'] == False)]['Survived'].mean() * 100, 2), '%')
print('Porcentaje de menores que sobrevivieron en segunda clase:', round(titanic_df[(titanic_df['Pclass'] == 2) & (titanic_df['EsMenor'] == True)]['Survived'].mean() * 100, 2), '%')
print('Porcentaje de mayores de edad que sobrevivieron en segunda clase:', round(titanic_df[(titanic_df['Pclass'] == 2) & (titanic_df['EsMenor'] == False)]['Survived'].mean() * 100, 2), '%')
print('Porcentaje de menores que sobrevivieron en tercera clase:', round(titanic_df[(titanic_df['Pclass'] == 3) & (titanic_df['EsMenor'] == True)]['Survived'].mean() * 100, 2), '%')
print('Porcentaje de mayores de edad que sobrevivieron en tercera clase:', round(titanic_df[(titanic_df['Pclass'] == 3) & (titanic_df['EsMenor'] == False)]['Survived'].mean() * 100, 2), '%')
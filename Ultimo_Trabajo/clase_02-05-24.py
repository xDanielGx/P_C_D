#%%      #Permite visualizar las graficas en una terminal alterna
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]
#plt.plot(yield_apples)
#plt.show()
# %%
years =[2010, 2011, 2012, 2013, 2014, 2015]
yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]
plt.plot(years, yield_apples)
plt.xlabel('Año')
plt.ylabel('Rendimiento (toneladas por hectarea)')
# %%
years = range(2000, 2012)
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]
plt.plot(years, apples)
plt.plot(years, oranges)
plt.xlabel('Año')
plt.ylabel('Rendimiento (toneladas por hectárea)');
# %%
years = range(2000, 2012)
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]
plt.plot(years, apples)
plt.plot(years, oranges)
plt.xlabel('Año')
plt.ylabel('Rendimiento (toneladas por hectárea)')
plt.title("Rendimiento de los campos en Baja California")    #Muestra el titulo de la grafica
plt.legend(['Manzanas', 'Naranjas'])    #Muestra etiquetas sobre los temas que se especifica
# %%
years = range(2000, 2012)
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]
plt.plot(years, apples, marker='o')
plt.plot(years, oranges, marker='x')
plt.xlabel('Año')
plt.ylabel('Rendimiento (toneladas por hectárea)');
plt.title("Rendimiento de los campos en Baja")    
plt.legend(["Manzana", "Naranja"])
# %%
years = range(2000, 2012)
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]
#Se modifica los diseños, los colores, el tamaño de los datos graficados
plt.plot(years, apples, marker='s', c='b', ls='--', lw=2, ms=10, mew=2, mec='navy')
plt.plot(years, oranges, marker='o', c='r', ls='--', lw=3, ms=10, alpha=.5)
plt.xlabel('Año')
plt.ylabel('Rendimiento (toneladas por hectárea)');
plt.title("Rendimiento de los campos en Baja California")
plt.legend(['Manzanas', 'Naranjas'])
# %%
#Otra manera de ver los cambios de colores
years = range(2000, 2012)
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]
fmt = 's-b'
plt.plot(years, apples, fmt);
plt.plot(years, oranges, 'o--r');
plt.xlabel('Año')
plt.ylabel('Rendimiento (toneladas por hectárea)');
plt.title("Rendimiento de los campos en Baja California")
plt.legend(['Manzanas', 'Naranjas'])
# %%
years = range(2000, 2012)
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]
plt.figure(figsize=(12, 6))    #Modifica el tamaño de la visualizacion de la grafica
sns.set_style("whitegrid")    #Cambia los diseños mediante los diferentes formatos
fmt = 's-b'
plt.plot(years, apples, fmt);
plt.plot(years, oranges, 'o--r');
plt.xlabel('Año')
plt.ylabel('Rendimiento (toneladas por hectárea)');
plt.title("Rendimiento de los campos en Baja California")
plt.legend(['Manzanas', 'Naranjas'])
# %%
years = range(2000, 2012)
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]
plt.figure(figsize=(12, 6))    #Modifica el tamaño de la visualizacion de la grafica
sns.set_style("darkgrid")
fmt = 's-b'
plt.plot(years, apples, fmt);
plt.plot(years, oranges, 'o--r');
plt.xlabel('Año')
plt.ylabel('Rendimiento (toneladas por hectárea)');
plt.title("Rendimiento de los campos en Baja California")
plt.legend(['Manzanas', 'Naranjas'])
# %%
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

years = range(2000, 2012)
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]
plt.figure(figsize=(12, 6))
matplotlib.rcParams['font.size'] = 10
matplotlib.rcParams['figure.figsize'] = (15, 8)
matplotlib.rcParams['figure.facecolor'] = '#00000000'
sns.set_style("darkgrid")
fmt = 's-b'
plt.plot(years, apples, fmt);
plt.plot(years, oranges, 'o--r');
plt.xlabel('Año')
plt.ylabel('Rendimiento (toneladas por hectárea)');
plt.title("Rendimiento de los campos en Baja California")
plt.legend(['Manzanas', 'Naranjas'])
# %%
# Load data into a Pandas dataframe
flowers_df = sns.load_dataset("iris")
print (flowers_df)
print (flowers_df.species.unique())

# %%
flowers_df = sns.load_dataset("iris")
print (flowers_df)
print (flowers_df.species.unique())
plt.plot(flowers_df.sepal_length, flowers_df.sepal_width);
# %%
flowers_df = sns.load_dataset("iris")
print (flowers_df)
print (flowers_df.species.unique())
#plt.plot(flowers_df.sepal_length, flowers_df.sepal_width);
sns.scatterplot(x=flowers_df.sepal_length, y=flowers_df.sepal_width);
# %%
flowers_df = sns.load_dataset("iris")
print (flowers_df)
print (flowers_df.species.unique())
sns.scatterplot(x=flowers_df.sepal_length, y=flowers_df.sepal_width, hue=flowers_df.species, s=100);
# %%
flowers_df = sns.load_dataset("iris")
plt.figure(figsize=(12, 6))
plt.title('Dimension de Sepalo')
sns.scatterplot(x=flowers_df.sepal_length, y=flowers_df.sepal_width, hue=flowers_df.species, s=100);
# %%
flowers_df = sns.load_dataset("iris")
plt.figure(figsize=(12, 6))
plt.title('Dimensiones de Sepalo')
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', s=100, data=flowers_df);
# %%
plt.figure(figsize=(12, 6))
plt.title('Dimensiones de Sepalo')
plt.hist(flowers_df.sepal_width);
# %%
plt.figure(figsize=(12, 6))
plt.title('Dimensiones de Sepalo')
plt.hist(flowers_df.sepal_width, bins=3);
# %%
plt.figure(figsize=(12, 6))
plt.title('Dimensiones de Sepalo')
plt.hist(flowers_df.sepal_width, bins=np.arange(2, 6, 0.25));
# %%
plt.figure(figsize=(12, 6))
plt.title('Dimensiones de Sepalo')
plt.hist(flowers_df.sepal_width, bins=[1, 3, 4, 4.5]);
# %%
plt.figure(figsize=(12, 6))
plt.title('Dimensiones de Sepalo')
setosa_df = flowers_df[flowers_df.species == 'setosa']
versicolor_df = flowers_df[flowers_df.species == 'versicolor']
virginica_df = flowers_df[flowers_df.species == 'virginica']
plt.hist(setosa_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25));
plt.hist(versicolor_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25));
plt.hist(virginica_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25));
# %%
plt.figure(figsize=(12, 6))
plt.title('Dimensiones de Sepalo')
setosa_df = flowers_df[flowers_df.species == 'setosa']
versicolor_df = flowers_df[flowers_df.species == 'versicolor']
virginica_df = flowers_df[flowers_df.species == 'virginica']
plt.hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width],

bins=np.arange(2, 5, 0.25),
stacked=True);

plt.legend(['Setosa', 'Versicolor', 'Virginica']);
# %%
import matplotlib

years = range(2000, 2006)
apples = [0.35, 0.6, 0.9, 0.8, 0.65, 0.8]
oranges = [0.4, 0.8, 0.9, 0.7, 0.6, 0.8]
plt.figure(figsize=(12, 6))
matplotlib.rcParams['font.size'] = 20
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'
sns.set_style("darkgrid")
plt.bar(years, oranges);
plt.bar(years, oranges, bottom=apples);
plt.xlabel('Año')
plt.ylabel('Rendimiento (toneladas por hectárea)');
plt.title("Rendimiento de los campos en Baja California")
plt.legend(['Manzanas', 'Naranjas'])
# %%
tips_df = sns.load_dataset("tips");
print(tips_df)
# %%
print(tips_df)
sns.barplot(x='day', y='total_bill', data=tips_df);
# %%
tips_df = sns.load_dataset("tips");
print(tips_df)
sns.barplot(x='day', y='total_bill', hue='sex', data=tips_df);
# %%
sns.barplot(x='total_bill', y='day', hue='sex', data=tips_df);
# %%
# Chart title
plt.title("Daily Total Bill")
# Draw a nested boxplot to show bills by day and time
sns.boxplot(x=tips_df.day,

y=tips_df.total_bill,
hue=tips_df.smoker);
# %%
flights_df = sns.load_dataset("flights").pivot(index="month", columns="year", values="passengers")
print(flights_df)
# %%
flights_df = sns.load_dataset("flights").pivot(index="month", columns="year", values="passengers")
print(flights_df)
plt.title("Número de pasajeros (1000s)")
sns.heatmap(flights_df);
# %%
flights_df = sns.load_dataset("flights").pivot(index="month", columns="year", values="passengers")
plt.title("Número de pasajeros (1000s)")
sns.heatmap(flights_df, fmt="d", annot=True, cmap='Blues');
# %%
# Load data into a Pandas dataframe
flowers_df = sns.load_dataset("iris")
plt.figure(figsize=(12, 6))
plt.title('Flores')
sns.kdeplot(x=flowers_df.sepal_length,
y=flowers_df.sepal_width,
shade=True,
shade_lowest=False);
# %%
# Load data into a Pandas dataframe
flowers_df = sns.load_dataset("iris")
plt.figure(figsize=(12, 6))
plt.title('Flores')
setosa = flowers_df[flowers_df.species ==
'setosa']
virginica = flowers_df[flowers_df.species ==
'virginica']
plt.title("Flowers (Setosa & Virginica)")
sns.kdeplot(x=setosa.sepal_length,
y=setosa.sepal_width,
shade=True, cmap='Reds',
shade_lowest=False)

sns.kdeplot(x=virginica.sepal_length,
y=virginica.sepal_width,
shade=True, cmap='Blues',
shade_lowest=False);
# %%
from PIL import Image
img = Image.open('imagen1.jpeg')
img_array = np.array(img)
plt.imshow(img);
# %%
img_array = np.array(img)
plt.grid(False)
plt.title('A data science meme')
plt.axis('off')
plt.imshow(img);
# %%
img_array = np.array(img)
plt.grid(False)
plt.title('A data science meme')
plt.axis('off')
plt.imshow(img_array[125:325,105:305]);
# %%
fig, axes = plt.subplots(2, 3, figsize=(16, 8))
# Use the axes for plotting
axes[0,0].plot(years, apples, 's-b')
axes[0,0].plot(years, oranges, 'o--r')
axes[0,0].set_xlabel('Year')
axes[0,0].set_ylabel('Yield (tons per hectare)')
axes[0,0].legend(['Apples', 'Oranges']);
axes[0,0].set_title('Crop Yields in Kanto')

# Pass the axes into seaborn
axes[0,1].set_title('Sepal Length vs. SepalWidth')
sns.scatterplot(x=flowers_df.sepal_length,
y=flowers_df.sepal_width,
hue=flowers_df.species,
s=100,
ax=axes[0,1]);

# Use the axes for plotting
axes[0,2].set_title('Distribution of Sepal Width')
axes[0,2].hist([setosa_df.sepal_width,
versicolor_df.sepal_width, virginica_df.sepal_width],

bins=np.arange(2, 5, 0.25),
stacked=True);

axes[0,2].legend(['Setosa', 'Versicolor',
'Virginica']);
# Pass the axes into seaborn
axes[1,0].set_title('Restaurant bills')
sns.barplot(x='day', y='total_bill', hue='sex',
data=tips_df, ax=axes[1,0]);
# Pass the axes into seaborn
axes[1,1].set_title('Flight traffic')
sns.heatmap(flights_df, cmap='Blues', ax=axes[1,1]);
# Plot an image using the axes
axes[1,2].set_title('Data Science Meme')
axes[1,2].imshow(img)
axes[1,2].grid(False)
axes[1,2].set_xticks([])
axes[1,2].set_yticks([])
plt.tight_layout(pad=2);
# %%
##Tarea Numero 8 / Modificar y traducir
#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-
#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

#Crear figura y ejes
#Crea una figura con una cuadrícula de 2 filas y 3 columnas de subgráficos y un tamaño de 16x8 pulgadas
fig, axes = plt.subplots(2, 3, figsize=(16, 8))


#Gráfico de Líneas (Yields de Cultivos en Kanto)
axes[0,0].plot(years, apples, 's-b')  #Traza una línea azul sólida con marcadores cuadrados('s' = Cuadrado, 'b'= Azul, '-' Linea solida)
axes[0,0].plot(years, oranges, 'o--r')   #Traza una línea roja discontinua con marcadores circulares ('o' = Circulo, 'r'= Rojo, '-' Linea discontinua)
axes[0,0].set_xlabel('Año')  #Etiqueta del eje x
axes[0,0].set_ylabel('Rendimiento (toneladas por hectárea)')  #Etiqueta del eje y
axes[0,0].legend(['Manzanas', 'Naranjas'])  #Añade una leyenda para identificar las líneas (Por orden de agregacion)
axes[0,0].set_title('Rendimientos de Cultivos en Kanto')  #Título del gráfico

#Gráfico de Dispersión (Longitud vs. Ancho del Sépalo)
axes[0,1].set_title('Longitud vs. Ancho del Sépalo')  #Título del gráfico
#Crea un gráfico de dispersión con puntos coloreados según la especie de la flor
sns.scatterplot(x=flowers_df.sepal_length, y=flowers_df.sepal_width, hue=flowers_df.species, s=100, ax=axes[0,1])
axes[0,1].set_xlabel('Longitud del Sépalo (cm)')  #Etiqueta del eje x
axes[0,1].set_ylabel('Ancho del Sépalo (cm)')  #Etiqueta del eje y

#Histograma (Distribución del Ancho del Sépalo)
axes[0,2].set_title('Distribución del Ancho del Sépalo')  #Título del gráfico
#Crea un histograma apilado para mostrar la distribución del ancho del sépalo para tres especies de flores
axes[0,2].hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width], bins=np.arange(2, 5, 0.25), stacked=True)
axes[0,2].set_xlabel('Ancho del Sépalo (cm)')  #Etiqueta del eje x
axes[0,2].set_ylabel('Frecuencia')  #Etiqueta del eje y
axes[0,2].legend(['Setosa', 'Versicolor', 'Virginica'])  #Añade una leyenda para identificar las especies

# Gráfico de Barras (Cuentas de Restaurante)
axes[1,0].set_title('Cuentas de Restaurante')  #Título del gráfico
sns.barplot(x='day', y='total_bill', hue='sex', data=tips_df, ax=axes[1,0])   #Crea un gráfico de barras que muestra la cuenta total por día de la semana y por género
axes[1,0].set_xlabel('Día')  #Etiqueta del eje x
axes[1,0].set_ylabel('Cuenta Total')  #Etiqueta del eje y

#Mapa de Calor (Tráfico Aéreo)
axes[1,1].set_title('Tráfico Aéreo')  #Título del gráfico
sns.heatmap(flights_df, cmap='Blues', ax=axes[1,1])   #Crea un mapa de calor para mostrar el tráfico aéreo, con colores que indican la intensidad del tráfico
axes[1,1].set_xlabel('Mes')  #Etiqueta del eje x
axes[1,1].set_ylabel('Año')  #Etiqueta del eje y

#Mostrar una Imagen (Meme de Ciencia de Datos)
axes[1,2].set_title('Meme de Ciencia de Datos')  #Título del gráfico
axes[1,2].imshow(img)  #Muestra una imagen en el gráfico
axes[1,2].grid(False)  #Elimina la cuadrícula del gráfico
axes[1,2].set_xticks([])  #Elimina las marcas del eje x
axes[1,2].set_yticks([])  #Elimina las marcas del eje y

#Ajuste de Diseño
plt.tight_layout(pad=2)
#Ajusta el diseño de los gráficos para que no se superpongan y añade un pequeño espacio entre ellos
plt.show()
#Muestra la figura con todos los gráficos
#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-
#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-
# %%


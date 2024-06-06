# Importar las librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Función para la carga de datos
def cargar_datos(ruta_archivo):
    """
    Carga los datos de incendios desde un archivo CSV.

    Parámetros:
    ruta_archivo (str): Ruta del archivo CSV.

    Returns:
    DataFrame: DataFrame con los datos de incendios.
    """
    # Cargar los datos
    fire_df = pd.read_csv(ruta_archivo, encoding='iso-8859-1', dtype=str)

    # Imprimir el tipo de objeto
    print("Tipo de objeto:", type(fire_df))
    print("----------------------------------------------------------------")

    # Mostrar información sobre el DataFrame
    print("\nDescripción de los datos:")
    print(fire_df.info())

    # Mostrar las primeras filas del DataFrame
    print("\nPrimeras filas de los datos:")
    print(fire_df.head(10))

    # Mostrar las últimas filas del DataFrame
    print("\nÚltimas filas de los datos:")
    print(fire_df.tail(10))

    return fire_df

# Definir la ruta del archivo de datos
ruta_archivo = '/content/drive/MyDrive/Colab_EDyA/incendios.csv'

# Cargar los datos
fire_df = cargar_datos(ruta_archivo)

# Función para la limpieza de datos
def limpiar_datos(df):
    """
    Realiza la limpieza de los datos.

    Parámetros:
    df (DataFrame): DataFrame con los datos de incendios.

    Returns:
    DataFrame: DataFrame limpio.
    """
    # Convertir columnas numéricas a tipo float
    numeric_columns = ['latitud_grados', 'latitud_minutos', 'latitud_segundos', 'longitud_grados',
                       'longitud_minutos', 'longitud_segundos', 'Duración días', 'Arbolado Adulto',
                       'Renuevo', 'Arbustivo', 'Herbáceo', 'Hojarasca', 'Total hectáreas']
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Eliminar columnas irrelevantes
    df = df.drop(['Clave del incendio', 'Clave Municipio', 'CVE_ENT', 'CVE_MUN', 'CVEGEO', 'Predio'], axis=1)

    # Convertir columnas numéricas a tipos de datos numéricos
    numeric_columns = ['Año', 'Duración días', 'Arbolado Adulto', 'Renuevo', 'Arbustivo', 'Herbáceo', 'Hojarasca', 'Total hectáreas']
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

    # Especificar el formato de fecha y hora
    df['Fecha Inicio'] = pd.to_datetime(df['Fecha Inicio'], format='%d/%m/%Y', errors='coerce')
    df['Fecha Termino'] = pd.to_datetime(df['Fecha Termino'], format='%d/%m/%Y', errors='coerce')

    # Convertir columnas de latitud y longitud a tipo float
    df['Latitud'] = pd.to_numeric(df['Latitud'], errors='coerce')
    df['Longitud'] = pd.to_numeric(df['Longitud'], errors='coerce')

    # Imputación de valores faltantes usando la media
    for col in ['Duración días', 'Arbolado Adulto', 'Renuevo', 'Arbustivo', 'Herbáceo', 'Hojarasca']:
        df[col] = df[col].fillna(df[col].mean())

    # Información básica del DataFrame después de la conversión y la imputación
    print("\nInformación después de la conversión e imputación de valores faltantes:")
    print(df.info())

    # Descripción estadística de las columnas numéricas
    print("\nDescripción estadística de las columnas numéricas:")
    print(df.describe())

    return df

# Limpiar los datos
fire_df = limpiar_datos(fire_df)

# Función para generar un gráfico de barras del número de incendios por estado
def grafico_incendios_por_estado(df):
    """
    Genera un gráfico de barras del número de incendios por estado.

    Parámetros:
    df (DataFrame): DataFrame con los datos de incendios.
    """
    plt.figure(figsize=(15, 8))
    sns.countplot(data=df, y='Estado', order=df['Estado'].value_counts().index, hue='Estado', legend=False)
    plt.title('Número de Incendios por Estado', fontsize=16)
    plt.xlabel('Número de Incendios', fontsize=14)
    plt.ylabel('Estado', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.text(0.5, -0.15, "Este gráfico muestra la distribución del número de incendios por estado.", ha='center', fontsize=12, transform=plt.gca().transAxes)
    plt.show()
    plt.close()

# Función para generar un gráfico de líneas que muestra la cantidad de incendios a lo largo del tiempo
def grafico_lineas_incendios_por_año(df):
    """
    Crea un gráfico de líneas que muestra la cantidad de incendios a lo largo del tiempo.

    Parámetros:
    df (DataFrame): DataFrame con los datos de incendios.

    Returns:
    None
    """
    plt.figure(figsize=(15, 8))
    df['Año'] = pd.to_datetime(df['Año'], format='%Y')  # Convertir a formato de fecha
    fires_per_year = df.groupby('Año').size()
    fires_per_year.plot(kind='line', marker='o', color='green')
    plt.title('Número de Incendios a lo Largo del Tiempo', fontsize=16)
    plt.xlabel('Año', fontsize=14)
    plt.ylabel('Número de Incendios', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True)
    plt.text(0.5, -0.15, "Este gráfico muestra la cantidad de incendios a lo largo del tiempo en forma de serie temporal.", ha='center', fontsize=12, transform=plt.gca().transAxes)
    plt.show(block=False)
    plt.close()

# Función para generar un gráfico de barras que muestra la cantidad de incendios por mes a lo largo del tiempo
def grafico_barras_incendios_por_mes(df):
    """
    Crea un gráfico de barras que muestra la cantidad de incendios por mes a lo largo del tiempo.

    Parámetros:
    df (DataFrame): DataFrame con los datos de incendios.

    Retorna:
    Nada
    """
    df['Mes'] = df['Fecha Inicio'].dt.month
    incendios_por_meses = df.groupby('Mes').size()

    # Mapear números de mes a nombres de mes
    meses = {
        1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio',
        7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
    }

    # Obtener nombres de mes para cada número de mes
    nombres_meses = [meses[numero_mes] for numero_mes in incendios_por_meses.index]

    plt.figure(figsize=(15, 8))
    incendios_por_meses.plot(kind='bar', color='skyblue')
    plt.title('Número de Incendios por Mes', fontsize=16)
    plt.xlabel('Mes', fontsize=14)
    plt.ylabel('Número de Incendios', fontsize=14)
    plt.xticks(range(len(incendios_por_meses)), nombres_meses, rotation=45, ha='right', fontsize=12)
    plt.yticks(fontsize=12)
    plt.text(0.5, -0.3, "Este gráfico muestra la cantidad de incendios por mes a lo largo del tiempo.", ha='center', fontsize=12, transform=plt.gca().transAxes)
    plt.show()
    plt.close()

# Función para generar un gráfico de dispersión que muestra la distribución geográfica de los incendios por latitud y longitud
def grafico_dispersion_incendios_latitud_longitud(df):
    """
    Crea un gráfico de dispersión que muestra la distribución geográfica de los incendios por latitud y longitud.

    Parámetros:
    df (DataFrame): DataFrame con los datos de incendios.

    Retorna:
    Nada
    """
    plt.figure(figsize=(10, 10))
    sns.scatterplot(data=df, x='Longitud', y='Latitud', hue='Estado', palette='tab10', s=10)
    plt.title('Incendios por Latitud y Longitud', fontsize=16)
    plt.xlabel('Longitud', fontsize=14)
    plt.ylabel('Latitud', fontsize=14)
    plt.legend(loc='upper right', bbox_to_anchor=(1.25, 1), fontsize=12)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.text(0.3, -0.15, "Este gráfico muestra la distribución geográfica de los incendios por latitud y longitud, coloreados por estado.", ha='center', fontsize=12, transform=plt.gca().transAxes)
    plt.show()
    plt.close()

# Función para crear un mapa de calor de densidad que muestra la concentración de incendios en función de su ubicación geográfica
def mapa_calor_densidad_incendios(df):
    """
    Crea un mapa de calor de densidad que muestra la concentración de incendios en función de su ubicación geográfica.

    Parámetros:
    df (DataFrame): DataFrame con los datos de incendios.

    Regresa:
    Nada
    """
    plt.figure(figsize=(12, 8))
    sns.kdeplot(x=df['Longitud'], y=df['Latitud'], cmap='Reds', fill=True)
    plt.title('Mapa de Calor de Densidad de Incendios', fontsize=16)
    plt.xlabel('Longitud', fontsize=14)
    plt.ylabel('Latitud', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.text(0.5, -0.1, "Este mapa de calor de densidad muestra la concentración de incendios en función de su ubicación geográfica.", ha='center', fontsize=12, transform=plt.gca().transAxes)
    plt.show()
    plt.close()

# Función para generar un gráfico de pastel que muestra el porcentaje de incendios por temporada
def grafico_porcentaje_incendios_temporada(df):
    """
    Crea un gráfico de pastel que muestra el porcentaje de incendios por temporada.

    Parámetros:
    df (DataFrame): DataFrame con los datos de incendios.

    Retorna:
    Nada
    """
    df['Temporada'] = df['Fecha Inicio'].dt.month.map({1: 'Invierno', 2: 'Invierno', 3: 'Primavera', 4: 'Primavera',
                                                      5: 'Primavera', 6: 'Verano', 7: 'Verano', 8: 'Verano',
                                                      9: 'Otoño', 10: 'Otoño', 11: 'Otoño', 12: 'Invierno'})

    plt.figure(figsize=(10, 8))
    explode = (0.1, 0, 0, 0)  # Destacar la primera porción (Invierno)

    season_counts = df['Temporada'].value_counts()
    season_counts.plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette('pastel'), labels=None, explode=explode, shadow=True, startangle=140, textprops={'fontsize': 12})
    plt.title('Porcentaje de Incendios por Temporada', fontsize=18, fontweight='bold')
    plt.axis('equal')  # Hacer que el gráfico de pastel sea circular
    plt.ylabel('')  # Eliminar etiqueta del eje y

    # Agregar leyenda y ajustar tamaño de fuente
    plt.legend(season_counts.index, loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
    plt.text(0.5, -0.1, "Este gráfico de pastel muestra el porcentaje de incendios por temporada.", ha='center', fontsize=12, transform=plt.gca().transAxes)
    plt.show()
    plt.close()

# Función para generar un gráfico de pastel que muestra la proporción de incendios por tipo de vegetación afectada
def grafico_pastel_vegetacion_afectada(df):
    """
    Crea un gráfico de pastel que muestra la proporción de incendios por tipo de vegetación afectada.

    Parámetros:
    df (DataFrame): DataFrame con los datos de incendios.
    """
    # Sumar los valores de hectáreas afectadas por cada tipo de vegetación
    tipos_vegetacion = ['Arbolado Adulto', 'Renuevo', 'Arbustivo', 'Herbáceo', 'Hojarasca']
    suma_hectareas = df[tipos_vegetacion].sum()

    # Filtrar tipos de vegetación con al menos 1% del total de hectáreas afectadas
    suma_total = suma_hectareas.sum()
    suma_hectareas_filtradas = suma_hectareas[suma_hectareas / suma_total >= 0.01]

    # Crear etiquetas con porcentajes
    etiquetas = [f'{tipo} ({porcentaje:.2f}%)' for tipo, porcentaje in zip(suma_hectareas_filtradas.index, suma_hectareas_filtradas / suma_total * 100)]

    # Crear el gráfico de pastel
    plt.figure(figsize=(10, 8))
    explode = (0.1,) * len(suma_hectareas_filtradas)  # Destacar todas las porciones
    suma_hectareas_filtradas.plot(kind='pie', labels=None, autopct='%1.1f%%', startangle=140, explode=explode, shadow=True, colors=sns.color_palette('pastel'), textprops={'fontsize': 12})
    plt.title('Proporción de Incendios por Tipo de Vegetación Afectada', fontsize=18, fontweight='bold')
    plt.axis('equal')  # Hacer que el gráfico de pastel sea circular

    # Agregar leyenda y ajustar tamaño de fuente
    plt.legend(etiquetas, loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
    plt.text(0.5, -0.1, "Este gráfico muestra la proporción de hectáreas afectadas por tipo de vegetación.", ha='center', fontsize=12, transform=plt.gca().transAxes)
    plt.show()
    plt.close()

# Función para comparar el total de hectáreas quemadas por región
def grafico_comparacion_total_hectareas_regiones(df):
    """
    Crea un gráfico de barras que compara el total de hectáreas quemadas por región.

    Parámetros:
    df (DataFrame): DataFrame con los datos de incendios.

    Retorna:
    Nada
    """
    plt.figure(figsize=(12, 8))
    df.groupby('Región')['Total hectáreas'].median().sort_values().plot(kind='bar', color='skyblue')
    plt.title('Comparación del Total de Hectáreas Quemadas por Región', fontsize=16)
    plt.xlabel('Región', fontsize=14)
    plt.ylabel('Total de Hectáreas Quemadas', fontsize=14)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.yticks(fontsize=12)
    plt.show()
    plt.close()

# Función para generar un gráfico de caja y bigotes que muestra la distribución del total de hectáreas quemadas por estado
def grafico_hectareas_por_estado(df):
    """
    Crea un gráfico de caja y bigotes que muestra la distribución del total de hectáreas quemadas por estado.

    Parámetros:
    df (DataFrame): DataFrame con los datos de incendios.
    """
    plt.figure(figsize=(15, 8))
    sns.boxplot(data=df, x='Total hectáreas', y='Estado')
    plt.title('Total de Hectáreas Quemadas por Estado', fontsize=16)
    plt.xlabel('Total de Hectáreas Quemadas', fontsize=14)
    plt.ylabel('Estado', fontsize=14)
    plt.xscale('log')  # Usamos escala logarítmica debido a la alta variabilidad en los datos
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.text(0.5, -0.15, "Este gráfico muestra la distribución del total de hectáreas quemadas por estado mediante un diagrama de caja y bigotes.", ha='center', fontsize=12, transform=plt.gca().transAxes)
    plt.show()

# Función para generar un mapa de calor de las correlaciones entre variables numéricas en un DataFrame
def mapa_calor_correlaciones(df):
    """
    Crea un mapa de calor de las correlaciones entre variables numéricas en un DataFrame.

    Parámetros:
    df (DataFrame): DataFrame con las variables.

    Retorna:
    Nada
    """
    # Filtrar solo las columnas numéricas para el cálculo de la correlación
    columnas_numericas = df.select_dtypes(include='number').columns
    df_numeric = df[columnas_numericas]

    # Calcular la matriz de correlación
    correlaciones = df_numeric.corr()

    # Crear el mapa de calor de las correlaciones
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlaciones, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Mapa de Calor de Correlaciones entre Variables Numéricas', fontsize=16)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.yticks(rotation=0, fontsize=12)
    plt.show()
    plt.close()

# Función para mostrar el menú interactivo y permitir al usuario seleccionar gráficos
def menu_interactivo(fire_df):
    """
    Función para mostrar el menú interactivo y permitir al usuario seleccionar gráficos.
    """
    while True:
        print("\nSeleccione el gráfico que desea visualizar:")
        print("1. Número de Incendios por Estado")
        print("2. Número de Incendios a lo Largo del Tiempo (por Año)")
        print("3. Número de Incendios por Mes")
        print("4. Distribución Geográfica de los Incendios")
        print("5. Mapa de calor Geográfica de los Incendios")
        print("6. Procentaje de incendios por temporada")
        print("7. Porcentaje incendios por tipo de vegetación afectada")
        print("8. Comparación de incendios por region")
        print("9. Caja de bigote que muestra hectareas quemadas por estados")
        print("10. Correlaciones entrre variables numéricas")
        print("11. Salir")

        opcion = input("Ingrese el número de su elección: ")

        if opcion == '1':
            # Llamar a la función para generar el gráfico de barras del número de incendios por estado
            grafico_incendios_por_estado(fire_df)
        elif opcion == '2':
            # Llamar a la función para generar el gráfico de líneas que muestra la cantidad de incendios a lo largo del tiempo
            grafico_lineas_incendios_por_año(fire_df)
        elif opcion == '3':
            # Llamar a la función para generar el gráfico de barras que muestra la cantidad de incendios por mes a lo largo del tiempo
            grafico_barras_incendios_por_mes(fire_df)
        elif opcion == '4':
            # Llamar a la función para generar el gráfico de dispersión que muestra la distribución geográfica de los incendios por latitud y longitud
            grafico_dispersion_incendios_latitud_longitud(fire_df)
        elif opcion == '5':
            # Llamar a la función para generar el mapa de calor de densidad que muestra la concentración de incendios en función de su ubicación geográfica
            mapa_calor_densidad_incendios(fire_df)
        elif opcion == '6':
            # Llamar a la función para generar el gráfico de pastel que muestra el porcentaje de incendios por temporada
            grafico_porcentaje_incendios_temporada(fire_df)
        elif opcion == '7':
            # Llamar a la función para generar el gráfico de pastel que muestra la proporción de incendios por tipo de vegetación afectada
            grafico_pastel_vegetacion_afectada(fire_df)
        elif opcion == '8':
            # Llamar a la función para comparar el total de hectáreas quemadas por región
            grafico_comparacion_total_hectareas_regiones(fire_df)
        elif opcion == '9':
            # Llamar a la función para generar un gráfico de caja y bigotes que muestra la distribución del total de hectáreas quemadas por estado
            grafico_hectareas_por_estado(fire_df)
        elif opcion == '10':
            # Llamar a la función para generar un mapa de calor de las correlaciones entre variables numéricas en un DataFrame
            mapa_calor_correlaciones(fire_df)
        elif opcion == '11':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

# Función principal para ejecutar el análisis y las visualizaciones de manera interactiva
def main():
    """
    Función principal para ejecutar el análisis y las visualizaciones de manera interactiva.
    """
    menu_interactivo(fire_df)

if __name__ == "__main__":
    main()
import urllib.request
import numpy as np

# Descargar el archivo CSV
urllib.request.urlretrieve('https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv', 'climate.txt')

# Cargar los datos del archivo CSV en un arreglo NumPy
climate_data_np = np.genfromtxt('climate.txt', delimiter=',', skip_header=1)

# Imprime el contenido y las dimensiones del arreglo
print("Contenido del arreglo de datos climáticos: \n", climate_data_np)
print("Dimensiones del arreglo: \n", climate_data_np.shape)

# Crea un vector unidimensional de ejemplo (lista de Python)
weights = [0.3, 0.2, 0.5]

# Convierte el vector en un arreglo Numpy
weights_np = np.array(weights)

# Realiza la multiplicación de matrices entre los datos climáticos y los pesos
yields = np.dot(climate_data_np, weights_np)

# Imprime el resultado de la multiplicación
print("Resultados de la multiplicación: \n", yields)

# Concatena los resultados con los datos climáticos
climate_results_np = np.concatenate((climate_data_np, yields.reshape(-1, 1)), axis=1)

# Guarda los resultados en un archivo CSV
np.savetxt('climate_results.csv', climate_results_np, fmt='%.2f', delimiter=',', header='temperature,rainfall,humidity,yield_apples', comments='')

# Acceso a elementos específicos del arreglo Numpy
# Por ejemplo, el valor de la temperatura en la primera fila
print("Temperatura en la primera fila:", climate_results_np[0, 0])

# Operaciones aritméticas y de difusión en arreglos Numpy
# Por ejemplo, suma de la temperatura y la humedad en todas las filas
temperature_humidity_sum = climate_results_np[:, 0] + climate_results_np[:, 2]
print("Suma de temperatura y humedad en todas las filas:", temperature_humidity_sum)
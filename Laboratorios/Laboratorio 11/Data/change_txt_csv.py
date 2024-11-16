import os
import numpy as np
import csv

def leer_archivo_hea(archivo_hea):
    """Leer el archivo .hea y extraer metadatos (frecuencia de muestreo, número de canales)"""
    with open(archivo_hea, 'r') as f:
        lines = f.readlines()
        sampling_rate = int(lines[0].split(' ')[2])  # Frecuencia de muestreo (ej: 100 Hz)
        num_channels = int(lines[0].split(' ')[1])  # Número de canales (ej: 12)
        #num_muestras=int(lines[0].split('')[3])     
        return sampling_rate, num_channels

def convertir_dat_a_csv(archivo_dat, archivo_hea, directorio_salida):
    """Convertir un archivo .dat a un archivo .csv usando los metadatos del archivo .hea"""
    sampling_rate, num_channels = leer_archivo_hea(archivo_hea)
    
    # Leer el archivo .dat como binario de 16 bits (tipo de dato int16)
    data = np.fromfile(archivo_dat, dtype=np.int16)
    
    # Reformatear los datos en una matriz (filas x columnas) basada en el número de canales
    # Cada fila es una muestra, cada columna es un canal
    data = data.reshape(-1, num_channels)
    
    # Crear el nombre del archivo CSV de salida con la misma estructura de directorio
    output_file = archivo_dat.replace('.dat', '.csv').replace(directorio_base, directorio_salida)

    # Crear los directorios necesarios para el archivo CSV si no existen
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Escribir los datos en el archivo CSV
    with open(output_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        # Escribir los metadatos en el CSV
        csv_writer.writerow(['Frecuencia de muestreo', sampling_rate])
        csv_writer.writerow(['Número de canales', num_channels])

        # Escribir los datos de la señal
        for row in data:
            csv_writer.writerow(row)  # Cada fila en el .dat corresponde a una señal

    print(f"Archivo convertido exitosamente a CSV: {output_file}")

def procesar_archivos_en_directorio(directorio_base, directorio_salida):
    """Procesar todos los archivos .dat y .hea en un directorio base y guardarlos en directorio_salida"""
    # Recorrer todos los directorios y archivos dentro de records100/
    for root, dirs, files in os.walk(directorio_base):
        # Filtrar los archivos .dat
        archivos_dat = [f for f in files if f.endswith('.dat')]
        for archivo_dat in archivos_dat:
            archivo_hea = archivo_dat.replace('.dat', '.hea')
            archivo_dat_path = os.path.join(root, archivo_dat)
            archivo_hea_path = os.path.join(root, archivo_hea)

            # Comprobar si ambos archivos .dat y .hea existen
            if os.path.exists(archivo_hea_path):
                convertir_dat_a_csv(archivo_dat_path, archivo_hea_path, directorio_salida)
            else:
                print(f"Archivo .hea no encontrado para {archivo_dat_path}")

# Directorio base donde se encuentran los archivos .dat y .hea
directorio_base = 'C:/Users/Lenovo/OneDrive/Escritorio/CURSOS/INSTRU/PTB_DATASET/records100/'

# Directorio donde se guardarán los archivos CSV (con la misma estructura, pero sin los .dat ni .hea)
directorio_salida = 'C:/Users/Lenovo/OneDrive/Escritorio/CURSOS/INSTRU/PTB_DATASET/records100_csv/'

# Procesar todos los archivos en el directorio y guardar los CSV en la nueva ruta
procesar_archivos_en_directorio(directorio_base, directorio_salida)



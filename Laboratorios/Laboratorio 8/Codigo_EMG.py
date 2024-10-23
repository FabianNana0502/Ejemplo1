import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import pywt

# Lectura del TXT que llevamos empleando en anteriores labs:
def leer_senal_opensignals(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()

    # Buscar la línea que contiene el JSON con los parámetros
    for linea in lineas:
        if linea.startswith('# {'):
            # Remover el prefijo '#' y cargar el JSON
            json_data = json.loads(linea[2:])
            break
        
    # Extraer la frecuencia de muestreo del JSON
    device_key = list(json_data.keys())[0]  # Primera clave del JSON (el ID del dispositivo)
    fs = json_data[device_key]["sampling rate"]
    titulo = json_data[device_key]["label"]

    # Encontrar el final del encabezado ('EndOfHeader')
    inicio_datos = 0
    for i, linea in enumerate(lineas):
        if 'EndOfHeader' in linea:
            inicio_datos = i + 1
            break
    
    # Cargar los datos desde el archivo (a partir del final del encabezado)
    data = pd.read_csv(archivo, delimiter='\t', skiprows=inicio_datos, header=None)  
    # Suponiendo que la primera columna es el índice y la última columna es la señal de interés (A1)
    tiempo = np.arange(len(data)) / fs  # Crear un vector de tiempo basado en la cantidad de muestras
    senal = data.iloc[:, -1]  # Última columna (A1)

    return tiempo, senal, fs, titulo

# Descomposición y reconstrucción (Wavelet Denoise)
def wavelet_denoise(data, wavelet='db4', level=4): # nivel = 2.^i siendo i par no mayor a 3 segun articulo
    
    # Descomposición segun los niveles dados
    coeffs = pywt.wavedec(data, wavelet, level=level)
    # Cálculo de sigma (nivel de ruido estimado)
    sigma = np.median(np.abs(coeffs[-level])) / 0.6745 #  divisor indicado en el articulo
    # Umbral Universal (sqtwolog1) segun OLARTE
    uthresh = sigma * np.sqrt(2 * np.log(len(data)))  
    # Aplicacion de umbrales de manera "suave", recomendado por Olarte
    coeffs_filt = [pywt.threshold(c, value=uthresh, mode='soft') for c in coeffs]
    # Reconstruiccion de señal tras denoise
    denoised_signal = pywt.waverec(coeffs_filt, wavelet)   
    denoised_signal = denoised_signal[:len(data)]
    
    return denoised_signal

# Grafica
def graficar_senal(tiempo, senal, senal_filtrada, titulo):
    plt.figure(figsize=(12, 6))

    # Subplot 1: EMG cruda
    plt.subplot(2, 1, 1)
    plt.plot(tiempo, senal, label='EMG cruda', color='blue')
    plt.title(f'Señal EMG - {titulo}')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.legend()

    # Subplot 2: EMG filtrada con Wavelet
    plt.subplot(2, 1, 2)
    plt.plot(tiempo, senal_filtrada, label='EMG filtrada con Wavelet', color='red')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud Ajustada')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

# Leer el archivo 
archivo = input("Ingresar la ruta completa del archivo: ")
# ingrear en el TERMINAL, ejm: C:\Users\jakec\Desktop\ISB\Laboratorios\Laboratorio 4\Dataset\biceps3_mov_fuerza.txt
tiempo, senal, fs, titulo = leer_senal_opensignals(archivo)
# Rescomposición y reconstrucción
senal_filtrada = wavelet_denoise(senal)
#  Ploteo total
graficar_senal(tiempo, senal, senal_filtrada, titulo)
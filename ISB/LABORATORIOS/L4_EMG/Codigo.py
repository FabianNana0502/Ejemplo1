import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json


# Función para leer el archivo OpenSignals
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
    titulo=json_data[device_key]["label"]

# Encontrar el final del encabezado ('EndOfHeader')
    inicio_datos = 0
    for i, linea in enumerate(lineas):
        if 'EndOfHeader' in linea:
            inicio_datos = i + 1
            break
    # Cargar los datos desde el archivo (a partir del final del encabezado)
    data = pd.read_csv(archivo, delimiter='\t', skiprows=inicio_datos, header=None)
    
    # Suponiendo que la primera columna es el índice y la última columna es la señal de interés (A1)
    tiempo = np.arange(len(data)) / fs  # Crear un vector de tiempo basado en la cantidad de muestras (1000 Hz)
    senal = data.iloc[:, -1]  # Última columna (A1)

    return tiempo, senal, fs,titulo

# Función para graficar la señal
def graficar_senal(tiempo, senal, fs, titulo):
    # Graficar señal original
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(tiempo, senal)
    plt.title(titulo)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.legend()
    plt.xlim([5,10])
   
    # Calcular la FFT
    n = len(senal)
    fft = np.fft.fft(senal)
    fft_magnitud = np.abs(fft)[:n//2]  # Magnitud de la FFT
    freqs = np.fft.fftfreq(n, 1/fs)[:n//2]  # Frecuencias correspondientes
    fft_db = 20 * np.log10(fft_magnitud)        # Convertir magnitud a decibelios (dB)
    # Graficar FFT en decibelios
    plt.subplot(2, 1, 2)
    plt.plot(freqs, fft_db)
    plt.title("FFT en decibelios")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud (dB)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
    
# Leer y graficar la señal
while(1):
    archivo=input("Ingrese la dirección del archivo(Presione 1 para salir): ")
    # archivo = r"C:\Users\Lenovo\OneDrive\Escritorio\Repositorio ISB\Github\Software\EMG\Movimiento_Biceps.txt" 
    if archivo=="1":
        break
    tiempo, senal, fs, titulo = leer_senal_opensignals(archivo)
    graficar_senal(tiempo, senal, fs, titulo)
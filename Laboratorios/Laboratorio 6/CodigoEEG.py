import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from scipy.signal import butter, filtfilt, hilbert, lfilter, find_peaks, welch, iirnotch

from scipy.stats import linregress
import matplotlib.pyplot as plt

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
def ADCtouV(ADC, n = 10, VCC = 3.3):
    volts = (((ADC/(1024))-(1/2)) * VCC)/41782
    return volts*1000000
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y
def graficar_senal(tiempo, senal, fs, titulo):
    # Convertir la señal a mV (si es necesario, dependiendo del equipo usado)
    signaluV = ADCtouV(senal)
    
    # Preprocesado: remover componente DC
    pre_pro_signal = signaluV - np.average(signaluV)

    # Filtrado de la señal
    low_cutoff = 1.0
    high_cutoff = 100.0
    smooth_signal = butter_bandpass_filter(pre_pro_signal, low_cutoff, high_cutoff, fs)

    # Aplicar filtro notch para eliminar ruido de red
    b, c = iirnotch(60.0, 30.0, fs)
    smooth_signal = filtfilt(b, c, smooth_signal)

    # Configurar el gráfico
    plt.figure(figsize=(12, 8))

    # Subplot 1: Señal original en mV
    plt.subplot(3, 1, 1)
    plt.plot(tiempo, signaluV, label='Señal original')
    plt.title(f'Señal EEG ')
    plt.xlabel('Tiempo (s)')
    plt.xlim([0,12])
    plt.ylabel('Amplitud (uV)')
    plt.grid(True)
    plt.legend()

    # Subplot 2: Señal filtrada
    plt.subplot(3, 1, 2)
    plt.plot(tiempo, smooth_signal, label='Señal filtrada', color='red')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud filtrada (uV)')
    
    plt.grid(True)
    plt.legend()

    # Subplot 3: FFT de la señal
    n = len(smooth_signal)
    fft = np.fft.fft(smooth_signal)
    fft_magnitud = np.abs(fft)[:n//2]  # Magnitud de la FFT
    freqs = np.fft.fftfreq(n, 1/fs)[:n//2]  # Frecuencias correspondientes
    fft_db = 20 * np.log10(fft_magnitud)  # Convertir magnitud a dB
    
    plt.subplot(3, 1, 3)
    plt.plot(freqs, fft_db, label='FFT de la señal', color='black')
    plt.title("FFT de la Señal Filtrada")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud (dB)") 
    plt.grid(True)
    plt.legend()

    plt.tight_layout()  # Ajustar el espacio entre subplots
    plt.show()
# Leer y graficar la señal
while(1):
    archivo=input("Ingrese la dirección del archivo(Presione 1 para salir): ")
    # archivo = r"C:\Users\Lenovo\OneDrive\Escritorio\Repositorio ISB\Github\Software\EMG\Movimiento_Biceps.txt" 
    # "C:\Users\jakec\Desktop\ISB\Laboratorios\Laboratorio 6\Data\Basal.txt"
    # "C:\Users\jakec\Desktop\ISB\Laboratorios\Laboratorio 6\OpenBCI\Recordings\OpenBCISession_2024-09-25_12-32-07\OpenBCI-RAW-2024-09-25_12-32-37.txt"
    if archivo=="1":
        break
    tiempo, senal, fs, titulo = leer_senal_opensignals(archivo)
    graficar_senal(tiempo, senal, fs, titulo)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from scipy.signal import butter, filtfilt,  lfilter, iirnotch
import matplotlib.pyplot as plt
import pywt
# Función para leer la señal desde un archivo .txt de OpenSignals
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

    return tiempo, senal, fs

# Filtro de paso bajo (Butterworth)
def butter_lowpass_filter(data, cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y

# Filtro Notch para eliminar la interferencia de la línea eléctrica (50/60 Hz)
def notch_filter(data, fs, freq=50.0, quality=30.0):
    b, a = iirnotch(freq, quality, fs)
    y = filtfilt(b, a, data)
    return y

def ADCtomV(ADC, n = 10, VCC = 3.3):
    volts = (((ADC/(2**n))-(1/2)) * VCC)/1009
    return volts*1000

# Función para filtrar la señal EKG
def filtrar_senal(senal, fs):
    # Convertir la señal a mV (si es necesario, dependiendo del equipo usado)
    signalmV = ADCtomV(senal)
    
    # Preprocesado: remover componente DC
    pre_pro_signal = signalmV - np.average(signalmV)
    
    
    # Aplica un filtro Notch para eliminar la interferencia de 50 Hz
    senal_filtrada = notch_filter(pre_pro_signal, fs, freq=50.0, quality=30.0)
    
    # Aplica un filtro de paso bajo para eliminar el ruido de alta frecuencia
    senal_filtrada = butter_lowpass_filter(senal_filtrada, cutoff=40.0, fs=fs, order=4)
    
    return signalmV,senal_filtrada

# Función para detectar los picos usando la transformada wavelet
def detectar_picos_wavelet(senal_filtrada, wavelet='db4'):
    coeficientes, _ = pywt.dwt(senal_filtrada, wavelet)
    picos = np.where(np.abs(coeficientes) > np.mean(np.abs(coeficientes)))[0]
    return picos

# Visualización de la señal original y filtrada
def visualizar_senal(tiempo, signalmV, senal_filtrada, picos):
    plt.figure(figsize=(12, 6))
    
    # Señal original
    plt.subplot(2, 1, 1)
    plt.plot(tiempo, signalmV, label='Señal Original')
    plt.title('Señal EKG Original')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.xlim([2,4])
    
    # Señal filtrada
    plt.subplot(2, 1, 2)
    plt.plot(tiempo, senal_filtrada, label='Señal Filtrada', color='orange')
    plt.plot(tiempo[picos], senal_filtrada[picos], 'rx', label='Picos detectados')
    plt.title('Señal EKG Filtrada y Picos Detectados')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.xlim([2,4])
    plt.tight_layout()
    plt.legend()
    plt.show()

# Main
if __name__ == "__main__":
    # Ruta del archivo .txt de OpenSignals
    archivo = r"C:\Users\Lenovo\OneDrive\Escritorio\ECG\2daposeRespiración10.txt"
    
    # Leer la señal
    tiempo, senal, fs = leer_senal_opensignals(archivo)
    
    # Filtrar la señal
    [signalmV,senal_filtrada] = filtrar_senal(senal, fs)
    
    # Detectar picos en la señal filtrada usando transformada wavelet
    picos = detectar_picos_wavelet(senal_filtrada)
    
    # Visualizar la señal original, filtrada y los picos
    visualizar_senal(tiempo, signalmV, senal_filtrada, picos)

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import json
from scipy.signal import filtfilt, freqz
from scipy.fft import fft, fftfreq
from matplotlib.widgets import Slider

# Función para leer los coeficientes del filtro desde un archivo
def leer_coeficientes_filtro(archivo_coef, tipo_filtro):
    if tipo_filtro.lower() == 'fir':
        with open(archivo_coef, 'r') as f:
            coeficientes = np.array([float(coef) for coef in f.read().split()])
        return coeficientes, np.array([1])  # El coeficiente "b" es [1] para FIR

    elif tipo_filtro.lower() == 'iir':
        # Leer el archivo línea por línea, cada línea tiene un coeficiente b y a
        b = []
        a = []
        with open(archivo_coef, 'r') as f:
            for linea in f:
                coef_b, coef_a = linea.split(',')
                b.append(float(coef_b))
                a.append(float(coef_a))
        return np.array(b), np.array(a)
    
    else:
        raise ValueError("Tipo de filtro desconocido. Debe ser 'FIR' o 'IIR'.")

# Función para leer el archivo OpenSignals
def leer_senal_opensignals(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()

    # Buscar la línea que contiene el JSON con los parámetros
    for linea in lineas:
        if linea.startswith('# {'):
            json_data = json.loads(linea[2:])
            break

    # Extraer la frecuencia de muestreo del JSON
    device_key = list(json_data.keys())[0]
    fs = json_data[device_key]["sampling rate"]
    titulo = json_data[device_key]["label"]

    # Encontrar el final del encabezado ('EndOfHeader')
    inicio_datos = 0
    for i, linea in enumerate(lineas):
        if 'EndOfHeader' in linea:
            inicio_datos = i + 1
            break

    # Cargar los datos desde el archivo
    data = pd.read_csv(archivo, delimiter='\t', skiprows=inicio_datos, header=None)
    tiempo = np.arange(len(data)) / fs  # Crear un vector de tiempo basado en la cantidad de muestras
    senal = data.iloc[:, -1]  # Última columna (A2)

    return tiempo, senal, fs, titulo

# Función para convertir ADC a mV
def ADCtomV(ADC, n=10, VCC=3.3):
    volts = (((ADC/(2**n)) - (1/2)) * VCC) / 1009
    return volts * 1000

# Función para aplicar el filtro usando los coeficientes b y a con filtfilt (sin desfase)
def aplicar_filtro(senal, b, a):
    senal_filtrada = filtfilt(b, a, senal)  # Usar filtfilt para evitar el desfase
    return senal_filtrada

# Función para calcular y graficar la FFT
def calcular_fft(senal, fs):
    n = len(senal)
    fft_values = fft(senal)
    fft_magnitud = np.abs(fft_values)[:n//2]
    freqs = fftfreq(n, 1/fs)[:n//2]
    return freqs, fft_magnitud

# Función para actualizar las gráficas cuando se mueve el slider
def actualizar_graficas(val, ax1, ax3, tiempo, signalmV, senal_filtrada, fs, ventana_tiempo):
    t_min = val
    t_max = t_min + ventana_tiempo
    
    # Actualizar gráfica de señal original
    ax1.clear()
    ax1.plot(tiempo[(tiempo >= t_min) & (tiempo <= t_max)], signalmV[(tiempo >= t_min) & (tiempo <= t_max)], label='Señal original', linewidth=0.8)
    ax1.set_title('Original Signal')
    ax1.set_ylabel('Amplitude (mV)')
    ax1.grid(True)
    
    # Actualizar gráfica de señal filtrada
    ax3.clear()
    ax3.plot(tiempo[(tiempo >= t_min) & (tiempo <= t_max)], senal_filtrada[(tiempo >= t_min) & (tiempo <= t_max)], label='Señal filtrada', color='red', linewidth=0.8)
    ax3.set_title('Filtered Signal')
    ax3.set_xlabel('Time (s)')
    ax3.set_ylabel('Amplitud (mV)')
    ax3.grid(True)
    
    # Redibujar
    plt.draw()

# Función principal para leer los archivos, aplicar el filtro y graficar
def procesar_y_graficar(archivo_coef, archivo_senal, tipo_filtro):
    # Leer los coeficientes del filtro
    b, a = leer_coeficientes_filtro(archivo_coef, tipo_filtro)

    tiempo, senal, fs, titulo = leer_senal_opensignals(archivo_senal)
    signalmV = ADCtomV(senal)
    senal_filtrada = aplicar_filtro(signalmV, b, a)

    # Calcular FFT de las señales
    freqs_original, fft_original = calcular_fft(signalmV, fs)
    freqs_filtrada, fft_filtrada = calcular_fft(senal_filtrada, fs)

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))

    # Graficar las FFTs (no son controladas por el slider)
    ax2.plot(freqs_original, 20 * np.log10(fft_original), label='FFT original', linewidth=0.8)
    ax2.set_title('Original Signal FFT')
    ax2.set_ylabel('Magnitud (dB)')
    ax2.grid(True)

    ax4.plot(freqs_filtrada, 20 * np.log10(fft_filtrada), label='FFT filtrada', color='red', linewidth=0.8)
    ax4.set_title('Filtered Signal FFT')
    ax4.set_xlabel('Frecuencia (Hz)')
    ax4.set_ylabel('Magnitud (dB)')
    ax4.grid(True)

    # Graficar señales (controladas por el slider)
    ventana_tiempo = 3 # menor ventana posible
    ax1.plot(tiempo[:int(ventana_tiempo * fs)], signalmV[:int(ventana_tiempo * fs)], label='Señal original', linewidth=0.8)
    ax1.set_title('Original Signal')
    ax1.set_ylabel('Amplitude (mV)')
    ax1.grid(True)

    ax3.plot(tiempo[:int(ventana_tiempo * fs)], senal_filtrada[:int(ventana_tiempo * fs)], label='Señal filtrada', color='red', linewidth=0.8)
    ax3.set_title('Filtered Signal')
    ax3.set_xlabel('Time (s)')
    ax3.set_ylabel('Amplitude (mV)')
    ax3.grid(True)

    # Slider para controlar la ventana de tiempo
    ax_slider = plt.axes([0.25, 0.01, 0.5, 0.03], facecolor='lightgoldenrodyellow')
    slider = Slider(ax_slider, 'Tiempo', 0, max(tiempo) - ventana_tiempo, valinit=0, valstep=0.1)

    # Actualizar gráficas al mover el slider
    slider.on_changed(lambda val: actualizar_graficas(val, ax1, ax3, tiempo, signalmV, senal_filtrada, fs, ventana_tiempo))
    plt.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.15)
    plt.show()

# Ejecución principal
tipo_filtro = input("Ingrese el tipo de filtro (FIR o IIR): ")
archivo_coef = input("Ingrese la dirección del archivo de coeficientes: ")
archivo_senal = input("Ingrese la dirección del archivo de la señal: ")
procesar_y_graficar(archivo_coef, archivo_senal, tipo_filtro)

# Registro:
#  IIRs
# Filtro lowpass eliptic ECG: C:\Users\jakec\Desktop\ISB\Laboratorios\Laboratorio 7\Filtros Avendaño\Filtros\IIR Lowpass Eliptic\IIR lowpass eliptic ECG.txt
# Filtro lowpass buttersworth ECG: C:\Users\jakec\Desktop\ISB\Laboratorios\Laboratorio 7\Filtros Avendaño\Filtros\IIR Lowpas Buttersworth\IIR lowpass buttersworth.txt
# Filtro lowpass chebyshev ECG: C:\Users\jakec\Desktop\ISB\Laboratorios\Laboratorio 7\Filtros Avendaño\Filtros\IIR Lowpass Chebyshev\IIR lowpass chebyshev ecg.txt
# 
# INPUTS:
# d1 basal: C:\Users\jakec\Desktop\ISB\Laboratorios\Laboratorio 5\Señales_ECG\Data\1.Estado Basal\1D_basal.txt
# d1 respiracion: C:\Users\jakec\Desktop\ISB\Laboratorios\Laboratorio 5\Señales_ECG\Data\2.Respiración\1D_respiracion.txt
# d1 2do basal: C:\Users\jakec\Desktop\ISB\Laboratorios\Laboratorio 5\Señales_ECG\Data\3.Post_Respiración\1D_post_respiracion.txt
# d1 ejercicio: C:\Users\jakec\Desktop\ISB\Laboratorios\Laboratorio 5\Señales_ECG\Data\4.Ejercicio\1D_ejercicio.txt
#
# FIRs
# 
# 
# 
#
# INPUTS
#
#
#
#
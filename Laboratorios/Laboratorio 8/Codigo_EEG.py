import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pywt

# Función para cargar los datos del archivo .txt
def cargar_eeg(filepath):
    datos = pd.read_csv(filepath, comment='%', delimiter=',')
    datos.columns = datos.columns.str.strip()
    
    columnas_eeg = ['EXG Channel 0', 'EXG Channel 1', 'EXG Channel 2', 
                    'EXG Channel 3', 'EXG Channel 4', 'EXG Channel 5', 
                    'EXG Channel 6', 'EXG Channel 7']
    
    if all(col in datos.columns for col in columnas_eeg):
        eeg_data = datos[columnas_eeg]
    else:
        raise KeyError("No se encontraron las columnas EEG esperadas en el archivo.")
    return eeg_data

# Función para eliminar la tendencia cuadrática
def eliminar_tendencia_cuadratica(signal, tiempo):
    coeficientes = np.polyfit(tiempo, signal, 2)
    tendencia = np.polyval(coeficientes, tiempo)
    return signal - tendencia

# Función para ajustar los promedios de cada segundo
def ajustar_promedio_por_segundo(signal, tiempo, fs):
    señal_ajustada = signal.copy()
    num_muestras_por_segundo = fs
    for inicio in range(0, len(señal_ajustada), num_muestras_por_segundo):
        fin = min(inicio + num_muestras_por_segundo, len(señal_ajustada))
        promedio = np.mean(señal_ajustada[inicio:fin])
        señal_ajustada[inicio:fin] -= promedio
    return señal_ajustada

# Función para suavizar las señales con media móvil
def suavizar_senal(signal, window_size=5):
    return np.convolve(signal, np.ones(window_size) / window_size, mode='same')

# Función para aplicar el filtrado Wavelet a la señal EEG con un wavelet discreto
def filtrar_wavelet(signal, wavelet='db4', level=1):
    # Aplicar la descomposición de wavelet
    coeficientes = pywt.wavedec(signal, wavelet, level=level)
    # Se eliminan los coeficientes de detalle de alta frecuencia (ruido)
    coeficientes_filtrados = [coef if i == 0 else np.zeros_like(coef) for i, coef in enumerate(coeficientes)]
    # Reconstruir la señal filtrada
    señal_filtrada = pywt.waverec(coeficientes_filtrados, wavelet)
    return señal_filtrada[:len(signal)]  # Ajustar longitud si es necesario

# Cargar los datos del EEG
ruta_archivo = r"C:\Users\LENOVO\Desktop\4_10_ISB\Laboratorios\Laboratorio 6\Data_OpenBCI\OpenBCISession_Preguntas2\OpenBCI-RAW-2024-09-25_12-37-40.txt"
eeg_data = cargar_eeg(ruta_archivo)

# Crear el vector de tiempo en segundos (asumiendo 250 Hz de frecuencia de muestreo)
frecuencia_muestreo = 250  # Frecuencia de muestreo en Hz
tiempo_total = len(eeg_data) / frecuencia_muestreo  # Tiempo total en segundos
tiempo = np.linspace(0, tiempo_total, len(eeg_data))

# Limitar el rango del gráfico desde el segundo 5 hasta un segundo antes del final
xlim_min = 5
xlim_max = 10
# Filtrar los datos para el rango de tiempo
indices_rango = (tiempo >= xlim_min) & (tiempo <= xlim_max)
tiempo_rango = tiempo[indices_rango]
eeg_data_rango = eeg_data[indices_rango]

# Aplicar eliminación de tendencia cuadrática a todas las señales
eeg_data_quadratic_detrended = eeg_data_rango.apply(eliminar_tendencia_cuadratica, args=(tiempo_rango,))

# Aplicar el ajuste de promedios segundo a segundo
eeg_data_ajustada = eeg_data_quadratic_detrended.apply(ajustar_promedio_por_segundo, args=(tiempo_rango, frecuencia_muestreo))

# Suavizar todas las señales
eeg_data_suavizada = eeg_data_ajustada.apply(suavizar_senal)

# Filtrar las señales usando el Wavelet Daubechies ('db4')
eeg_data_filtrada = eeg_data_suavizada.apply(filtrar_wavelet, args=('db4', 1))

# Crear subplots de 8 filas y 2 columnas (izquierda: señal original, derecha: señal filtrada)
fig, axes = plt.subplots(8, 2, figsize=(16, 20), sharex=True)

# Colores para las diferentes señales
colores = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange']

# Plotear cada señal en su propio subplot (señal original a la izquierda, filtrada a la derecha)
for i, canal in enumerate(eeg_data_suavizada.columns):
    # Señal original (izquierda)
    axes[i, 0].plot(tiempo_rango, eeg_data_suavizada[canal], label=f'Canal {i+1}', color=colores[i])
    min_val = eeg_data_suavizada[canal].min()
    max_val = eeg_data_suavizada[canal].max()
    axes[i, 0].set_ylim([min_val - 10, max_val + 10])
    axes[i, 0].set_title(f'Señal Original Canal {i+1}')
    axes[i, 0].grid(True)
    
    # Señal filtrada (derecha)
    axes[i, 1].plot(tiempo_rango, eeg_data_filtrada[canal], label=f'Canal {i+1} Filtrada', color=colores[i])
    min_val = eeg_data_filtrada[canal].min()
    max_val = eeg_data_filtrada[canal].max()
    axes[i, 1].set_ylim([min_val - 10, max_val + 10])
    axes[i, 1].set_title(f'Señal Filtrada Canal {i+1}')
    axes[i, 1].grid(True)

# Etiquetas de los ejes
fig.text(0.5, 0.04, 'Tiempo (s)', ha='center', fontsize=14)
fig.text(0.04, 0.5, 'Amplitud (µVrms)', va='center', rotation='vertical', fontsize=14)
fig.suptitle('Señales EEG: Original y Filtrada con Wavelet Discreto (Daubechies)', fontsize=16)

# Ajustar el layout
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.95, hspace=0.5)

# Mostrar el gráfico
plt.show()

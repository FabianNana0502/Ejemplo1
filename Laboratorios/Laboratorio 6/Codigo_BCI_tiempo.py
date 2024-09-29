import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import detrend

# Función para cargar los datos del archivo .txt
def cargar_eeg(filepath):
    # Leer el archivo, ignorar las líneas de metadatos que comienzan con '%'
    datos = pd.read_csv(filepath, comment='%', delimiter=',')

    # Eliminar espacios en blanco al inicio y final de los nombres de las columnas
    datos.columns = datos.columns.str.strip()
    
    # Seleccionar las columnas de interés (EXG Channel 0 a EXG Channel 7)
    columnas_eeg = ['EXG Channel 0', 'EXG Channel 1', 'EXG Channel 2', 
                    'EXG Channel 3', 'EXG Channel 4', 'EXG Channel 5', 
                    'EXG Channel 6', 'EXG Channel 7']
    
    # Verificar si estas columnas existen en el archivo
    if all(col in datos.columns for col in columnas_eeg):
        # Filtrar solo las columnas de EEG
        eeg_data = datos[columnas_eeg]
    else:
        raise KeyError("No se encontraron las columnas EEG esperadas en el archivo.")

    # Devolver los datos filtrados
    return eeg_data

# Función para eliminar la tendencia cuadrática
def eliminar_tendencia_cuadratica(signal, tiempo):
    # Ajustar un polinomio de grado 2 (cuadrático) a la señal
    coeficientes = np.polyfit(tiempo, signal, 2)
    tendencia = np.polyval(coeficientes, tiempo)
    # Restar la tendencia cuadrática
    return signal - tendencia

# Función para ajustar los promedios de cada segundo
def ajustar_promedio_por_segundo(signal, tiempo, fs):
    # Crear una copia de la señal para modificar
    señal_ajustada = signal.copy()
    num_muestras_por_segundo = fs  # 250 Hz significa 250 muestras por segundo
    
    # Iterar sobre cada segundo de la señal y ajustar el promedio
    for inicio in range(0, len(señal_ajustada), num_muestras_por_segundo):
        fin = min(inicio + num_muestras_por_segundo, len(señal_ajustada))
        promedio = np.mean(señal_ajustada[inicio:fin])
        señal_ajustada[inicio:fin] -= promedio  # Restar el promedio para centrar
        
    return señal_ajustada

# Función para suavizar las señales con media móvil
def suavizar_senal(signal, window_size=5):
    return np.convolve(signal, np.ones(window_size) / window_size, mode='same')

# Cargar los datos del EEG
ruta_archivo = r"C:\Users\LENOVO\Desktop\isb_28_09\Laboratorios\Laboratorio 6\OpenBCI\Recordings\OpenBCISession_Basal (again)\OpenBCI-RAW-2024-09-25_12-35-13.txt"
eeg_data = cargar_eeg(ruta_archivo)

# Crear el vector de tiempo en segundos (asumiendo 250 Hz de frecuencia de muestreo)
frecuencia_muestreo = 250  # Frecuencia de muestreo en Hz
tiempo_total = len(eeg_data) / frecuencia_muestreo  # Tiempo total en segundos
tiempo = np.linspace(0, tiempo_total, len(eeg_data))

# Limitar el rango del gráfico desde el segundo 2 hasta un segundo antes del final
xlim_min = 5
xlim_max = tiempo_total - 1  # Un segundo antes del final

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

# Crear subplots de 8 filas y 1 columna
fig, axes = plt.subplots(8, 1, figsize=(12, 16), sharex=True)

# Colores para las diferentes señales
colores = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange']

# Plotear cada señal en su propio subplot
for i, canal in enumerate(eeg_data_suavizada.columns):
    axes[i].plot(tiempo_rango, eeg_data_suavizada[canal], label=f'Canal {i+1}', color=colores[i])
    
    # Ajustar los límites del eje Y según los valores mínimos y máximos de las señales
    min_val = eeg_data_suavizada[canal].min()
    max_val = eeg_data_suavizada[canal].max()
    axes[i].set_ylim([min_val - 10, max_val + 10])  # Ajustar con un margen de 100 µV
    
    # Etiquetas de cada subplot
    axes[i].grid(True)

# Etiqueta del eje X compartido y título general
fig.text(0.5, 0.04, 'Tiempo (s)', ha='center', fontsize=14)
fig.text(0.04, 0.5, 'Amplitud (µVrms)', va='center', rotation='vertical', fontsize=14)
fig.suptitle('Señales EEG', fontsize=16)

# Ajustar el layout
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9)

# Establecer el rango desde 2 segundos hasta un segundo antes del final
for ax in axes:
    ax.set_xlim([xlim_min, xlim_max])

# Mostrar el gráfico
plt.show()

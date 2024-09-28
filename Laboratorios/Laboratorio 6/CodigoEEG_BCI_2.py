import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar el archivo .txt en un DataFrame 
archivo_txt = r"./OpenBCI/Recordings/OpenBCISession_Preguntas2/OpenBCI-RAW-2024-09-25_12-37-40.txt"

# Leer el archivo, omitiendo las primeras filas con metadatos (indicadas con '%')
df = pd.read_csv(archivo_txt, comment='%', header=0)

# Si los nombres de las columnas tienen espacios, eliminar espacios en blanco
df.columns = df.columns.str.strip()

# Definir las columnas relevantes: Sample Index, Timestamp (Formatted) y los 8 canales de EEG
columnas_eeg = ['Sample Index', 'EXG Channel 0', 'EXG Channel 1', 'EXG Channel 2', 
                'EXG Channel 3', 'EXG Channel 4', 'EXG Channel 5', 'EXG Channel 6', 'EXG Channel 7', 'Timestamp (Formatted)']

# Verificar si las columnas requeridas están presentes
if not all(col in df.columns for col in columnas_eeg):
    print("Algunas columnas no se encontraron. Revisa los nombres de las columnas en el archivo.")
else:
    # Filtrar las columnas de interés
    df_eeg = df[columnas_eeg]

    # Convertir la columna 'Timestamp (Formatted)' a formato datetime
    df_eeg['Timestamp (Formatted)'] = pd.to_datetime(df_eeg['Timestamp (Formatted)'])

    # Calcular el tiempo transcurrido en segundos desde la primera muestra
    t0 = df_eeg['Timestamp (Formatted)'].iloc[0]
    df_eeg['Tiempo Transcurrido (s)'] = (df_eeg['Timestamp (Formatted)'] - t0).dt.total_seconds()

    # Definir la frecuencia de muestreo (Hz)
    frecuencia_muestreo = 250  # Dada en el archivo

# Crear una figura con 8 subplots (uno por cada canal de EEG)
    fig, axs = plt.subplots(8, 1, figsize=(14,10))  # 8 filas, 1 columna

    for i in range(0, 8):  # Canales de 'EXG Channel 0' a 'EXG Channel 7'
        
       # Obtener la señal del canal
        canal = df_eeg[f'EXG Channel {i}'].values

        # Calcular la FFT del canal
        fft_canal = np.fft.fft(canal)
        fft_frecuencias = np.fft.fftfreq(len(canal), d=1/frecuencia_muestreo)  # Frecuencias asociadas

        # Magnitud de la FFT
        fft_magnitud = np.abs(fft_canal)

        # Filtrar frecuencias positivas para visualización
        frecuencias_positivas = fft_frecuencias > 0
        fft_frecuencias = fft_frecuencias[frecuencias_positivas]
        fft_magnitud = fft_magnitud[frecuencias_positivas]

        # Graficar la FFT en el subplot correspondiente
        axs[i].plot(fft_frecuencias, fft_magnitud)
        axs[i].set_title(f'FFT del Canal {i+1}')
        axs[i].set_ylabel('Magnitud')
        axs[i].set_xlim([0,75])

    # Ajustar layout para que no se superpongan las etiquetas
    axs[i].set_xlabel('Frecuencia (Hz)')
    plt.tight_layout()
    plt.show()

    # Graficar todos los canales de EEG en función del tiempo transcurrido
    plt.figure(figsize=(14, 8))

    for i in range(0,8):
        plt.plot(df_eeg['Tiempo Transcurrido (s)'], df_eeg[f'EXG Channel {i}']*0.02235, label=f'Canal {i+1}')

    plt.title('Señal EEG de 8 canales - Estado Basal')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud (µV)')
    plt.legend()
    plt.grid(True)
    plt.show()

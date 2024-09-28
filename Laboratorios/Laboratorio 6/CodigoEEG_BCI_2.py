import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo .txt en un DataFrame (modificar 'ruta_al_archivo.txt' con el nombre de tu archivo)
archivo_txt = r"./OpenBCI/Recordings/OpenBCISession_Basal/OpenBCI-RAW-2024-09-25_12-32-37.txt"

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
    t0 = df_eeg['Timestamp (Formatted)'].iloc[0]  # Primer momento de tiempo
    df_eeg['Tiempo Transcurrido (s)'] = (df_eeg['Timestamp (Formatted)'] - t0).dt.total_seconds()

    # Graficar todos los canales de EEG en función del tiempo transcurrido
    plt.figure(figsize=(14, 8))

    for i in range(0, 8):  # Canales de 'EXG Channel 0' a 'EXG Channel 7'
        plt.plot(df_eeg['Tiempo Transcurrido (s)'], df_eeg[f'EXG Channel {i}']*0.02235, label=f'Canal {i+1}')

    plt.title('Señal EEG de 8 canales - OpenBCI Cyton')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud (µV)')
    plt.legend()
    plt.grid(True)
    plt.show()

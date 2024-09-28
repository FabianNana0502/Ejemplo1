import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# Función para cargar los datos del archivo .txt
def cargar_eeg(filepath):
    # Leer el archivo, ignorar las líneas de metadatos que comienzan con '%'
    datos = pd.read_csv(filepath, comment='%', delimiter=',')
    
    # Asegúrate de que las columnas sean numéricas donde sea necesario
    datos = datos.apply(pd.to_numeric, errors='coerce')
    
    # Devolver los datos del EEG, seleccionando las columnas EXG Channel 0 a EXG Channel 7
    canales_eeg = datos.iloc[:, 1:8]  # Asumimos que las columnas 1 a 8 son los canales EEG
    return canales_eeg

# Función para aplicar un filtro Butterworth
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

def bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

# Parámetros de frecuencia
frecuencia_muestreo = 250  # Frecuencia de muestreo en Hz 

# Frecuencias de los ritmos cerebrales
bandas = {
    "Delta (0.5-4 Hz)": (0.5, 4),
    "Theta (4-8 Hz)": (4, 8),
    "Alpha (8-13 Hz)": (8, 13),
    "Beta (13-30 Hz)": (13, 30),
    "Gamma (30-100 Hz)": (30, 100)
}

# Cargar los datos del EEG
ruta_archivo = r"./OpenBCI/Recordings/OpenBCISession_Basal/OpenBCI-RAW-2024-09-25_12-32-37.txt"
datos = cargar_eeg(ruta_archivo)

# Asumimos que estamos trabajando con el canal 0 (primera columna)
canal_eeg = datos.iloc[:, 2].values.astype(np.float64)  # Convertir a array de numpy de tipo float
canal_eeg=canal_eeg*0.02235
# Crear el vector de tiempo en segundos
tiempo = np.arange(len(canal_eeg)) / frecuencia_muestreo  # tiempo = muestras / frecuencia de muestreo

# Plotear los ritmos del EEG en segundos y microvoltios
plt.figure(figsize=(12, 10))

for i, (banda, (low, high)) in enumerate(bandas.items(), 1):
    filtrada = bandpass_filter(canal_eeg, low, high, frecuencia_muestreo)
    
    # Verificar que los datos filtrados no estén vacíos
    #print(f"Filtrada {banda} (primeras 10 muestras):", filtrada[:10])
    
    plt.subplot(len(bandas), 1, i)
    plt.plot(tiempo, filtrada, label=f'{banda}', color='b')
    plt.title(f'{banda}', fontsize=12)
    plt.xlabel('Tiempo (segundos)')
    plt.ylabel('Amplitud (µV)')
    plt.grid(True)
    plt.xlim([0,25])

plt.tight_layout()
plt.show()

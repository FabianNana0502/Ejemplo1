import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def ADCtomV(ADC, n=10, VCC=3.3):
    """Convierte valores ADC a mV."""
    volts = (((ADC / (2**n)) - (1/2)) * VCC) / 1009
    return volts * 1000

def downsample_signal_to_exact_samples(time, values, target_samples):
    """Reduce la señal para que contenga exactamente el número de muestras especificado."""
    downsampling_factor = max(1, int(len(values) / target_samples))
    new_indices = np.arange(0, len(values), downsampling_factor)
    downsampled_time = np.array(time)[new_indices]
    downsampled_values = np.array(values)[new_indices]
    return downsampled_time, downsampled_values, downsampling_factor

def resample_data(time, values, factor, mode="uS"):
    """Aplica upsampling o downsampling a los datos."""
    n_samples = int(len(values) * factor)  # Calcular el nuevo tamaño
    new_indices = np.linspace(0, len(values) - 1, n_samples)  # Nuevos índices
    resampled_time = np.interp(new_indices, np.arange(len(values)), time)  # Interpolación de tiempo
    resampled_values = np.interp(new_indices, np.arange(len(values)), values)  # Interpolación de valores
    print(f"Resampleo aplicado: {mode} con factor {factor}, nuevas muestras: {n_samples}")
    return resampled_time, resampled_values

def process_and_resample(folder_path, sampling_rate, target_duration=300, upsampling_factors=None, downsampling_factors=None):
    """Procesa los archivos .txt, resamplea y genera archivos CSV con gráficos."""
    if not os.path.exists(folder_path):
        print("La carpeta no existe.")
        return
    
    txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    
    if not txt_files:
        print("No se encontraron archivos .txt en la carpeta.")
        return

    target_samples = target_duration * sampling_rate  # Muestras necesarias para 5 minutos

    for file_name in txt_files:
        file_path = os.path.join(folder_path, file_name)
        print(f"Procesando: {file_name}")
        
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Identificar el final del encabezado y extraer datos
        header_end_index = next(i for i, line in enumerate(lines) if line.startswith("# EndOfHeader"))
        data_lines = lines[header_end_index + 1:]
        
        # Leer datos en DataFrame
        data = pd.DataFrame([line.split() for line in data_lines], dtype=float)
        fifth_column = data[5]  # Columna de datos de interés
        mv_values = fifth_column.apply(ADCtomV)  # Convertir ADC a mV
        
        # Crear vector de tiempo
        time = [i / sampling_rate for i in range(len(mv_values))]

        # Ajustar la señal original para tener 5 minutos de datos
        downsampled_time, downsampled_values, _ = downsample_signal_to_exact_samples(
            time, mv_values, target_samples
        )

        # Guardar la señal downsampleada (base)
        downsampled_csv_file_name = os.path.splitext(file_name)[0] + "_5min_1000Hz_downsampled.csv"
        downsampled_csv_file_path = os.path.join(folder_path, downsampled_csv_file_name)
        downsampled_data = pd.DataFrame({'Tiempo (s)': downsampled_time, 'Voltaje (mV)': downsampled_values})
        downsampled_data.to_csv(downsampled_csv_file_path, index=False, sep=';')
        print(f"Señal base guardada como: {downsampled_csv_file_name}")

        # Aplicar factores de resampleo (upsampling y downsampling)
        if upsampling_factors:
            for factor in upsampling_factors:
                resampled_time, resampled_values = resample_data(downsampled_time, downsampled_values, factor, mode="uS")
                upsampled_csv_file_name = os.path.splitext(file_name)[0] + f"_5min_1000Hz_uS{factor}.csv"
                upsampled_csv_file_path = os.path.join(folder_path, upsampled_csv_file_name)
                upsampled_data = pd.DataFrame({'Tiempo (s)': resampled_time, 'Voltaje (mV)': resampled_values})
                upsampled_data.to_csv(upsampled_csv_file_path, index=False, sep=';')
                print(f"Upsampled data guardada como: {upsampled_csv_file_name}")

        if downsampling_factors:
            for factor in downsampling_factors:
                resampled_time, resampled_values = resample_data(downsampled_time, downsampled_values, factor, mode="dS")
                downsampled_csv_file_name = os.path.splitext(file_name)[0] + f"_test_dS{factor}.csv"
                downsampled_csv_file_path = os.path.join(folder_path, downsampled_csv_file_name)
                downsampled_data = pd.DataFrame({'Tiempo (s)': resampled_time, 'Voltaje (mV)': resampled_values})
                downsampled_data.to_csv(downsampled_csv_file_path, index=False, sep=';')
                print(f"Downsampled data guardada como: {downsampled_csv_file_name}")

        # Graficar señal original y downsampleada
        plt.figure()
        plt.plot(time, mv_values, label="Original")
        plt.plot(downsampled_time, downsampled_values, label="Downsampleada (5 minutos, 1000 Hz)", linestyle="--")
        plt.title(f"Señal Original y Base: {file_name}")
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Voltaje (mV)")
        plt.legend()
        plt.grid(True)
        plt.show()

# Parámetros de entrada
folder_path = "D:/Users/DELL/Downloads/Data_ECG"  # Cambia esta ruta a la carpeta correspondiente
sampling_rate = 1000  # Frecuencia de muestreo deseada
target_duration = 300  # Duración deseada en segundos (5 minutos)
# Factores de resampleo
upsampling_factors = [1.6,1.7]  # Factores de upsampling
downsampling_factors = [0.9,1.0]  # Factores de downsampling


process_and_resample(folder_path, sampling_rate, target_duration, upsampling_factors, downsampling_factors)







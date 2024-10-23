import numpy as np
import pywt
import matplotlib.pyplot as plt

# Función para convertir el valor del ADC a milivoltios
def convertir_ADC_a_mV(valor_ADC, bits_ADC=10, voltaje_referencia=3.3):
    
    adc_maximo = (2**bits_ADC) - 1  # Por ejemplo, 2^10 - 1 = 1023 para un ADC de 10 bits
    
    # Conversión de ADC a voltios
    voltios = (valor_ADC / adc_maximo) * voltaje_referencia
    
    # Ajuste para offset (-1/2) y división final (41782 es un factor según tu ajuste)
    voltios_ajustados = (voltios - (voltaje_referencia / 2)) / 41782
    
    # Convertir a milivoltios
    milivoltios = voltios_ajustados * 1000
    return milivoltios

# Función para cargar los datos desde un archivo
def cargar_datos(ruta_archivo, max_muestras=15000):
    
    try:
        # Cargar los datos desde el archivo ignorando las primeras 10 filas y limitando las muestras
        datos = np.loadtxt(ruta_archivo, skiprows=10, max_rows=max_muestras)
        valores_ADC = datos[:, 5]  # Selecciona la columna correspondiente a los valores ADC
        valores_mV = np.array([convertir_ADC_a_mV(adc) for adc in valores_ADC])  # Convierte ADC a mV
        return valores_mV
    except Exception as e:
        print(f"Error al cargar los datos del archivo {ruta_archivo}: {e}")
        return None

# Función para aplicar denoising usando wavelet
def aplicar_wavelet_denoising(datos, wavelet='db4', nivel=9):
    
    # Descomposición de la señal en coeficientes usando wavelet
    coeficientes = pywt.wavedec(datos, wavelet, level=nivel)
    
    # Estimación del ruido usando la desviación estándar del último nivel de coeficientes
    sigma = np.std(coeficientes[-1])
    
    # Umbral basado en sigma y el tamaño de los datos
    umbral = sigma * np.sqrt(2 * np.log(len(datos))) * 2.0
    
    # Aplicar umbralización suave a los coeficientes de detalle (excepto la aproximación)
    coeficientes[1:] = [pywt.threshold(c, value=umbral, mode='soft') for c in coeficientes[1:]]
    
    # Reconstruir la señal denoised a partir de los coeficientes
    señal_reconstruida = pywt.waverec(coeficientes, wavelet)
    return señal_reconstruida

# Función para graficar las señales originales y filtradas
def graficar_señales(original, filtrada, tiempo, nombre_archivo):
    
    # Asegurar que todas las señales tengan la misma longitud
    longitud_minima = min(len(original), len(filtrada), len(tiempo))
    original = original[:longitud_minima]
    filtrada = filtrada[:longitud_minima]
    tiempo = tiempo[:longitud_minima]

    # Graficar la señal original y la filtrada
    plt.figure(figsize=(15, 13))
    plt.subplot(211)
    plt.plot(tiempo, original, label='Señal ECG original', color='red', linewidth=1)
    plt.title(f'Señal ECG Original - {nombre_archivo}', fontsize=9)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')

    plt.subplot(212)
    plt.plot(tiempo, filtrada, label='Señal ECG Filtrada', color='blue', linewidth=1)
    plt.title(f'Señal ECG Filtrada - {nombre_archivo}', fontsize=9)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')

    plt.tight_layout(pad=3.0)
    plt.show()

# Parámetros generales
frecuencia_muestreo = 250  # Frecuencia de muestreo en Hz
archivos_ECG = ["basal_ECG.txt", "Respiracion_ECG.txt", "postrespiracion_ECG.txt", "ejercicio_ECG.txt"]

# Procesamiento de cada archivo
for archivo in archivos_ECG:
    ruta_datos = f"C:/Users/DELL/Downloads/EMG1/LAB7/SenalesECG/{archivo}"
    señal_ECG = cargar_datos(ruta_datos)
    
    # Aplicar denoising usando wavelet
    señal_denoised = aplicar_wavelet_denoising(señal_ECG)
    
    # Crear un array de tiempo para graficar
    array_tiempo = np.linspace(0, len(señal_ECG) / frecuencia_muestreo, num=len(señal_ECG))
    
    # Graficar la señal original y la señal filtrada
    graficar_señales(señal_ECG, señal_denoised, array_tiempo, archivo.split('.')[0])


    

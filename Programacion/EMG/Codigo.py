import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Función para leer el archivo OpenSignals
def leer_senal_opensignals(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()
    
    # Encontrar el final del encabezado ('EndOfHeader')
    inicio_datos = 0
    for i, linea in enumerate(lineas):
        if 'EndOfHeader' in linea:
            inicio_datos = i + 1
            break
    
    # Cargar los datos desde el archivo (a partir del final del encabezado)
    data = pd.read_csv(archivo, delimiter='\t', skiprows=inicio_datos, header=None)
    
    # Suponiendo que la primera columna es el índice y la última columna es la señal de interés (A1)
    tiempo = np.arange(len(data)) / 1000  # Crear un vector de tiempo basado en la cantidad de muestras (1000 Hz)
    senal = data.iloc[:, -1]  # Última columna (A1)
    
    return tiempo, senal

# Función para graficar la señal
def graficar_senal(tiempo, senal, titulo="Señal A1 de OpenSignals"):
    plt.figure(figsize=(10, 6))
    plt.plot(tiempo, senal, label="A1")
    plt.title(titulo)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.legend()
    plt.xlim([1,2])     #Colocar limites para visualizar mejor la gráfica 
    plt.show()

# Leer y graficar la señal
while(1):
    archivo=input("Ingrese la dirección del archivo(Presione 1 para salir): ")
    # archivo = r"C:\Users\Lenovo\OneDrive\Escritorio\EMG\Movimiento_Biceps.txt"  
    if archivo=="1":
        break
    tiempo, senal = leer_senal_opensignals(archivo)
    graficar_senal(tiempo, senal)

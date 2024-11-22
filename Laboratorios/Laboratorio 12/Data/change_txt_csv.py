import os
import csv
import json

# Lista de archivos que quieres convertir
archivos_a_convertir = [
    "1D_basal", "1D_ejercicio", "1D_post_respiracion", "1D_respiracion",
    "2D_basal", "2D_ejercicio", "2D_post_respiracion", "2D_respiracion",
    "3D_basal", "3D_ejercicio", "3D_post_respiracion", "3D_respiracion",
    "60", "90", "120", "150"
]

# Encabezado que se usará para todos los archivos CSV
encabezado = ["nSeq", "I1", "I2", "O1", "O2", "A2"]

def convertir_txt_a_csv(archivo_txt, archivo_csv):
    """Convierte un archivo .txt a un archivo .csv con encabezado y datos separados por punto y coma"""
    
    with open(archivo_txt, 'r') as f:
        lines = f.readlines()
    
    # Buscar el índice donde termina el encabezado
    end_of_header_index = None
    for i, line in enumerate(lines):
        if line.strip() == '# EndOfHeader':
            end_of_header_index = i + 1
            break

    # Si no se encuentra '# EndOfHeader', asumir que no hay encabezado y usar todas las líneas
    if end_of_header_index is None:
        end_of_header_index = 0
    
    # Leer los datos después del encabezado
    data_lines = lines[end_of_header_index:]
    
    # Convertir los datos en filas separadas por espacios
    rows = [line.strip().split() for line in data_lines if line.strip()]
    
    # Verificar si hay datos antes de crear el archivo CSV
    if not rows:
        print(f"No se encontraron datos en {archivo_txt}")
        return
    
    # Guardar los datos en un archivo CSV utilizando punto y coma como delimitador
    with open(archivo_csv, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=';')
        
        # Escribir el encabezado
        csv_writer.writerow(encabezado)
        
        # Escribir las filas de datos en columnas separadas
        for row in rows:
            if len(row) == len(encabezado):
                csv_writer.writerow(row)
            else:
                print(f"Advertencia: La fila tiene un número incorrecto de columnas en {archivo_txt}")
    
    print(f"Archivo convertido exitosamente: {archivo_csv}")

def procesar_archivos():
    """Procesa todos los archivos especificados en la lista"""
    directorio_base = r"C:\Users\LENOVO\Desktop\ISB_lab_11\Laboratorios\Laboratorio 11\Data"
    directorio_salida = r"C:\Users\LENOVO\Desktop\ISB_lab_11\Laboratorios\Laboratorio 11\Data_csv"
    
    os.makedirs(directorio_salida, exist_ok=True)
    
    for nombre_archivo in archivos_a_convertir:
        archivo_txt = os.path.join(directorio_base, nombre_archivo + '.txt')
        archivo_csv = os.path.join(directorio_salida, nombre_archivo + '.csv')
        
        if os.path.exists(archivo_txt):
            convertir_txt_a_csv(archivo_txt, archivo_csv)
        else:
            print(f"Archivo no encontrado: {archivo_txt}")

# Ejecutar el procesamiento
procesar_archivos()

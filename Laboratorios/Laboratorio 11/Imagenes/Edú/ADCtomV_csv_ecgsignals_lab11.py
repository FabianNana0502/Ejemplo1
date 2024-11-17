import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def ADCtomV(ADC, n=10, VCC=3.3):
    volts = (((ADC / (2**n)) - (1/2)) * VCC) / 1009
    return volts * 1000

def process_and_plot(folder_path, sampling_rate):
    if not os.path.exists(folder_path):
        print("La carpeta no existe.")
        return
    
    txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    
    if not txt_files:
        print("No se encontraron archivos .txt en la carpeta.")
        return

    for file_name in txt_files:
        file_path = os.path.join(folder_path, file_name)
        print(f"Procesando: {file_name}")
        
        with open(file_path, 'r') as file:
            lines = file.readlines()
        header_end_index = next(i for i, line in enumerate(lines) if line.startswith("# EndOfHeader"))
        data_lines = lines[header_end_index + 1:]
        
        data = pd.DataFrame([line.split() for line in data_lines], dtype=float)
        fifth_column = data[5]
        mv_values = fifth_column.apply(ADCtomV)
        
        time = [i / sampling_rate for i in range(len(mv_values))]

        csv_file_name = os.path.splitext(file_name)[0] + ".csv"
        csv_file_path = os.path.join(folder_path, csv_file_name)
        processed_data = pd.DataFrame({'Tiempo (s)': time, 'Voltaje (mV)': mv_values})
        processed_data.to_csv(csv_file_path, index=False)
        print(f"Archivo guardado como: {csv_file_path}")

        fig, ax = plt.subplots()
        plt.subplots_adjust(bottom=0.25)
        l, = plt.plot(time, mv_values, label=f"Archivo: {file_name}")
        ax.set_title(f"Señal procesada: {file_name}")
        ax.set_xlabel("Tiempo (s)")
        ax.set_ylabel("Voltaje (mV)")
        plt.legend()

        ax_slider = plt.axes([0.2, 0.1, 0.65, 0.03])
        slider = Slider(ax_slider, 'Tiempo (s)', 0, len(time) / sampling_rate - 1, valinit=0, valstep=1/sampling_rate)

        def update(val):
            pos = slider.val
            ax.set_xlim(pos, pos + 1000 / sampling_rate)
            fig.canvas.draw_idle()
        
        slider.on_changed(update)
        plt.show()

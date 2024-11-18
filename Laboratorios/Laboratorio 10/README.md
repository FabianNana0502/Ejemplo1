# LABORATORIO 10: – Procesamiento de señales ECG
## Integrantes
- Fabian Alcides Ñaña Alfaro
- Christian Huarancca Quispe
- Ryoshin Cavero Mosquera
- Flavio Andreas Avendanho Cáceres
- Joao Marco Torres Rivera

## Contenido de la sesión

1. [Introducción](#id1)
2. [Objetivos](#id2)
3. [Metodología](id3)
4. [Resultados](#id4)  
5. [Discusión](#id5)  
6. [Conclusiones](#id6)  
7. [Bibliografia](#id7)
***


## Introducción <a name="id1"></a>
<div align="justify">
En previas presentaciones se habló del funcionamiento del Electrocardiograma (ECG) junto con la historia que hay detrás. Una vez extraída la información de los electrodos, el siguiente paso es el procesamiento de la señal para extraer características que sirvan de utilidad ser mencionadas. La extracción de los picos R se muestra muy útil para encontrar la frecuencia cardiaca evaluando el intervalo R-R. Algoritmos como Pan-Tompkins son muy útiles para indicar la frecuencia cardiaca en pacientes al usar los picos R extraídos de la señal, cuyo procedimiento fue detallado por El Yaakoubi[2]. Junto a las transformadas wavelet ambos algoritmos utilizan el filtrado como paso previo, sin embargo, las wavelets utilizan el componente frecuencial como una herramienta adicional. Según una investigación, las wavelets presentan un 99.8% de precisión de extracción del complejo QRS [3], otra por su parte realizó un conteo estadísticos de falsos negativos y falsos positivos llegando a un error de 0.24% y 0.39% respectivamente, usando la wavelet Daubechies 6 (Db6), presentandose asi como una de los mejores algoritmos para detección del complejo QRST [4]. La apliación de las wavelets requiere de un lenguaje de programación que pueda darle al usuario una representación visual de lo realizado. En este punto "Neurokit2" es una librería reciente, no tan antigua como los algoritmos ya mencionados, que mediante funciones usando lenguaje de programación python, nos permite una mejor visualización de lo que sucede en la señal ECG [5]. En este trabajo nos enfocaremos el uso de la librería "Neurokit2" en el procesamiento de nuestras señales ECG extraídas en un laboratorio pasado. Además del uso de algoritmos como Pan-Tompkins y técnicas de wavelet, el procesamiento de señales ECG se ha beneficiado significativamente de la aplicación de filtros adaptativos, los cuales permiten una cancelación de ruido más precisa y, por ende, una detección más confiable de arritmias [6]. Estos métodos avanzados han sido fundamentales para mejorar la calidad de las señales obtenidas en entornos clínicos, donde las interferencias y el ruido pueden afectar la precisión de los diagnósticos. Asimismo, los enfoques modernos en el procesamiento de señales bioeléctricas han evolucionado para incluir técnicas avanzadas que combinan análisis en el dominio del tiempo y de la frecuencia, facilitando la extracción de características críticas como los complejos QRS y otros componentes del ECG. En este contexto, el libro de Sörnmo y Laguna [7] proporciona una base exhaustiva sobre el procesamiento de señales bioeléctricas, cubriendo métodos avanzados para el análisis de ECG en aplicaciones tanto cardíacas como neurológicas. La integración de estos conocimientos en herramientas como "Neurokit2" permite un análisis detallado y visualmente accesible de las señales, brindando a los investigadores y profesionales de la salud una poderosa herramienta para la evaluación clínica.

## Objetivos <a name="id2"></a>
* Elección del mejor filtro Wavelet para ECG en base a búsqueda bibliográfica 
* Extracción de picos R-R de las señales.
* Verificar el comportamiento de la señal ECG.

## Metodología <a name="id3"></a>
<p style="text-align: justify;"> 

En este trabajo usaremos la librería "Neurokit2" en Python usando funciones específicas que sinteticen la labor del programador. Primero usaremos ecg_clean(), una función que limpia la señal de ruido que altere su comportamiento. 

```python

ecg_cleaned = nk.ecg_clean(ecg_signal, sampling_rate=sampling_rate)

```

Posterior a ello, se trabajará con la función ecg_peaks(), el cual, según al documentación, transforma datos de una lista en un dataframe con la ubicación de picos R marcados según el número de muestra tomado

```python

instant_peaks, rpeaks, = nk.ecg_peaks(ecg_cleaned, sampling_rate=1000)

```

Luego se utiliza la funcion, ecg_rate(), el cual calcula la frecuencia cardiaca respecto al número de muestra de la señal.

```python

rate = nk.ecg_rate(rpeaks, sampling_rate=1000, desired_length=len(ecg_cleaned))

```

Para finalizar, el último paso se divide el proceso en dos secciones para comparar los ploteos finales y su presentación de estos. La diferencia es que una sección utiliza la función ecg_quality para una presentación mejor y distinta que se va a visualizar en resultados

```python

quality = nk.ecg_quality(ecg_cleaned, sampling_rate=1000)

```

## Resultados: <a name="id4"></a>

### 1° Derivacion 
<table>
   <tr>
      <th>Estado del sujeto</th>    
      <th>Ploteo de la señal (usando ecg_plot)</th>
      <th>Ploteo de la señal</th>
   </tr>
   <tr>
      <td rowspan="1">Reposo</td>
      <td><img src="./Imagenes/1D_basal1.png"></td>
      <td><img src="./Imagenes/1D_basal2.png"></td>
   </tr>
   <tr>
        <td rowspan="1">Respiración</td>
        <td><img src="./Imagenes/1D_respiracion1.png"></td>
        <td><img src="./Imagenes/1D_respiracion2.png"></td>
    </tr>
    <tr>
        <td rowspan="1">Post_respiración</td>
        <td><img src="./Imagenes/1D_post_respiracion1.png"></td>
        <td><img src="./Imagenes/1D_post_respiracion2.png"></td>
    </tr>
    <tr>
        <td rowspan="1">Ejercicio</td>
        <td><img src="./Imagenes/1D_ejercicio1.png"></td>
        <td><img src="./Imagenes/1D_ejercicio2.png"></td>
    </tr>
</table>

### 2° Derivacion 
<table>
   <tr>
      <th>Estado del sujeto</th>    
      <th>Ploteo de la señal (usando ecg_plot)</th>
      <th>Ploteo de la señal</th>
   </tr>
   <tr>
      <td rowspan="1">Reposo</td>
      <td><img src="./Imagenes/2D_basal1.png"></td>
      <td><img src="./Imagenes/2D_basal2.png"></td>
   </tr>
   <tr>
        <td rowspan="1">Respiración</td>
        <td><img src="./Imagenes/2D_respiracion1.png"></td>
        <td><img src="./Imagenes/2D_respiracion2.png"></td>
    </tr>
    <tr>
        <td rowspan="1">Post_respiración</td>
        <td><img src="./Imagenes/2D_post_respiracion1.png"></td>
        <td><img src="./Imagenes/2D_post_respiracion2.png"></td>
    </tr>
    <tr>
        <td rowspan="1">Ejercicio</td>
        <td><img src="./Imagenes/2D_ejercicio1.png"></td>
        <td><img src="./Imagenes/2D_ejercicio2.png"></td>
    </tr>
</table>

### 3° Derivacion 
<table>
   <tr>
      <th>Estado del sujeto</th>    
      <th>Ploteo de la señal (usando ecg_plot)</th>
      <th>Ploteo de la señal</th>
   </tr>
   <tr>
      <td rowspan="1">Reposo</td>
      <td><img src="./Imagenes/3D_basal1.png"></td>
      <td><img src="./Imagenes/3D_basal2.png"></td>
   </tr>
   <tr>
        <td rowspan="1">Respiración</td>
        <td><img src="./Imagenes/3D_respiracion1.png"></td>
        <td><img src="./Imagenes/3D_respiracion2.png"></td>
   </tr>
   <tr>
        <td rowspan="1">Post_respiración</td>
        <td><img src="./Imagenes/3D_post_respiracion1.png"></td>
        <td><img src="./Imagenes/3D_post_respiracion2.png"></td>
   </tr>
   <tr>
        <td rowspan="1">Ejercicio</td>
        <td><img src="./Imagenes/3D_ejercicio1.png"></td>
        <td><img src="./Imagenes/3D_ejercicio2.png"></td>
   </tr>
</table>

<div align="justify">

## Discusión <a name="id5"></a>

### Variacion media del BPM segun derivada

<div align="center">

| Estado | 1ra Derivada | 2da Derivada | 3ra Derivada |
|:------:|:------------:|:------------:|:------------:|
| Reposo |      103     |      98      |      95      |
|Respiracion|    89     |      91      |      94      |
|Post-Respiracion| 93   |      92      |      92      |
|Ejercicio|     171     |      101     |      136     |

<div align="justify">

Al analizar los datos obtenidos sobre los bpm en cada estancia, se presentan frecuencias cardíacas elevadas en estado de reposo. Un reposo cercano a 100 bpm puede indicar taquicardia sinusal, especialmente si es recurrente, lo que podría estar asociado a estrés o incluso hipertensión como posibles productos del estres estudiantil, para el caso del sujeto analizado. 

Durante el ejercicio, el incremento a 171 bpm es elevado; aunque por debajo del rango normal (220 - edad) recomendado, teniendo en cuenta los valores atipicos del estado reposo, de haber experimentado alguna dificultad para recuperarse a niveles normales post-ejercicio, sería recomendable realizar un electrocardiograma especializado para descartar arritmias u otras afecciones a modo de recomendacion.

### Variacion del tamaño de intervalo R-R (ms)

<div align="center">

| Estado | 1ra Derivada | 2da Derivada | 3ra Derivada |
|:------:|:------------:|:------------:|:------------:|
| Reposo |      600     |      620      |     610     |
|Respiracion|    810    |      820      |     805     |
|Post-Respiracion| 520  |      490      |     500     |
|Ejercicio|     280     |      310      |     310     |

<div align="justify">

Para una correcta interpretacion debemos revisar los rangos de valores establecidos: en estado de reposo el intervalo R-R puede ser 700-850 ms, correspondiente a una frecuencia cardíaca de alrededor de 60-75 bpm. Al mantener la respiración, el intervalo crece a 800-1000 ms debido al aumento de la actividad vagal. En la fase de post-respiración, el intervalo vuelve poco a poco a los valores previos de reposo (600-750 ms). Tras el ejercicio, el intervalo R-R disminuye significativamente, pudiendo llegar a 400-550 ms (120-200 bpm) para satisfacer la demanda de oxígeno tras la actividad física. Si el intervalo tarda en regresar a más de 700 ms (frecuencia inferior a 85 bpm) en reposo tras el ejercicio, podría indicar una recuperación cardíaca lenta.

Segun los datos del sujeto analizado, y empleando los valores comparados con los rangos referenciales:

* Reposo: El intervalo R-R en la tabla muestra 600-620 ms, que es un poco bajo en comparación con el rango referencial de 700-850 ms. Esto indica una frecuencia cardíaca ligeramente más alta de lo esperado en reposo.
* En Respiración: Los valores están dentro del rango esperado de 800-1000 ms, lo cual es adecuado, reflejando una respuesta normal del sistema nervioso.

* Post-Respiración: El intervalo R-R se mantiene alrededor de 490-520 ms, un poco por debajo del rango referencial de recuperación , lo que podría sugerir una recuperación algo rápida o una ligera adaptación ineficiente.

* Ejercicio: El intervalo R-R entre 280-310 ms es menor que el rango referencial de 400-550 ms, lo que refleja una respuesta elevada al ejercicio, aunque todavía puede ser normal en actividades de alta intensidad.

Si bien los valores están cerca de los rangos normales, hay dificultades para recuperarse dde la actividad fisica, por lo cual se recomienda mayor actividad , ya que la rutina (baja) de actividad fisica podria ser la causa subyacente

Todas estas caracterisitcas del ECG nos facilitan un analisis y prevencion de cardiopatias


## Bibliografía<a name="id7"></a>
 
[1] J. Pan y W. J. Tompkins, “A Real-Time QRS Detection Algorithm”, IEEE Trans. Biomed. Eng., vol. BME-32, núm. 3, pp. 230–236, 1985. 
https://ieeexplore.ieee.org/document/4122029

[2] N. A. El Yaakoubi, "Procesamiento del complejo QRS característico del electrocardiograma (ECG)", Tutor: F. J. Mata Contreras, Escuela Técnica Superior de Ingeniería Informática, Universidad de Málaga, Departamento de Ingeniería de Comunicaciones, Málaga, España, Junio, 2020. 
https://riuma.uma.es/xmlui/bitstream/handle/10630/20493/Amrani%20El%20Yaakoubi%20Nissrin%20Memoria.pdf?sequence=1 

[3] C. Li, C. Zheng, y C. Tai, “Detection of ECG characteristic points using wavelet transforms”, IEEE Trans. Biomed. Eng., vol. 42, núm. 1, pp. 21–28, 1995.
https://ieeexplore.ieee.org/abstract/document/362922
 
[4] S. Pal y M. Mitra, “Detection of ECG characteristic points using Multiresolution Wavelet Analysis based Selective Coefficient Method”, Measurement (Lond.), vol. 43, núm. 2, pp. 255–261, 2010.
https://www.sciencedirect.com/science/article/abs/pii/S0263224109002139

[5] Makowski, D., Pham, T., Lau, Z. J., Brammer, J. C., Lespinasse, F., Pham, H.,
Schölzel, C., & Chen, S. A. (2021). NeuroKit2: A Python toolbox for neurophysiological signal processing.
Behavior Research Methods, 53(4), 1689–1696. 
https://doi.org/10.3758/s13428-020-01516-y

[6] N. V. Thakor and Y. S. Zhu, "Applications of adaptive filtering to ECG analysis: noise cancellation and arrhythmia detection," IEEE Transactions on Biomedical Engineering, vol. 38, no. 8, pp. 785-794, Aug. 1991, doi: 10.1109/10.83591.
[7] L. Sörnmo and P. Laguna, Bioelectrical Signal Processing in Cardiac and Neurological Applications, Biomedical Engineering. Elsevier, 2005.





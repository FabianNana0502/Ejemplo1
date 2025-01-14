# LABORATORIO 6: – Uso de EEG usando BITalino y Ultracortex Mark IV:
## Integrantes
- Fabian Alcides Ñaña Alfaro
- Christian Huarancca Quispe
- Ryoshin Cavero Mosquera
- Flavio Andreas Avendanho Cáceres
- Joao Marco Torres Rivera

## Contenido de la sesión
1. [Introducción](#id1)
2. [Objetivos](#id2)
3. [Materiales y equipos](#id3)
4. [Metodologia](#id4)
5. [Resultados](#id5)  
   5.1 [EEG alumno](#id6)  
   5.2 [EEG profesor ](#id7)  
6 [Discucion](#id8)  
7 [Resultado](#id9)  
8 [Bibliografia](#id10)

## Introducción <a name="id1"></a>
   ### ¿Qué es un EEG?  
<p style="text-align: justify;">                  
   Un Electroencefalograma (EEG) es una prueba que mide la actividad eléctrica del cerebro, ya que utiliza los impulsos electricos de las neuronas para comunicarse. Además se encuentra en el orden de los microvoltios(uV)[1].

   El examen consiste en la colocación de electrodos en varios lugares del cuero cabelludo como en la parte frontal de la cabeza. Luego se procede a capturar la señal mientras el paciente está despierto o incluso durmiendo[2]. Por último se realiza un filtrado dependiendo del ritmo de EEG que se quiera analizar de la señal.

   ### Conceptos Previos
<p style="text-align: center;">
   
   _"El cerebro es el único órgano que se intenta explicar a sí mismo"_

<p style="text-align: justify;">    
   El cerebro es el órgano ubicado dentro de la corteza cranela que está compuesto de mil millones de  neuronas que coordinan pensamientos, conductas, etc. Es la parte más grande del encéfalo y está dividido por surcos en 2 hemisferios. Cada hemisferio presenta 6 lóbulos, aunque algunos autores consideran solo 4, los cuales se presentan a continuación:
   
   * Lóbulos frontales: Se encargan de las funciones motoras, movimientos, emocione.
   * Lóbulos parietales: Se encargan de los sentidos, de la visión, el tacto y de la orientación espacial y temporal.
   * Lóbulo temporal: Está asociado al habla, la audición y a la memoria de corto plazo.
   * Lóbulo occipital: Está asociado al sistema visual, gestos y expresiones.
   * Insula: Está asociado al habla y la información sensitiva y autónoma de las vísceras.
   * Lóbulo límbico: Reciben conexiones de diversas áreas del encéfalo que están interrelacionados [3,4]. 
<div align="center">

   ![Figura 1](https://cdn1.imaios.com/i/images/8/2/7/2/472728-4-esl-ES/brain-illu-cerebral-lobes.jpg?q=75&w=1280&s=5d6bd697dae034d4abe61a186002bf79)

   Figura 1. Ubicación de los lóbulos [8]

</div>

<p style="text-align: justify;">

   Para visualizar cuáles son las porciones del cerebro que se activan cuando se realiza cualquier acción se requiere un EEG. La señal presenta distintas oscilaciones con bandas de frecuencias definidas pero no uniformizadas por todos los autores [5]. Estas son:

   * Gamma: 30-50 Hz. Son las ondas más rápidas. Ocurren en ráfagas cortas. Están relacionados con el proceso de información simultánea en varias áreas del Sistema Nervioso Central. Se observan estallidos de ondas gamma cuando el cerebro se encuentra en un estado de alta resolución. 
   * Beta: 12-30 Hz. Predominan durante el período de vigilia. La frecuencia es rápida, está presente cuando estamos atentos e implicados en la resolución de tareas o problemas diarios, también durante la toma de decisiones o cuando estamos concentrados.
   * Alpha: 8-12 Hz. Predominan cuando el Sistema Nervioso Central está en reposo, relajado pero despierto y atento.
   * Theta: 4-8 Hz. Predominan cuando los sentidos están procesando información interna y el individuo está desconectado del mundo exterior, absorto. Fase 3 sueño no REM
   * Delta: 0.5-4 Hz. Son características de cuando el individuo está dormido y predominan durante el sueño. Fase 4 sueño REM.

   Algunos autores difieren en 1 o 2 Hz de las bandas de frecuencia de acuerdo a la distribución anterior. Como por ejemplo: Beta: de 13-30 Hz [6].

<div align="center">

   ![Figura 2](https://i2.wp.com/psicoterapeutas.eu/imagenes-psicoterapeutas-eu/Electroencefalograma.jpg?w=311&ssl=1)

Figura 2. Ritmos EEG. [7]

</div>


## Objetivos <a name="id2"></a>
* Obtener señales de electroencefalograma utilizando el arreglo de electrodos UltraCortex MARK IV y la tarjeta de biosensado Cyton de 8 canales.
* Obtener una señal de electroencefalograma utilizando el Kit BITalino (R)evolution.
* Analizar y plotear las señales obtenidas utilizando Python.

## Materiales y equipos <a name="id3"></a>

| Material     |Descripción      |Cantidad   |
|-----------   |:------------:   |:---------:|
|Mark IV       | Ultracortex     |1          |  
| (R)Evolution |Kit BITalino[4]  |1          |
| Laptop       |Laptop           |1          |
| Electrodos   |Electrodos EEG   |3          |
|Cyton         |Tarjeta biosensado|1         |

![Bitalino](https://www.pluxbiosignals.com/cdn/shop/products/BITalino-Plugged-Board.1.jpg?v=1718709938&width=720 "BiTAalino")

<p style="text-align: center;">  
   Figura 3. BITalino. Fuente: BITalino (r)evolution.
<p>

## Metodología <a name="id4"></a>
<div align="justify">
Para el registro de EEG se usaron 2 voluntarios para 2 tipos de procedimientos similares, pero con equipamiento distintos. En ambos realizaron los siguientes 5 pasos detallados a continuación:

1. Registrar una línea base de señal con poco ruido y sin movimientos (respiración normal junto con ojos cerrados) durante 30 segundos.
2. Repetir un ciclo de OJOS ABIERTOS - OJOS CERRADOS cinco veces, manteniendo ambas fases durante cinco segundos.
3. Registrar otra fase de referencia de 30 segundos (paso 1)
4. Otro compañero leerá una serie de ejercicios matemáticos (3 simples y 3 complejos), mientras el voluntario resolverá los ejercicios mirando a un punto fijo.
5. Detener la grabación y guardar datos.

El primer procedimiento consistió en la captura de un EEG mediante el Kit BITalino (R)evolution con la laptop y para ello se siguió la siguiente secuencia:

1. Descarga de la plataforma OpenSignals.
2. Alimentación de la tarjeta BITalino utilizando una batería de litio incluida en el kit de compra.
3. Conexión de los 3 electrodos (Positivo, Negativo y Referencia) a la placa de sensado a través de un conector hacia el canal de sensado de EEG.
4. Conectar por Bluetooth a la tarjeta BITalino con la laptop.

Una vez realizadas las conexiones, se procedió a colocar 2 electrodos en la parte frontal de la cabeza, por encima de cada ceja y 1 electrodo que sirve de referencia por debajo de la oreja derecha, tal como se detalla en la figura 4. Una vez finalizadas las conexiones se procedió a realizar los pasos mencionados al inicio.
</div>
<div align="center">

![Figura 4](./Imagenes/EEG%20placement.png)

Figura 4. Colocación electrodos EEG. Fuente: BITalino Home Guide
</div>

---

<div align="justify">
El segundo procedimiento usó el UltraCortex MARK IV junto a la Tarjeta Cyton y para ello se siguió la siguiente secuencia:

1. Descarga de la plataforma OpenBCI GUI.
2. Alimentación de la tarjeta Cyton utilizando una batería de litio incluida en el kit de compra.
3. Conexión del UltraCortex MARK IV con la tarjeta Cyton.
4. Ajuste del UltraCortex en la cabeza del voluntario (profesor Moises) siguiendo el sistema 10-20 de posicionamiento de electrodos, como se visualiza en la figura 5.
5. Conexión de la laptop y la tarjeta Cyton.

Una vez realizadas las conexiones, se procedió a realizar los pasos mencionados al inicio de Metodología.
</div>
<div align="center">

![Figura 5](./Imagenes/Colocacion%20Ultracortex.jpeg)
Figura 5. Colocacion del ULTRACORTEX en el voluntario.
</div>


<div align="justify">




### Proceso de Filtrado
Una vez definido el procedimiento, el siguiente paso es realizar el código en Visual Studio Code para el filtrado de la señal resultante. Este proceso se dividió en dos etapas: 

El primer paso del filtrado fue la aplicación de un filtro notch centrado en 60 Hz. Este filtro se utilizó para eliminar la interferencia de la red eléctrica, una fuente común de ruido en los registros ECG, EEG y EMG. Al eliminar estas frecuencias no deseadas, se obtuvo una señal más limpia, lo que es crucial para un análisis fiable de la actividad cardiaca.

El segundo paso fue aplicar un filtro pasa banda con un rango de 0.5 a 100 Hz. Este rango de frecuencia fue elegido para aislar las frecuencias relevantes de la señal ECG, eliminando los ajenos a la señal ECG . Este procedimiento es esencial para mejorar la calidad de la señal y su representatividad de ella. Por ejemplo, Lorenzo (2015) [5] emplearon un filtrado similar (0.5-100 Hz) en su estudio para obtener señales ECG claras y útiles.


### Código usado en Python
<div align="justify">

El código realiza un completo proceso de adquisición, preprocesamiento y visualización de señales electromiográficas (ECG) capturadas utilizando el sistema BITalino y OpenSignals. A continuación, se detallan los procesos de filtrado, con su respectiva justificación, que se llevaron a cabo en el código:

1. **Conversión de la Señal ADC a Milivoltios (uV):**
   
   La función `ADCtomV` se utiliza para convertir la señal digital (ADC) a analógico (voltaje en milivoltios (mV)). Dado que la señal se obtiene en formato ADC, es necesario convertirla a un formato más comprensible (milivoltios) para analizar la amplitud real de la señal ECG. Esta conversión es crucial para asegurar que los datos se interpreten correctamente y se puedan comparar con otros estudios electromiográficos.

2. **Remoción del Componente DC:**
   
   Antes de aplicar cualquier filtrado, se realiza una remoción del componente DC de la señal. Este paso implica restar el valor promedio de la señal para eliminar cualquier desplazamiento en el nivel base. La presencia de un componente DC podría distorsionar los resultados del filtrado posterior y la representación de la señal. La remoción del componente DC garantiza que las etapas de filtrado subsiguientes no se vean afectadas por un nivel base elevado.

3. **Filtrado Pasa Banda (Bandpass Filter):**
   
   Se aplica un filtro pasa banda utilizando la función `butter_bandpass_filter`, que emplea el diseño de filtros Butterworth. Este filtro se diseña con una frecuencia de corte inferior de 0.5 Hz y una frecuencia de corte superior de 100 Hz. El objetivo de este filtrado es eliminar las componentes de baja frecuencia (como el ruido de movimiento y la línea base) y las componentes de alta frecuencia que suelen estar asociadas con el ruido eléctrico o artefactos no deseados. El uso del filtro pasa banda permite aislar las frecuencias relevantes de la señal ECG que se encuentran dentro de este rango, proporcionando una representación más precisa de la actividad cardiaca.

4. **Filtrado Notch para Eliminar Ruido de Red Eléctrica:**
   
   Después del filtrado pasa banda, se aplica un filtro notch (rechaza bandas específicas de frecuencias) centrado en 60 Hz mediante la función `iirnotch`. La frecuencia de 60 Hz corresponde al ruido de la red eléctrica que es común en los registros electromiográficos. Este ruido puede interferir con la señal ECG, haciendo que sea difícil distinguir las características de la señal. El filtro notch elimina este ruido específico, resultando en una señal más limpia y más representativa de la actividad muscular verdadera.

5. **Visualización de la Señal:**
   
   Una vez que la señal ha sido filtrada, se procede a su visualización en tres subgráficos:
     - **Señal Original:** Muestra la señal convertida a mV antes del filtrado.
     - **Señal Filtrada:** Muestra la señal después de los procesos de filtrado (pasa banda y notch), destacando cómo el filtrado mejora la claridad de la señal ECG.


## Resultados <a name="id5"></a>
***
### EEG del alumno<a name="id6"></a>
***
|**EEG alumno - Estado Basal**|**EEG alumno - Parpadeos (lapsos 5 segundos)**|
|:---------------------------:|:------------------------:|
|![video1](http://img.youtube.com/vi/GpzFBP9PeDw/0.jpg)("https://youtu.be/GpzFBP9PeDw")|![video1](http://img.youtube.com/vi/yvh0mibmzds/0.jpg)("https://youtube.com/shorts/yvh0mibmzds")|
|**EEG alumno - 2do Estado Basal**|**EEG alumno - Ejercicios mentales (total)**|
|![video1](http://img.youtube.com/vi/2i9HHr30mw0/0.jpg)("https://youtube.com/shorts/2i9HHr30mw0")|![video1](http://img.youtube.com/vi/fh9nf8_U0Es/0.jpg)("https://youtu.be/fh9nf8_U0Es")|
***

|**EEG alumno - Estado Basal**|**EEG alumno - Parpadeos (lapsos 5 segundos)**|
|:---------------------------:|:------------------------:|
|<img src="./Ploteos/EstadoBasal.jpeg" width="600" height="300">|<img src="./Ploteos/Parpadeos.jpeg" width="600" height="300"> |
|**EEG alumno - 2do Estado Basal**|**EEG alumno - Ejercicios mentales (total)**|
|<img src="./Ploteos/EstadoBasal2.jpeg" width="600" height="300">|<img src="./Ploteos/EjerciciosMentales.jpeg" width="600" height="300">|


### EEG del profesor<a name="id7"></a>
***
|**EEG profesor - Estado Basal**|**EEG profesor - Parpadeos (lapsos 5 segundos)**|
|:---------------------------:|:------------------------:|
|![video1](http://img.youtube.com/vi/DEUQdwvzWDg/0.jpg)("https://youtu.be/DEUQdwvzWDg")|![video1](http://img.youtube.com/vi/_X7cUqVrU60/0.jpg)("https://youtu.be/_X7cUqVrU60")|
|**EEG profesor - 2do Estado Basal**|**EEG profesor - Ejercicios mentales (total)**|
|![video1](http://img.youtube.com/vi/Zm6OFPL9uPM/0.jpg)("https://youtu.be/Zm6OFPL9uPM")|![video1](http://img.youtube.com/vi/FpcMIeKeOmc/0.jpg)("https://youtu.be/FpcMIeKeOmc")|
***

|**EEG profesor - Estado Basal**|**EEG profesor - Parpadeos (lapsos 5 segundos)**|
|:---------------------------:|:------------------------:|
|<img src="./Ploteos/BCI/Estado_basal_1.png" width="600" height="300">|<img src="./Ploteos/BCI/parpadeo.png" width="600" height="300">|
|**EEG profesor - 2do Estado Basal**|**EEG profesor - Ejercicios mentales (total)**|
|<img src="./Ploteos/BCI/Estado_basal_2.png" width="600" height="300">|<img src="./Ploteos/BCI/Preguntas_ploteos/Preguntas_82_final_s.png" width="600" height="300">|
***

### Aclaracion: la imagen BCI de ejercicios mentales corresponde a las preguntas dificiles

<div align="justify">

## Discusión <a name="id8"></a>
***
### Análisis señal en estado basal

En esta gráfica, se observa una representación de la señal EEG en basal , es decir , en condición de reposo y sin movimientos oculares , la señal está ploteada en un intervalo de 0 a 15 segundos . La  señal obtenida muestra una variabilidad considerable, con picos que se extienden a lo largo de un rango de amplitudes que van desde aproximadamente -40 µV a +40 µV. 

<div align="center">

<img src="./Ploteos/Discu1.png" alt="1D Basal" width="1000" height="200">

Fig 6. EEG de alumno - estado basal

<div align="justify">

### Análisis señal durante pestañeo

Se observan diferencias significativas con respecto a la señal en estado basal , en la señal se observan numerosos picos, tanto positivos como negativos, que se extienden más allá de la actividad EEG en reposo, posiblemente indicando los momentos en los que el usuario parpadeó . Estos artefactos por parpadeo son comúnmente más grandes que la actividad eléctrica cerebral típica y pueden identificarse por sus formas características de gran amplitud.

<div align="center">

<img src="./Ploteos/Discu2.png" alt="1D Basal" width="1000" height="200">

Fig 7. EEG de alumno - Parpadeos

<div align="justify">

### Análisis durante preguntas 

En la primera gráfica, la señal EEG muestra variaciones de amplitud considerables, con valores que oscilan entre aproximadamente -40 y +40 µV. Estas fluctuaciones sugieren una la detección de actividad cerebral dinámica, posiblemente debido a la carga cognitiva de responder a las preguntas planteadas . 

<div align="center">

<img src="./Ploteos/Discu4.png" alt="1D Basal" width="1000" height="200">

Fig 8. EEG de alumno - ejercicios mentales

<img src="./Ploteos/Discu5.png" alt="1D Basal" width="1000" height="200">

Fig 9. EEG de alumno - ejercicios (ventana 0-75)

<div align="justify">

En la segunda imagen, que muestra un intervalo más corto de 0 a 75 segundos , las variaciones de la señal son evidentes con la diferente aparición de picos positivos y negativos. Esta gráfica representa  respuestas cerebrales a momentos específicos de resolución de problemas que fueron planteados, donde la actividad mental es más intensa . Asimismo,el nivel de las preguntas fue aumentando con respecto a la dificultad.

## Análisis de los resultados en OpenBCI
Fisiológicamente , las neuronas se comunican entre sí mediante pequeños impulsos eléctricos que pueden medirse. A estas las llamamos ondas cerebrales. Estas ondas tienen diferentes tipos de frecuencias, algunas son más rápidas y otras más lentas. Si se separan mediante filtros podremos observarlos con mayor claridad.
Hemos empleado el electroencefalograma (EEG) para registrar  la actividad eléctrica del cerebro a través de sensores colocados en el cuero cabelludo para ver estos potenciales eléctricos en forma de ondas.

Las ondas mas importantes en un EEG son:

**Ondas Gamma**: Resaltan en situaciones de alta actividad cognitiva, concentracion y procesado de información, se ubican de 30-100 Hz

**Ondas Beta**: presentes en situaciones de alerta o repentina alerta , en un rango de 12-30 Hz.

**Ondas Alfa**: Durante momentos de relajación o vigilia y descanso, a ojos cerrados, 8-12 Hz.

**Ondas Theta**: asociadosa a la somnolencia, la meditación durante las fases ligeras del sueño a 4-8 Hz.

**Ondas Delta**: Presentes en sueño profundo (no REM) a 0.5-4 Hz.

**Ondas Lambda**: ondas muy breves, que surgen cuando se dirige la vista hacia un nuevo estímulo visual.

**Ondas K-complejas**: Particulares del sueño y surgen en la segunda fase del sueño NO REM. 

<div align="center">

<img src="./Ploteos/BCI/Estado_basal_1.png" width="600" height="300">

Fig 10. OpenBCI - estado basal

<div align="justify">

Al obtener el EEG durante un estado de reposo, de todas las ondas, la mas predominante son las ondas Alfa, ya que si bien la persona esta muy relajada y a ojos cerrados, esta aun despierta, ademas, debido a que el ambiente donde se reaalizo la medicion contenia a un numero considerable de personas, la persona tuvo la influecnia de ruido externo, lo cual limitó la aparicion de ondas theta, las cuales podrian haber aparecido, de haber estado en un ambiente con  el minimo de ruido o interferencias ajenas.

<div align="center">

<img src="./Ploteos/BCI/parpadeo.png.png" width="600" height="300">

Fig 11. OpenBCI - Parpadeo

<div align="justify">

Al abrir y cerrar los ojos en periodos simétricos, generan un patrón de ingreso de nueva informacion a traves de los ojos, lo cual se puede pareciar en la secuencia de picos en todos los canales. Estos rapidos y alternados ingresos de informacion se pueden observar con la prescenia de ondas beta en forma de picos intensos pero esporadicos justo en los instantes de apertura de los ojos, presente en la mayoria de los canales, a su vez de la aparicion de breves ondas alfa al momento de cerrar los ojos ya que por breves instantes la persona reposa los ojos y por ende su procesamiento de información.

<div align="center">

|**Ejercicios mentales simples**|**Ejercicios mentales difíciles**|
|<img src="./Ploteos/BCI/Preguntas_ploteos/Preguntas_12_22_s.png" width="600" height="300">|<img src="./Ploteos/BCI/Preguntas_ploteos/Preguntas_82_final_s.png" width="600" height="300">|

Tabla 1. Comparacion ejercicos faciles-dificiles

<div align="justify">
   
Al realizar las preguntas "sencillas" vemos un gran aumento de ondas beta, picos cortos y altamente repetitivos, los cuales indican el aumento de actividad cerebral debido a la exigencia requerida para resolver los acertijos planteados. Pero al pasar a la mitad de tiempo, momento en el cual se realizan las preguntas de nivel complejo, se observa la aparente presencia de ondas gamma, ya que la persona requiere un alto nivel de concentración y enfoque para poder resolver las preguntas con información compleja, activando mutiles areas del cerebro, representado con las presencia multiples y recurrentes picos en todos los canales.

## Conclusión <a name="id9"></a>

El estudio de la actividad eléctrica cerebral, utilizando el electroencefalograma y las técnicas subsiguientes de filtrado, ha permitido lograr una caracterización más específica de las señales obtenidas. De particular relevancia fue la implementación de los filtros pasa banda, para minimizar la potencial interferencia entre frecuencias y fuera de la gama fisiológica relevante. 

En la condición basal, durante la cual el sistema nervioso central estaba en reposo y libre de artefactos de movimiento ocular, la señal de EEG demostró estabilidad, manteniendo amplitud dentro de los límites típicos para la señal de onda alfa. Este resultado es esperable, ya que la literatura científica sostiene que, durante la vigilia relajada, las ondas alfa prevalecen en todas las áreas corticales, y la ausencia de cargas de trabajo significativas está asociada con la disminución de la necesidad de procesamiento neural. 

Por otro lado, durante las series parpadeantes, las amplitudes de señal notables, en particular los artefactos, se observaron regularmente. Los eventos con amplitudes superiores a ±40 fueron definidos como artefactos, apoyando la literatura científica que indica que la interferencia de movimiento supresor es generalmente de magnitud en la mayoría de las frecuencias. Se filtraron y fueron disminuidos por el proceso de filtrado; sin embargo, la completa eliminación del ruido motriz podría ser imposible sin la aplicación del Análisis de Componentes Independientes. Durante los desafíos cognitivos, la amplitud y el rango de señales EEG observadas fueron significativamente diferentes entre los sujetos.
En el análisis cognitivo durante la resolución de preguntas, se observaron variaciones significativas en la amplitud y frecuencia de las señales EEG, lo que sugiere una mayor activación neuronal en respuesta a la carga cognitiva. Las fluctuaciones en el rango de ±40 µV, con una predominancia de las ondas beta (12-30 Hz), refuerzan la hipótesis de una mayor actividad cortical durante la toma de decisiones y el procesamiento de información, consistente con la literatura que asocia las oscilaciones beta con tareas cognitivas y de atención.

El uso del sistema OpenBCI y el posterior procesamiento de los datos ha demostrado ser útil para la captura y visualización de las señales EEG. La conversión de las señales digitales ADC a unidades de voltaje (µV) fue esencial para una correcta interpretación de las amplitudes, permitiendo comparaciones fiables con estudios previos. Además, la remoción del componente DC y la aplicación de un filtro Butterworth de cuarto orden contribuyeron a la fidelidad de las señales procesadas, eliminando desplazamientos de la línea base y artefactos de baja frecuencia que podrían comprometer los resultados.

## Bibliografía<a name="id10"></a>

[1] https://www.mayoclinic.org/es/tests-procedures/eeg/about/pac-20393875

[2] https://medlineplus.gov/spanish/ency/article/003931.htm

[3]https://www.msdmanuals.com/es-pe/professional/trastornos-neurol%C3%B3gicos/funci%C3%B3n-y-disfunci%C3%B3n-de-los-l%C3%B3bulos-cerebrales/generalidades-sobre-la-funci%C3%B3n-cerebral

[4]https://www.mayoclinic.org/es/diseases-conditions/epilepsy/in-depth/brain/art-20546821

[5]https://www.msdmanuals.com/es-pe/professional/trastornos-neurol%C3%B3gicos/pruebas-y-procedimientos-neurol%C3%B3gicos/electroencefalograf%C3%ADa-eeg

[6]https://fisiologia.facmed.unam.mx/index.php/fisiologia-de-la-actividad-electrica-del-cerebro-electroencefalografia/

[7]https://psicoterapeutas.eu/electroencefalograma/electroencefalograma-2/

[8]https://doi.org/10.37019/e-anatomy/49401.es 

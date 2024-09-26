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
   5.1 [Implementación](#id6)  
   5.2 [ECG Estado Basal](#id7)  
   5.3 [ECG Respiracion](#id8)  
   5.4 [ECG Post-respiración](#id9)  
   5.5 [ECG Post-ejercicio](#id10)
   5.6 [Discusión](#id11)  
   5.7 [Conclusión](#id12)

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
   Figura 1. Ubicación de los lóbulos. Fuente: ![IMAIOS](https://doi.org/10.37019/e-anatomy/49401.es)

</div>

<p style="text-align: justify;">

   Para visualizar cuáles son las porciones del cerebro que se activan cuando se realiza cualquier acción se requiere un EEG. La señal presenta distintas oscilaciones con bandas de frecuencias definidas pero no uniformizadas por todos los autores [5]. Estas son:

   * Gamma: 30-50 Hz. Son las ondas más rápidas. Ocurren en ráfagas cortas. Están relacionados con el proceso de información simultánea en varias áreas del Sistema Nervioso Central. Se observan estallidos de ondas gamma cuando el cerebro se encuentra en un estado de alta resolución. 
   * Beta: 12-30 Hz. Predominan durante el período de vigilia. La frecuencia es rápida, está presente cuando estamos atentos e implicados en la resolución de tareas o problemas diarios, también durante la toma de decisiones o cuando estamos concentrados.
   * Alpha: 8-12 Hz. Predominan cuando el Sistema Nervioso Central está en reposo, relajado pero despierto y atento.
   * Theta: 4-8 Hz. Predominan cuando los sentidos están procesando información interna y el individuo está desconectado del mundo exterior, absorto. Fase 3 sueño no REM
   * Delta: 0.5-4 Hz. Fase 4 sueño REM.

   Algunos autores difieren en 1 o 2 Hz de las bandas de frecuencia de acuerdo a la distribución anterior. Como por ejemplo: Beta: de 13-30 Hz [6].

<div align="center">

   ![Figura 2](https://www.researchgate.net/profile/Salvador-Ruiz/publication/302589558/figure/fig2/AS:363428171534338@1463659436281/Figura-3-Ritmos-electroencefalograficos_W640.jpg)

Figura 2. Ritmos EEG. Fuente: ![ResearchGate](https://www.researchgate.net/publication/302589558_El_sueno_en_los_animales)

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

1. **Conversión de la Señal ADC a Milivoltios (mV):**
   
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


## Implementación <a name="id6"></a>
***
### Click on images to visualize the videos
***
|  **ECG ESTADO BASAL DERIVADA I**  | **AGUANTANDO RESPIRACION I DERIVADA** | **POST AGUANTANDO RESPIRACION I DERIVADA** |
|:------------:|:---------------:|:------------:|
|https://drive.google.com/file/d/1p2DJ1yurO03lyf1WLENLBMfI_1ryaaga/view?usp=sharing|https://drive.google.com/file/d/1XMZoKpcnTuxhg_tEjeOoiogzPngMHLph/view?usp=sharing|https://drive.google.com/file/d/1b1P5wtIn3Z_EkZo2kRRaPBTHnOEAG4kf/view?usp=sharing|
***
|  **ECG ESATDO BASAL DERIVADA II**  | **AGUANTANDO RESPIRACION II DERIVADA** | **POST AGUANTANDO RESPIRACION II DERIVADA** |
|:------------:|:---------------:|:------------:|
|https://drive.google.com/file/d/1jaC2D8yFGBopVKKNw3IYkY0D37EabJwE/view?usp=sharing|https://drive.google.com/file/d/1mqaD4aCkCTAIjIJ9RPzYXFef1Ft-FPMm/view?usp=sharing|https://drive.google.com/file/d/1r-0VkqwXQIehlsraf-jBD4w9jbQ8fBJv/view?usp=sharing|
***
|  **ECG ESTADO BASAL DERIVADA III**  | **AGUANTANDO RESPIRACION III DERIVADA** | **POTS AGUANTANDO RESPIRACION III DERIVADA** |
|:------------:|:---------------:|:------------:|
|https://drive.google.com/file/d/1yk-53DK0n22BtcBRoVvy0dsy8XzD0VUf/view?usp=sharing|https://drive.google.com/file/d/1wC7PeMzJzvqW8g1-2qVQ0sneYnBQAkmb/view?usp=sharing|https://drive.google.com/file/d/1RbyMZvDXfzYS9dE3VyYx9i_ixWKZgRk9/view?usp=sharing|

|  **POST ACTIVIDAD FISICA DERIVADA I**  | **POST ACTIVIDAD FISICA DERIVADA II** | **POST ACTIVIDAD FISICA DERIVADA III** |
|:------------:|:---------------:|:------------:|
|https://drive.google.com/file/d/1b1P5wtIn3Z_EkZo2kRRaPBTHnOEAG4kf/view?usp=sharing|https://drive.google.com/file/d/1HbuAkgelLQ-kvIb1587E0uSX8-gCoEuw/view?usp=sharing|https://drive.google.com/file/d/1jbfdfQTVNpSUcHV2uwGyTq0MDReXjOck/view?usp=sharing|


## ECG Estado Basal <a name="id7"></a>

| **Derivada 1 Estado Basal** | 
![D1reposo](./Ploteos/1D_basal.png)
| **Derivada 2 Estado Basal** |
![D2reposo](./Ploteos/2D_basal.png) 
| **Derivada 3 Estado Basal** |
![D3reposo](./Ploteos/3D_basal.png)

## ECG Respiración <a name="id8"></a>

| **Derivada 1 Respiración** | 
|![D1respiracion](./Ploteos/1D_respiracion.png)|  
| **Derivada 2 Respiración** |
|![D2respiracion](./Ploteos/2D_respiracion.png)| 
| **Derivada 3 Respiración** |
|![D3respiracion](./Ploteos/3D_respiración.png)| 

## ECG Post-respiración <a name="id9"></a>

| **Derivada 1 Post-respiración** | 
|![D1post](./Ploteos/1D_post_respiracion.png)| 
| **Derivada 2 Post-respiración** |
|![D2post](./Ploteos/2D_post_respiracion.png)| 
| **Derivada 3 Post-respiración** |
|![D3post](./Ploteos/3D_post_respiracion.png)| 

## ECG Post-ejercicio <a name="id10"></a>

| **Derivada 1 Post-ejercicio** | 
|![D1ejercicio](./Ploteos/1D_ejercicio.png)| 
| **Derivada 2 Post-ejercicio** |
|![D2ejercicio](./Ploteos/2D_ejercicio.png)| 
| **Derivada 3 Post-ejercicio** |
|![D3ejercicio](./Ploteos/3D_ejercicio.png)| 


## Discusión <a name="id11"></a>


## Conclusión <a name="id12"></a>


## Bibliografía

[1] https://www.mayoclinic.org/es/tests-procedures/eeg/about/pac-20393875

[2] https://medlineplus.gov/spanish/ency/article/003931.htm

[3]https://www.msdmanuals.com/es-pe/professional/trastornos-neurol%C3%B3gicos/funci%C3%B3n-y-disfunci%C3%B3n-de-los-l%C3%B3bulos-cerebrales/generalidades-sobre-la-funci%C3%B3n-cerebral

[4]https://www.mayoclinic.org/es/diseases-conditions/epilepsy/in-depth/brain/art-20546821

[5]https://www.msdmanuals.com/es-pe/professional/trastornos-neurol%C3%B3gicos/pruebas-y-procedimientos-neurol%C3%B3gicos/electroencefalograf%C3%ADa-eeg

[6]https://fisiologia.facmed.unam.mx/index.php/fisiologia-de-la-actividad-electrica-del-cerebro-electroencefalografia/


# LABORATORIO 8: – Teoria y aplicacion de la Transformada Wavelet
## Integrantes
- Fabian Alcides Ñaña Alfaro
- Christian Huarancca Quispe
- Ryoshin Cavero Mosquera
- Flavio Andreas Avendanho Cáceres
- Joao Marco Torres Rivera

## Contenido de la sesión

1. [Introducción](#id1)
2. [Objetivos](#id2)
3. [¿Qué es la transformada de Wavelet?](#id3)
4. [Filtrado señal ECG con transformada Wavelet ](#id4)
5. [ Filtrado señal EEG con transformada Wavelet](#id5)
6. [Resultados](#id6)  
   6.1 [EMG](#id7)  
   6.2 [EEG ](#id8)
7. [Discusión](#id9)  
8. [Conclusiones](#id10)  
9. [Bibliografia](#id11)
***

<p style="text-align: justify;">  

## Resumen 

<p style="text-align: justify;"> 
Este informe aborda el estudio y la implementación del filtro wavelet en el procesamiento de señales biomédicas, 
enfocándose específicamente en señales de EMG (electromiografía), ECG (electrocardiografía) y EEG 
(electroencefalografía). Se examinan los principios fundamentales de los filtros wavelet, su aplicación práctica 
y se analizan los resultados obtenidos. Además, se destaca la comparación entre distintos tipos de filtros wavelet 
y su efectividad en la mejora de la calidad de las señales biomédicas.

## Introducción <a name="id1"></a>
<p style="text-align: justify;"> 
   Fue el físico francés Joseph Fourier que se atribuye al algoritmo más importante del último siglo: La transformada de Fourier. Que surgió de la idea de visualizar cualquier señal en el dominio de la frecuencia y no del tiempo. Los dispositivos actuales funcionan usando la Transformada de Fourier en filtros aplicados para eliminación de ruido y para mejorar la señal de salida. Sin embargo, en la medicina surge una cuestión importante. La transformada de fourier tiene sus limitaciones y la principal es que no detecta los cambios bruscos (alta frecuencia en la señal) debido al ventaneo inadecuado en el tiempo y/o en la frecuencia. Es por ello que se utiliza el concepto de la transformada de Wavelet como una solución a nuestro problema. [1,2]

   ### ¿Qué es la transformada de Wavelet?   
   <p style="text-align: justify;"> 
   La transformada Wavelet es una técnica de análisis de señales que proyecta una señal en un conjunto de funciones 
   base que ofrecen localización en el dominio de la frecuencia. A diferencia de la transformada de Fourier, que 
   proporciona una localización tiempo-frecuencia constante, la transformada Wavelet ofrece una alta resolución 
   frecuencial en bajas frecuencias y una alta resolución temporal en altas frecuencias. Esto se logra mediante 
   el uso de una serie de bases ortogonales con diferentes resoluciones para representar o aproximar una señal a 
   través de la expansión y traslación de la función base de la wavelet.
 
## Objetivos <a name="id2"></a>
* Comprender los principios fundamentales del filtro wavelet.
* Aplicar el filtro wavelet a señales de EMG, ECG y EEG.
* Analizar y evaluar las señales biomédicas tras aplicar los filtros wavelet.
* Analizar y evaluar las señales tras aplicar los filtros wavelet.

## ¿Qué es la transformada de Wavelet? <a name="id3"></a>
<p style="text-align: justify;"> 
La transformada Wavelet es una técnica de análisis de señales que proyecta una señal en un conjunto de funciones base que ofrecen localización en el dominio de la frecuencia. A diferencia de la transformada de Fourier, que proporciona una localización tiempo-frecuencia constante, la transformada Wavelet ofrece una alta resolución frecuencial en bajas frecuencias y una alta resolución temporal en altas frecuencias. Esto se logra mediante el uso de una serie de bases ortogonales con diferentes resoluciones para representar o aproximar una señal a través de la expansión y traslación de la función base de la wavelet.


## Filtrado señal ECG con transformada Wavelet <a name="id4"></a>
<p style="text-align: justify;"> 
Se realizó el procesamiento de las señales obtenidas en laboratorios previos usando el Kit-Bitalino, para el caso de la señal ECG se tomaron en cuenta las señales en estado basal , durante la respiración , periodo post respiración y periodo después del ejercicio .
Es uno de los métodos más eficientes para eliminar ruidos en el ECG. Existen muchos tipos de wavelets como Daubechies, Haar, Symlet y BiorSplines[E] . La transformada wavelet es una técnica matemática utilizada en procesamiento de señales para analizar señales que varían en el tiempo o contienen detalles a diferentes escalas. A diferencia de la transformada de Fourier, que representa una señal en el dominio de la frecuencia globalmente, la transformada wavelet proporciona una representación local tanto en el dominio del tiempo como en el de la frecuencia .La metodología de la transformada Wavelet se basa en descomponer la señal, cálculo de coeficientes de diferentes longitudes por cada nivel de descomposición ,estos coeficientes contienen la información esencial de la señal a diferentes escalas de resolución temporal y frecuencia ; finalmente,  un proceso de recomposición de la señal .  

![Figura 1](./Imagenes/Denoising%20techniques.png)

Figura 1. Técnica de eliminación de ruido [3]

La transformada wavelet consta de 3 pasos principales:
Descomponer la señal eligiendo wavelet ‘sym8’ y nivel ‘7’. Esto da como resultado muchos coeficientes de varias longitudes.
Convertir los coeficientes más altos con longitud mínima en ceros, es decir, convertir CA7 y CD7 en ceros. Aplicar umbralización suave al resto de los coeficientes [15] (CD6, CD5, CD4, CD3, CD2 y CD1).
Reconstruir el wavelet utilizando coeficientes modificados y el mismo wavelet ‘sym8’ y nivel ‘7’.

![Figura 2](./Imagenes/signal.png)

Figura 2. Cálculo de umbral suave [3]

![Figura 3](./Imagenes/decomposition.png)

Figura 3. Eliminación de ruido de la señal de ECG mediante la transformada wavelet. [3]

## Filtrado señal EEG con transformada Wavelet <a name="id5"></a>
<div align="justify">
Para el análisis de señales EEG, usaremos el Morlet Wavelet debido a su capacidad de brindar una buena resolución tanto en tiempo como en frecuencia, lo que es crucial en la interpretación de señales no estacionarias como las EEG.  

El Morlet Wavelet es una función que combina una onda sinusoidal modulada por una envolvente gaussiana. Este tipo de wavelet se utiliza comúnmente en el análisis de señales EEG porque ofrece un equilibrio adecuado entre la resolución en el dominio del tiempo y la frecuencia, algo fundamental para estudiar eventos cerebrales que ocurren de forma localizada en el tiempo, como las oscilaciones rítmicas del cerebro. 

El Morlet Wavelet permite analizar cómo cambian las frecuencias en la señal EEG a lo largo del tiempo. Utilizando la Transformada Wavelet Continua (CWT), se convoluciona la señal EEG con versiones escaladas y desplazadas del Morlet Wavelet, lo que genera una representación tiempo-frecuencia de la señal conocida como scalogram. Esto permite observar las dinámicas cerebrales, tales como las transiciones entre distintos estados cerebrales, con alta precisión temporal[4]. 

En su investigación, Olarte evaluó diversas técnicas de denoising utilizando la Transformada Wavelet Discreta y determinó que la wavelet Daubechies de orden 4 ('db4') era la más efectiva para la corrección de ruido en las señales. Este enfoque se aplicó a una descomposición en 4 niveles, lo que permitió una captura adecuada de las características relevantes de la señal.Además, Olarte encontró que la implementación de un umbral suave (soft thresholding) proporcionaba una reducción efectiva del ruido, manteniendo al mismo tiempo la integridad de la información en la señal. Estos resultados resaltan la importancia de elegir adecuadamente los parámetros de la wavelet para optimizar el procesamiento de señales[5].


## Resultados <a name="id6"></a>

<div align="center">

### EMG: <a name="id7"></a> 

#### Bicep en contra reposo:

![Figura 4](./Imagenes/Bicep_reposo.png)

Figura 4. 

#### Bicep en movimiento:

![Figura 5](./Imagenes/Bicep_mov.png)

Figura 5.

#### Bicep en contra fuerza:

![Figura 6](./Imagenes/Bicep_contraF.png)

Figura 6. 


### EEG: <a name="id8"></a>
#### BASAL:

![Figura 7](./Imagenes/Basal_eeg.png)

Figura 7.

#### PARPADEO:

![Figura 8](./Imagenes/Parpadeo_eeg.png)

Figura 8.

#### PREGUNTAS:

![Figura 9](./Imagenes/preguntas_eeg.png)

Figura 9.
<div align="justify">

## Discusión <a name="id9"></a>


Se observan las señales EEG originales y filtradas usando la transformada wavelet Daubechies. La filtración wavelet ha permitido una notable distinción de las características de la señal, eliminando gran parte del ruido de alta frecuencia sin afectar las principales componentes de la señal. Esto se refleja especialmente en los canales donde se percibía mayor ruido o variaciones no deseadas.

- Filtración eficaz: La transformada wavelet aplicada ha sido eficiente para preservar la estructura principal de la señal EEG, lo que facilita su análisis posterior. El análisis de las señales EEG antes y después de aplicar la transformada de Wavelet discreto ilustra efectivamente la utilidad de esta técnica para la mejora de la calidad de las señales biomédicas. Observando las gráficas proporcionadas, se puede apreciar que la aplicación de la transformada Wavelet reduce significativamente el ruido en las señales EEG, permitiendo una visualización más clara de las ondas cerebrales, lo cual es crucial para diagnósticos precisos y para estudios de investigación.
- Reducción de ruido: Antes de la transformación, las señales originales muestran un grado considerable de variabilidad y ruido, lo cual podría interferir con la interpretación clínica de los datos. Después de la transformación, cada canal presenta una línea más suave y menos dispersa, lo que indica una reducción efectiva del ruido. Esto demuestra la capacidad de la transformada Wavelet para preservar las características importantes de la señal mientras minimiza las distracciones causadas por fluctuaciones aleatorias y artefactos..Los coeficientes de alta frecuencia se han eliminado en gran medida, lo que ha permitido resaltar las ondas características del EEG y reducir las fluctuaciones que no pertenecen a la actividad cerebral. 
- Visualización mejorada: Como resultado de la filtración, se logra una señal más clara que puede ser interpretada con mayor facilidad, sin interferencias debidas a componentes no deseados. 

El uso de la wavelet Daubechies es altamente recomendable para el procesamiento de señales como el EEG, donde es crucial identificar patrones a lo largo del tiempo con alta precisión, manteniendo la información relevante en frecuencias bajas. Esto permite identificar eventos específicos de manera más confiable, contribuyendo al análisis neurofisiológico.

## Conclusión <a name="id10"></a>
<div align="justify">
La aplicación de la transformada wavelet, particularmente utilizando la wavelet Daubechies, en el análisis de señales biomédicas como EMG, ECG y EEG ha demostrado ser una técnica poderosa y eficaz para mejorar la calidad de la señal al reducir significativamente el ruido y conservar las características esenciales. Este enfoque ha permitido una visualización más clara y una interpretación más precisa de las señales, facilitando diagnósticos más exactos y avances en la investigación médica. En el caso de las señales EMG y ECG, la transformada wavelet ha proporcionado una herramienta robusta para el filtrado de ruido, preservando detalles importantes que son cruciales para la evaluación de la función muscular y cardíaca. Para las señales EEG, la eliminación efectiva de artefactos y la mejora en la visualización de las ondas cerebrales han permitido una mejor comprensión de los procesos neurológicos, lo que es fundamental para estudios relacionados con trastornos neurológicos y para el monitoreo de la actividad cerebral en entornos clínicos. La transformada wavelet se destaca como una técnica esencial en la ingeniería biomédica, ofreciendo soluciones avanzadas para el procesamiento de señales complejas y variadas en el tiempo.

## Bibliografía<a name="id11"></a>

[1] B. Osgood, “Fourier Transform”, en The Fourier Transform and its Applications. Standford Univ., pp. 65–94.

[2]G. González, “Series de Fourier, Transformadas de Fourier y Aplicaciones”, en Fourier series, Fourier Transforms and Applications, vol. 5, Divulgaciones Matemáticas. Maracaibo, Venezuela: Univ. Del Zulia, 1997, pp. 43–60.

[3]“ECG denoising using wavelet transform and filters | IEEE Conference Publication | IEEE Xplore”. Consultado: el 22 de octubre de 2024. [En línea]. Disponible en: https://ieeexplore-ieee-org.ezproxybib.pucp.edu.pe/document/8300189 

[4] N. Bajaj, "Wavelets for EEG Analysis," IntechOpen, 2020. DOI: 10.5772/intechopen.94398

[5]O. J. Olarte Rodríguez y D. A. Sierra Bueno, “Determinación de los Parámetros Asociados al Filtro Wavelet por Umbralización Aplicado a Filtrado de Interferencias Electrocardiográficas”, Rev. UIS Ing., vol. 6, núm. 2, pp. 33–44, 2007.
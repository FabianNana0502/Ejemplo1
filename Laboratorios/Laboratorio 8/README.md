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
5. [Resultados](#id5)  
   5.1 [EEG alumno](#id6)  
   5.2 [EEG profesor](#id7)
   
6 [Discucion](#id8)  
7 [Resultado](#id9)  
8 [Bibliografia](#id10)
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


## Resultados <a name="id5"></a>
***


<div align="justify">

## Discusión <a name="id8"></a>
***


## Conclusión <a name="id9"></a>
El estudio del procesamiento de señales EEG utilizando la transformada wavelet, específicamente con la wavelet Daubechies, ha demostrado ser muy eficaz en la reducción de ruido y en la preservación de características esenciales de la señal. La capacidad de esta técnica para eliminar el ruido sin perder detalles cruciales permite una interpretación más clara y precisa de la actividad cerebral, esencial tanto para diagnósticos clínicos como para investigaciones neurofisiológicas. La claridad mejorada en las señales facilita un análisis detallado y una visualización efectiva de las dinámicas cerebrales, contribuyendo significativamente al entendimiento de trastornos neurológicos y al desarrollo de intervenciones basadas en evidencia. La recomendación del uso de wavelets Daubechies para el análisis EEG resalta su equilibrio óptimo entre resolución temporal y frecuencial, haciendo de esta técnica una elección ideal para el análisis fiable y detallado de eventos neurológicos complejos. En conjunto, la aplicación de la transformada wavelet en señales EEG representa un avance notable en el campo biomédico, proporcionando herramientas robustas para mejorar el diagnóstico y la investigación en neurociencia.


## Bibliografía<a name="id10"></a>

[1] B. Osgood, “Fourier Transform”, en The Fourier Transform and its Applications. Standford Univ., pp. 65–94.

[2]G. González, “Series de Fourier, Transformadas de Fourier y Aplicaciones”, en Fourier series, Fourier Transforms and Applications, vol. 5, Divulgaciones Matemáticas. Maracaibo, Venezuela: Univ. Del Zulia, 1997, pp. 43–60.


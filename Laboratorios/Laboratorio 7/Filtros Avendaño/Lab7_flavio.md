# LABORATORIO 7: – Diseño y aplicaciones de Filtros mediante PyFDA
***
## Autor

### Flavio Avendaño Cáceres

## Contenido del informe
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
<div align="justify">

En el proceso de obtencion de bioseñales, tales como los EMGs, ECGs y EEGs, las calidad de las señales puede verse afectadas por factores como la calidad del elctrodo, campos electromagenticos o ruido (biologico o eléctrico) del mismo ambiente de evaluaciones.

Por lo cual es imperativo el uso de los filtros, los cuales son sistemas (analogicos o digitales) que tiene por funcion recibir la señal y eliminar componentes no deseados conservarndo solo elementos característicos relevantes de la señal en cuestión. Para el diseño de estos filtros se empleara el software pyFDA(Python Digital Filtering and Analysis) aplicandolo a señales EMG y ECG de laboratorios previos y evaluar el rendimiento de disntintos tipos de filtros segun cuanto conserven y refinen las señales de entarda.

   ### Conceptos Previos
  
   Los filtros pueden ser divididos en:[1]

   * Filtro pasa-bajas: permite el paso de todas las frecuencias menores a la frecuencia de corte, atenuando aquellas que son mayores a esta última.
   * Filtro pasa-altas: atenúa todas las frecuencias bajas y permite el paso de aquellas por encima de la frecuencia de corte.
   * Filtro pasa-bandas: deja pasar las frecuencias comprendidas entre la frecuencia de corte inferior y la frecuencia de corte superior, atenuando las demás.
   * Filtro rechaza-bandas: atenúa las frecuencias comprendidas entre la frecuencia de corte inferior y la frecuencia de corte superior, dejando pasar las demás.

<div align="center">

<img src="./Infografia/IdealFilters.png" width="600" height="300">

Fig 1. Representación gráfica de los tipos de filtros [1]

<div align="justify">

Estos filtros se pueden clasificar, de acuerdo a la aproximación matemática empleada, en:

   * Butterworth: tiene objetivo una respuesta de ganancia plana en la banda de paso. Esto se consigue mediante una región de transición de caída lenta y una respuesta de fase no lineal alrededor de la frecuencia de corte
   * Chebyshev: tiene como objetivo maximizar la pendiente de la característica de ganancia en la región de transición. Presenta un cierto rizado en la banda de paso, que se incrementa al aumentar el orden de filtro.
   * Bessel: tiene como objetivo lograr una respuesta de fase lineal en un margen de frecuencias amplio en torno a la frecuencia de corte. La ganancia en la banda de paso no es tan plana como en un filtro Butterworth ni la pendiente en la banda de transición tan acentuada como en un filtro Chebyshev
   * Elíptica: se caracteriza por tener ondulaciones constantes tanto en la banda de paso como en la banda de corte.

<div align="center">

<img src="./Infografia/Aproximaciones.png" width="600" height="300">

Fig 1. Representación gráfica segun la Aproximacion Matematica [1]

## Objetivos <a name="id2"></a>
* Analizar y seleccionar los filtros segun la señal a procesar.
* Diseñar un total de 6 filtros y aplicarlos a las señales EMG y EKG mediante pyFDA.
* Comparar los resultados obtenidos y diferenciar ventajas y desventajas de un 
  filtro sobre otro.

## Materiales y equipos <a name="id3"></a>

<div align="center">

| Material     |Descripción      |Cantidad   |
|-----------   |:------------:   |:---------:| 
| Laptop       |Laptop           |1          |
| Programa de diseño   | pyFDA   |1          |

<img src="./Infografia/pyFDA.png" width="600" height="300">

Fig 3. Software pyFDA

<div align="justify">

## Metodología <a name="id4"></a>



### Proceso de Filtrado


## Resultados <a name="id5"></a>
***
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

   


## Conclusión <a name="id9"></a>



## Bibliografía<a name="id10"></a>

[1] Federico Miyara.(2004) Electronica III - Filtros Activos, Segunda Edicion. Universidad Nacional de Rosario
   https://www.fceia.unr.edu.ar/enica3/filtros-t.pdf

[2] 

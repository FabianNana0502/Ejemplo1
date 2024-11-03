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
   4.1 [Extracción de características](#id5)  
5. [Discusión](#id6)  
6. [Conclusiones](#id7)  
7. [Bibliografia](#id8)
***


## Introducción <a name="id1"></a>
<div align="justify">



## Objetivos <a name="id2"></a>
* Elección del mejor filtro Wavelet para EMG en base a búsqueda bibliográfica 
* Segmentación de la señal.
* Extracción de parámetros estáticos y temporales de la señal.
* Realizar el análisis de las características y cómo varían estos  valores.
* Verificar el comportamiento de la señal EMG.

## Metodología <a name="id3"></a>
### Extracción de características
<p style="text-align: justify;"> 
Esta información se obtiene de la aplicación  de las llamadas  técnicas  de  extracción  de  características, dentro de las cuales se destacan como pioneras las basadas en análisis temporal por su sencillez y facilidad de evaluación, debido a que no requieren ningún tipo de transformación de la señal .
También están las basadas en análisis espectral, para las cuales se requiere de la transformación de la señal, como la transformada de Fourier de tiempo corto (STFT­ short time Fourier transform)  con la cual se obtiene información  de la señal en el dominio de ­frecuencia , aunque esta técnica asume la condición  de estacionariedad  en la señal, lo cual no se cumple para las señales EMG.Una solución a este inconveniente se refleja en los últimos trabajos de investigación en el área de procesamiento de señales con la técnica de análisis espectral basada en la “teoría  de  wavelets”, mediante las  transformadas  wavelets: CWT (Continuous Wavelet Transform) y DWT (Discrete Wavelet Transform) . Con esta técnica se consigue una representación de la señal en los dominios de tiempo­ y frecuencia mucho  más compacta que la conseguida por transformada de Fourier STFT, puesto que permite disponer de información de la señal en sus dominios original y transformado de manera simultánea , en laboratorios previos se realizó el filtrado de la señal EMG  mediante Transformada Wavelet Discreta usando la wavelet Daubechies de orden 4 ('db4') ,la cual es la más efectiva para la corrección de ruido en las señales[5] .

La extracción de características como la Raíz Cuadrática Media (RMS), Valor Absoluto Medio (MAV), Longitud de la Onda (WL) y Cruce por Cero (ZC) permite el desarrollo de sistemas de control precisos en prótesis basados en señales EMG. El RMS y MAV son indicadores clave de la intensidad y energía de la señal, útiles para diferenciar estados de reposo de contracciones de baja y alta intensidad. La WL aporta información sobre la complejidad de la contracción, permitiendo identificar patrones asociados a movimientos suaves o de fuerza. El ZC, al detectar cambios de fase, facilita la identificación de inicios y finales de contracción, cruciales en la sincronización de los movimientos de la prótesis con la intención del usuario.
Estas características, al ser integradas en algoritmos de control, permiten que la prótesis responda en tiempo real, adaptando su nivel de respuesta a las variaciones de la señal EMG. Por ejemplo, un sistema puede aumentar la potencia del dispositivo en función de la amplitud de la señal (medida por RMS o MAV) durante contracciones de fuerza, o activar movimientos de precisión cuando se detectan movimientos voluntarios de baja intensidad.

### Análisis de los ploteos antes y después de aplicar la Transformada Wavelet:
<p style="text-align: justify;"> 


## Resultados: 

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

## Discusión <a name="id6"></a>



## Conclusión <a name="id7"></a>
<div align="justify">

### Comparación Cuantitativa entre Grupos:


### Diferencias en Variabilidad y Cruces por Cero:


### Hallazgos de Interés:



## Bibliografía<a name="id8"></a>







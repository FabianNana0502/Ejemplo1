# LABORATORIO 13: Generacion Impulso Edge Impulse
## Alumno
- Flavio Avendaño Cáceres
---
## Contenido de la sesión

[Informe Laboratorio](#id1)
    - [Creacion de impulso](#id2)
    - [Caracteristicas espectrales](#id3)
    - [Clasificacion](#id4)
    - [Retrain](#id5)
    - [Conclucion](#id6)

---
<div align="justify">

## Informe Laboratorio <a name="id1"></a>

https://studio.edgeimpulse.com/studio/558200/impulse/1/create-impulse

### Creacion de impulso <a name="id2"></a>

En base a la configuracion previa que se hizo al subir los datos al Edge Impulse, se configuró en consecuencia el impulso, en modo "Time Series Data", a 1000Hz, tal y como se subir los datos, agregando un analysis espectral por recomendacion del programa y un clasificador segun las caracteristicas espectral que se obtengan.

<div align="center">

![fisrt](./Images/1.png)

Fig. 1 Configuracion inicial del impulso

<div align="justify">

### Caracteristicas espectrales <a name="id3"></a>

Para un optimo resultado, se emplea un FFT length de 256 y activando el overlap y log del espectro a obtener

<div align="center">

![spec](./Images/2.png)

Fig. 2 Configuracion de estractor de caracteristicas

![res1](./Images/feat.png)

Fig. 3 Resultado de extraccion de caracteristicas y su peso respectivo

<div align="justify">

### Clasificacion <a name="id4"></a>

Para la clasificacion se empleo un alto numero de ciclos de entrenamiento y un ratio de aprendizaje de 0.001, procesiendo a tratar un total de 133 caracteristicas.

<div align="center">

![config](./Images/3.png)

Fig. 4 Configuracion 

![mat](./Images/mat1.png)

Fig. 5 Matriz de confusion obtenida

![ex](./Images/explorer.png)

Fig. 6 Distribucion de resultados

<div align="justify">

### ReTrain <a name="id5"></a>

Si bien se intento mejorar las estadisticas con la funcion de Re-entrenamiento, no hubo mejorias, mas bien una disminucion de la presicion, haciendo inviable este metodo.

<div align="center">

![retrain](./Images/end.png)

Fig. 7 Resultado de ReTrain

<div align="justify">

### Conclucion <a name="id6"></a>

El valor de accuracy obtenido de 67% resulta ser un valor demasiado bajo, el cual considerando además, el Loss obtenido, presenta como NO optimo el modelo diseñado, teniendo en cuenta el proceso de diseño, dentro de las posibles causas de este bajo valor estan:

* Ventaneo demasiado pequeño que impide obtener suficientes caracteristicas

* Analysis espectral sin suficiente informacion debido al window de 2000 ms seleccionado en CSV wizzard

* Falta de procesos de interpolacion durante la etapa de preprocesamiento de la data adquirida con el BITalino

Teniendo en cuenta estas consdieraciones, se espera que tras el agregar estos pasos extras en el pre-procesamiento de la data, y mayor cuidado al seleccionar las ventanas de informacion y la confirguacion del extractor de caracteristicas, obtener como minimo un ,modelo con prescion superior a 95%.

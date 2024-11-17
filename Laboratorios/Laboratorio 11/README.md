# LABORATORIO 11: Edge Impulse
## Integrantes
- Fabian Alcides Ñaña Alfaro
- Christian Huarancca Quispe
- Ryoshin Cavero Mosquera
- Flavio Andreas Avendaño Cáceres
- Joao Marco Torres Rivera

---

## Contenido de la sesión

1. [Entregable por miembro del grupo](#id1)
    - [Fabian Ñaña](#id2)
    - [Christian Huarancca](#id3)
    - [Ryoshin Cavero](#id4)
    - [Flavio Avendaño](#id5)
    - [Joao Torres](#id6)

---

## 1. Entregable por miembro del grupo <a name="id1"></a>

### 1.1 Fabian Alcides Ñaña Alfaro <a name="id2"></a>
https://studio.edgeimpulse.com/studio/560365/acquisition/training?page=1 

Para realizar la clasificación de señales de ECG en **Edge Impulse**, se utilizaron archivos CSV preprocesados. A continuación, se detallan los pasos seguidos para configurar los datos.

### Configuración del CSV Wizard en Edge Impulse

#### Paso 1: Subir archivos CSV
En esta etapa, se selecciona el archivo CSV para su carga en el **CSV Wizard**.

<img src="Imagenes/Imagenes_Fabian/csvwizard1.png" alt="Fig.1: Subir archivo CSV">

---

#### Paso 2: Selección de archivos y carpeta
Se eligió la opción para cargar múltiples archivos dentro de una carpeta para una mayor eficiencia. Aquí se muestran los archivos cargados con éxito.

<img src="Imagenes/Imagenes_Fabian/subidos.png" alt="Fig.2: Archivos subidos">

---

#### Paso 3: Vista previa del conjunto de datos cargado
En esta sección se visualizan los datos de entrenamiento y prueba ya cargados.

**Datos de Prueba:**
<img src="Imagenes/Imagenes_Fabian/test.png" alt="Fig.3: Conjunto de datos de prueba">

**Datos de Entrenamiento:**
<img src="Imagenes/Imagenes_Fabian/train.png" alt="Fig.4: Conjunto de datos de entrenamiento">

---

#### Paso 4: Proceso de carga de datos
El sistema permite cargar archivos **JSON**, **CSV**, y otros formatos. Para este proyecto, se utilizaron archivos CSV configurados con delimitadores adecuados.

<img src="Imagenes/Imagenes_Fabian/upload.png" alt="Fig.5: Proceso de carga de datos">

---

### Descripción del proceso del CSV Wizard

#### Paso 2: Procesar el archivo CSV
El delimitador seleccionado fue el punto y coma (;), lo cual permitió que los datos fueran correctamente separados en columnas.

<img src="Imagenes/Imagenes_Fabian/wizard2.png" alt="Fig.6: Configuración del delimitador">

---

#### Paso 3: Información sobre los datos
Se indicó que los datos cargados corresponden a **series de tiempo**, con una frecuencia de **1000 Hz**.

<img src="Imagenes/Imagenes_Fabian/wizard3.png" alt="Fig.7: Configuración de series de tiempo">
<img src="Imagenes/Imagenes_Fabian/wizard3.1.png" alt="Fig.8: Confirmación de la estructura">

---

#### Paso 4: Selección de valores
En esta etapa, se determinó qué columnas contienen los datos relevantes.

<img src="Imagenes/Imagenes_Fabian/wizard4.png" alt="Fig.9: Selección de valores">

---

#### Paso 5: División de muestras
Se configuraron muestras de **300 ms** para la creación de segmentos de datos, lo que permite una mejor clasificación durante el entrenamiento.

<img src="Imagenes/Imagenes_Fabian/wizard5.png" alt="Fig.10: División en muestras">

---

### 1.2. Christian Huarancca Quispe <a name="id3"></a>
**Descripción pendiente por completar**

---

### 1.3. Ryoshin Cavero Mosquera <a name="id4"></a>

Puede encontrar el enlace a **Edge Impulse** [aquí](https://studio.edgeimpulse.com/studio/552481/acquisition/training?page=1).

He realizado la separación de las señales de acuerdo a la actividad realizada en el momento, como se aprecia en la Figura a continuación:

<img src="./Imagenes/Ryoshin/SEPARACION.png" alt="Fig.11: Separación de señales">

A continuación, se muestra la tabla de los archivos utilizados para cada clase de ECG separado:

<table>
    <tr>
        <th>BASAL</th>
        <th>RESPIRACIÓN</th>
        <th>POST-RESPIRACIÓN</th>
        <th>EJERCICIO</th>
    </tr>
    <tr>
        <td><img src="./Imagenes/Ryoshin/BASAL.png" alt="Basal"></td>
        <td><img src="./Imagenes/Ryoshin/RESPIRACION.png" alt="Respiración"></td>
        <td><img src="./Imagenes/Ryoshin/POST-RESPIRACION.png" alt="Post-Respiración"></td>
        <td><img src="./Imagenes/Ryoshin/EJERCICIO.png" alt="Ejercicio"></td>
    </tr>
</table>

---

### 1.4. Flavio Andreas Avendaño Cáceres <a name="id5"></a>
**Descripción pendiente por completar**

---

### 1.5. Joao Marco Torres Rivera <a name="id6"></a>
**Descripción pendiente por completar**

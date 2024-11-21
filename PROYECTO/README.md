# Avance 2 de proyecto

## Integrantes
- Fabian Alcides Ñaña Alfaro
- Christian Huarancca Quispe
- Ryoshin Cavero Mosquera
- Flavio Andreas Avendaño Cáceres
- Joao Marco Torres Rivera

---

## Estado de Arte

Ryoshi

---

## Problematica y propuesta

Joao

---

## Metodologia

HQ

---

## Prototipo

<div align="justify">

### Procesamiento del dataset

En primer lugar, debido a que toda la informacion cruda de los 13 musculos de cada uno de los 300 sujetos esta en formato R, es imprescindible, en Rstudio (para agilizar el trabajo debido al formato original) filtrar toda la informacion EMG en el rango definido en laboratorios (20-450 Hz) y convertir las señales dependientes de tiempo a archivos csv, formando un conjunto de archivos csv, los cuales son faciles y practicos de leer para el codigo de extraccion de caracteristicas, que se elaborará en Python.

<div align="center">

![Ambiente R](./avance%202/R.png)

Fig #. Ambiente Rstudio con el dataset Raw-Data

<div align="justify">

No se evaluaran todos y cada uno de los 13 musculos del miembro inferior (aunque el dataset si los posee) debido a la robustez, por lo cual a futuro se identificara los musculos mas relevantes para analizar los modulos musculares, de tal forma, para el filtrado y obtencion de los EMGs, se empleó el siguiente codigo en R el cual posee opciones de previsualizacion segun sujeto, musculo y ventana de tiempo de 10s o ploteo de señal completa.

Codigo R:

```python

library(shiny)
library(signal)

# Interfaz 
ui <- fluidPage(
  titlePanel("Pass-band Filtered EMG"),
  
  sidebarLayout(
    sidebarPanel(
      selectInput("file", "Select patient ID from DATA:", 
                  choices = names(RAW_DATA)),
      uiOutput("muscle_select"),
      sliderInput("time_window", "Move trough the signal (ms):",
                  min = 0, max = 50000, value = 0, step = 100, ticks = FALSE),
      actionButton("plot_button", "Plot current window"),
      actionButton("full_plot_button", "Plot full signal"),
    ),
    
    mainPanel(
      plotOutput("emg_plot")
    )
  )
)

# Servidor
server <- function(input, output, session) {
  
  # Variables reactivas 
  signal_info <- reactiveValues(max_time = 50000, full_plot = FALSE)
  
  # Actualizar selección de músculos y duración de la señal
  observeEvent(input$file, {
    data <- RAW_DATA[[input$file]][["emg"]]
    
    if (is.data.frame(data)) {
      muscles <- colnames(data)
      max_time <- nrow(data) / 2
    } else {
      data <- as.data.frame(data)
      muscles <- paste0("Músculo_", 1:ncol(data))
      max_time <- length(data) / 2
    }
    
    # selección de músculos
    output$muscle_select <- renderUI({
      selectInput("muscle", "Select muscle:", choices = muscles)
    })
    
    # límite del control deslizante
    signal_info$max_time <- max_time
    updateSliderInput(session, "time_window", max = max_time - 10000, value = 0)
  })
  
  # Graficar 
  output$emg_plot <- renderPlot({
    req(input$file, input$muscle)
    
    # Cargar datos
    data <- RAW_DATA[[input$file]][["emg"]]
    if (!is.data.frame(data)) {
      data <- as.data.frame(data)
      colnames(data) <- colnames(data, do.NULL = FALSE, prefix = "Músculo_")
    }
    
    # Seleccionar el músculo
    muscle_data <- data[[input$muscle]]
    
    # Parámetros de filtrado
    fs <- 2000                         
    nyquist <- fs / 2
    band <- butter(4, c(20 / nyquist, 500 / nyquist), type = "pass")
    
    # Filtrar señal
    filtered_data <- filtfilt(band, muscle_data)
    
    if (signal_info$full_plot) {
      # Graficar toda la señal
      time <- seq(0, length(filtered_data) - 1) * (1000 / fs)
      plot(time, filtered_data, type = "l", 
           main = paste("Filtered EMG - muscle:", input$muscle),
           xlab = "Time (ms)", ylab = "Amplitude (mV)",
           col = "blue", lwd = 1)
    } else {
      # Ventana fija de 10,000 ms
      start_idx <- round(input$time_window * fs / 1000)
      end_idx <- min(start_idx + (10000 * fs / 1000), length(filtered_data))
      filtered_data_window <- filtered_data[start_idx:end_idx]
      time_window <- seq(input$time_window, input$time_window + 10000, length.out = length(filtered_data_window))
      
      plot(time_window, filtered_data_window, type = "l", 
           main = paste("Filtered EMG - muscle:", input$muscle),
           xlab = "Time (ms)", ylab = "Amplitude (mV)",
           col = "red", lwd = 2)
    }
  })
  
  # Botón para graficar toda la señal
  observeEvent(input$full_plot_button, {
    signal_info$full_plot <- TRUE
    output$emg_plot <- renderPlot({
      req(input$file, input$muscle)
      data <- RAW_DATA[[input$file]][["emg"]]
      if (!is.data.frame(data)) {
        data <- as.data.frame(data)
        colnames(data) <- colnames(data, do.NULL = FALSE, prefix = "Músculo_")
      }
      muscle_data <- data[[input$muscle]]
      fs <- 2000                         
      nyquist <- fs / 2
      band <- butter(4, c(20 / nyquist, 500 / nyquist), type = "pass")
      filtered_data <- filtfilt(band, muscle_data)
      time <- seq(0, length(filtered_data) - 1) * (1000 / fs)
      plot(time, filtered_data, type = "l", 
           main = paste("Filtered EMG - muscle:", input$muscle),
           xlab = "Time (ms)", ylab = "Amplitude (mV)",
           col = "blue", lwd = 1)
    })
  })
  
  # Botón para graficar ventana
  observeEvent(input$plot_button, {
    signal_info$full_plot <- FALSE
    output$emg_plot <- renderPlot({
      req(input$file, input$muscle)
      data <- RAW_DATA[[input$file]][["emg"]]
      if (!is.data.frame(data)) {
        data <- as.data.frame(data)
        colnames(data) <- colnames(data, do.NULL = FALSE, prefix = "Músculo_")
      }
      muscle_data <- data[[input$muscle]]
      fs <- 2000                         
      nyquist <- fs / 2
      band <- butter(4, c(20 / nyquist, 500 / nyquist), type = "pass")
      filtered_data <- filtfilt(band, muscle_data)
      start_idx <- round(input$time_window * fs / 1000)
      end_idx <- min(start_idx + (10000 * fs / 1000), length(filtered_data))
      filtered_data_window <- filtered_data[start_idx:end_idx]
      time_window <- seq(input$time_window, input$time_window + 10000, length.out = length(filtered_data_window))
      plot(time_window, filtered_data_window, type = "l", 
           main = paste("Filtered EMG - muscle:", input$muscle),
           xlab = "Time (ms)", ylab = "Amplitude (mV)",
           col = "red", lwd = 2)
    })
  })
}

shinyApp(ui = ui, server = server)

```

<div align="center">

![Ambiente R](./avance%202/window.png)

Fig #. Ploteo de ventana movil

![Ambiente R](./avance%202/full.png)

Fig #. Ploteo de señal EMG completa

<div align="justify">

Una vez previsualizado, se puede elegir entre convertir a csv. la señal entera o la ventan segun el tamaño que se busque para el modelo IA.


FALTA PARTE DE ÑAÑA

---

## Bibliografia


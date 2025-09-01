# 📘 Proyecto de Detección de Placas Vehiculares con CNN

Este notebook implementa un modelo de **Red Neuronal Convolucional (CNN)** para la detección de **placas vehiculares colombianas** a partir de un dataset en formato COCO.  

El proyecto contempla las siguientes etapas:

1. **Preprocesamiento**  
   - Carga del dataset en formato COCO (train, validation, test).  
   - Normalización y redimensionamiento de imágenes.  
   - Conversión de etiquetas de bounding boxes a coordenadas normalizadas.  
   - Separación en conjuntos de entrenamiento, validación y prueba.  

2. **Construcción del Modelo CNN**  
   - Arquitectura con múltiples bloques convolucionales.  
   - Dos salidas:  
     - **Clasificación** (`placa_carro` vs `placa_moto`).  
     - **Regresión de bounding box** (`x, y, w, h`).  
   - Uso de capas de regularización (`Dropout`, `BatchNormalization`).  

3. **Entrenamiento y Evaluación**  
   - Optimización con `Adam`.  
   - Pérdida compuesta: `categorical_crossentropy` (clasificación) + `Huber` (bounding box).  
   - Callbacks de `EarlyStopping` y `ModelCheckpoint`.  

4. **Evaluación de Métricas**  
   - Cálculo de:  
     - **Accuracy** (clasificación).  
     - **IoU (Intersection over Union)** para bounding boxes.  
     - **Pérdida total**, **pérdida de clasificación** y **pérdida de bounding box**.  

5. **Visualización**  
   - Ejemplos de imágenes con data augmentation.  
   - Visualización de predicciones con cajas detectadas.  

---

## ⚙️ Requisitos

Instalar las dependencias necesarias:

```bash
pip install tensorflow matplotlib numpy opencv-python tqdm
````

---

## 🚀 Ejecución

Ejecutar el notebook paso a paso:

```bash
jupyter notebook procesamiento.ipynb
```

---

## 📊 Muestra de Métricas

Ejemplo de resultados obtenidos en **test**, **train** y **validación**:

### Conjunto de Prueba (Test)

```
Pérdida total:       0.0370
Pérdida clasif.:     0.0011
Pérdida bbox:        0.0359
Precisión clasif.:   1.0000
IoU medio bbox:      0.3367
```

### Conjunto de Entrenamiento (Train)

```
Pérdida total:       1.3628
Pérdida clasif.:     1.3037
Pérdida bbox:        0.0333
Precisión clasif.:   0.8208
IoU medio bbox:      0.3474
```

### Conjunto de Validación (Val)

```
Pérdida total:       0.0374
Pérdida clasif.:     0.0009
Pérdida bbox:        0.0503
Precisión clasif.:   1.0000
IoU medio bbox:      0.3112
```

---

## 📌 Observaciones

* La **clasificación** obtiene resultados excelentes (accuracy ≈ 1.0 en valid/test).
* El desempeño en **regresión de bounding boxes** aún puede mejorarse (IoU ≈ 0.31–0.34).
* Posibles mejoras:

  * Ajustar pesos de pérdidas (`loss_weights`).
  * Cambiar la función de pérdida de bounding box (ej. IoU loss).
  * Usar **Transfer Learning** (ej. MobileNetV2 o ResNet50).

---

## ✨ Autor

Desarrollado por **Andres Felipe Patiño Mogollon** como parte de la prueba técnica de **Incolmotos Yamaha**.

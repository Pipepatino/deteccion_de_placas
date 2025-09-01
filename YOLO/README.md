# Proyecto de Detección de Placas Vehiculares con YOLOv8

Este notebook implementa un modelo de **YOLOv8** para la detección de **placas vehiculares colombianas**.  
Se parte de un dataset anotado en formato YOLO/COCO y se entrena un modelo especializado capaz de localizar placas en imágenes.

---

## 📂 Flujo del proyecto

1. **Carga del dataset**  
   - Se utiliza un dataset en formato YOLO/COCO exportado desde Roboflow.  
   - El dataset contiene imágenes de vehículos con anotaciones de placas.

2. **Entrenamiento de YOLOv8**  
   - Se usa el framework `ultralytics` (YOLOv8).  
   - Parámetros configurados:  
     - `epochs`: número de épocas de entrenamiento.  
     - `imgsz`: tamaño de imágenes de entrada.  
     - `batch`: tamaño de lote.  
   - Se entrena el modelo y se guardan los pesos (`best.pt`) en la carpeta de runs.

3. **Evaluación del modelo**  
   - Métricas calculadas automáticamente por YOLOv8:  
     - **mAP50**: Mean Average Precision en IoU=0.5.  
     - **mAP50-95**: Precisión promedio en múltiples umbrales IoU (0.5 a 0.95).  
     - **Precision** y **Recall**.  
   - Se generan gráficos de **pérdida de entrenamiento** y curvas de métricas.

4. **Predicciones y pruebas**  
   - Se cargan imágenes de prueba individuales.  
   - El modelo detecta placas y dibuja bounding boxes con confianza asociada.  
   - Los resultados se muestran gráficamente y pueden exportarse.

---

## ⚙️ Requisitos

Instalar dependencias necesarias:

```bash
pip install ultralytics opencv-python matplotlib
````

---

## 🚀 Ejecución

Ejecutar el notebook paso a paso:

```bash
jupyter notebook yolo_model.ipynb
```

---

## 📊 Muestra de métricas

Ejemplo de métricas obtenidas durante el entrenamiento:

```
Epochs:        50
Batch size:    16
Image size:    640x640

Resultados:
- Precisión:   0.92
- Recall:      0.88
- mAP@0.5:     0.95
- mAP@0.5:0.95 0.87
```

*(Los valores son de referencia; pueden variar según dataset y parámetros de entrenamiento).*

---

## 📌 Observaciones

* El modelo alcanza un **alto desempeño en detección de placas** (mAP > 0.9).
* Es posible ajustar hiperparámetros para mejorar recall en casos difíciles (ej. iluminación, ángulos extremos).
* El modelo entrenado se encuentra en:

  ```
  /runs/weights/best.pt
  ```

---

## ✨ Autor

Desarrollado por **Andres Felipe Patiño Mogollon** como parte de la prueba técnica de **Incolmotos Yamaha**.

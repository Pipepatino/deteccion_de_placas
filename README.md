
#  Sistema de Detección y Reconocimiento de Placas Vehiculares

Este proyecto integra técnicas de **visión por computadora** y **aprendizaje profundo** para construir un sistema completo de **detección, reconocimiento y control de acceso de vehículos mediante placas**.  

Se desarrollaron e integraron tres componentes principales:

1. **Red Neuronal Convolucional (CNN propia)** para clasificación de tipo de placa y regresión de bounding boxes.  
2. **YOLOv8** como detector avanzado de placas, entrenado en dataset específico.  
3. **OCR + Lógica de Negocio** para extraer caracteres de las placas y determinar si un vehículo es **registrado o visitante**, así como si está **ingresando o saliendo**.  

---

##  Estructura del Proyecto

```

.
├── Caracteres\_placa/         # OCR + lógica de negocio
│   ├── app.py                # Detección con YOLO + OCR con PaddleOCR
│   ├── logic.py              # Ingreso/Salida + Visitante/Registrado
│   └── README.md
│
├── CNN/                      # Entrenamiento CNN multitarea
│   ├── dataset\_coco/         # Dataset en formato COCO
│   ├── output/               # Modelos guardados
│   ├── procesamiento.ipynb   # Preprocesamiento, entrenamiento y métricas
│   └── README.md
│
├── YOLO/                     # Entrenamiento YOLOv8
│   ├── dataset\_yolo/         # Dataset en formato YOLO
│   ├── runs/                 # Resultados de entrenamiento
│   ├── yolo\_model.ipynb      # Entrenamiento y validación YOLO
│   ├── yolov8n.pt            # Pesos preentrenados
│   └── README.md
│
└── README.md                 # Documentación general (este archivo)

````

---


## Arquitctura del proyecto


| Etapa              | Herramienta     | Resultado                         |
| ------------------ | --------------- | --------------------------------- |
| Entrada            | Imagen vehículo | Imagen original                   |
| Detección de placa | YOLOv8 / CNN    | Bounding box con placa localizada |
| Reconocimiento     | PaddleOCR       | Texto con caracteres de la placa  |
| Lógica             | Logic.py        | Estado: Ingreso / Salida          |
| Clasificación      | Logic.py + BD   | Tipo: Registrado / Visitante      |


---

## ⚙️ Instalación

Clonar el repositorio y crear un entorno virtual:

```bash
git clone <repo_url>
cd proyecto-placas
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## 🚀 Uso

### 1. Entrenar CNN

```bash
jupyter notebook CNN/procesamiento.ipynb
```

* Entrena una CNN multitarea con salida de clasificación y bounding box.
* Guarda el modelo en `CNN/output/`.

### 2. Entrenar YOLOv8

```bash
jupyter notebook YOLO/yolo_model.ipynb
```

* Entrena YOLO con dataset anotado en formato YOLO.
* Resultados y métricas en `YOLO/runs/`.

### 3. OCR + Lógica

```bash
python Caracteres_placa/app.py
```

* Detecta placas en imágenes.
* Extrae caracteres con PaddleOCR.
* Determina si el vehículo es registrado o visitante, e ingreso o salida.

---

## 📊 Métricas de Referencia

### CNN

```
== TEST ==
Pérdida total:       0.0370
Pérdida clasif.:     0.0011
Pérdida bbox:        0.0359
Precisión clasif.:   1.0000
IoU medio bbox:      0.3367
```

### YOLOv8

```
Épocas:       50
Batch size:   16
Image size:   640x640

Resultados:
- Precisión:   0.92
- Recall:      0.88
- mAP@0.5:     0.95
- mAP@0.5:0.95 0.87
```

---

##  Observaciones

* La **CNN** obtiene muy buena clasificación, pero el IoU de bounding boxes aún es limitado.
* **YOLOv8** logra resultados más robustos, adecuado para uso en producción y tiempo real.
* La integración de **OCR + lógica** permite simular un sistema de control de acceso de vehículos.

---

##  Mejoras Futuras

* Reemplazar la base simulada por una **base de datos real** (ej. PostgreSQL o SQLite).
* Implementar un **sistema en tiempo real con cámara IP**.
* Guardar logs de eventos en **CSV o base de datos** con fecha y hora.
* Usar técnicas de **transfer learning** (ej. MobileNet, ResNet) para mejorar el IoU en CNN.
* Integrar una **interfaz web** para consulta de accesos.

---

##  Autor

**Andres Felipe Patiño Mogollon**
Prueba técnica — *Incolmotos Yamaha*


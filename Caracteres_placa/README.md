
# Sistema de Detección y Registro de Placas Vehiculares

Este proyecto implementa un sistema de **detección de placas vehiculares** usando un modelo **YOLOv8** y un módulo de **reconocimiento óptico de caracteres (OCR)** con **PaddleOCR**.  
Además, incluye una **lógica de negocio** para identificar si el vehículo corresponde a un **visitante o registrado** y determinar si está **ingresando o saliendo** de las instalaciones.

---

## 📂 Estructura del proyecto

```

Caracteres\_placa/
│
├── app.py        # Detección de placas, OCR y visualización
├── logic.py      # Lógica de ingreso/salida y visitante/registrado
└── README.md     # Documentación del proyecto

````

---

## ⚙️ Requisitos

Instalar las dependencias necesarias:

```bash
pip install ultralytics paddleocr opencv-python imutils
````

---

## ▶️ Uso

### 1. `app.py`

Este archivo:

* Carga una imagen de prueba.
* Detecta placas vehiculares usando YOLOv8.
* Extrae la placa y aplica OCR con PaddleOCR.
* Filtra caracteres válidos (A-Z, 0-9).
* Muestra la imagen con la placa detectada y los caracteres reconocidos.
* Llama a la función `process_plate()` para determinar el estado del vehículo.

Ejecutar:

```bash
python app.py
```

La salida mostrará en consola, por ejemplo:

```
Placa: ABC123 | Registrado | Ingreso
Placa: QWE987 | Visitante | Ingreso
Placa: ABC123 | Registrado | Salida
```

Y en pantalla se abrirá una ventana con la imagen y la información superpuesta.

---

### 2. `logic.py`

Este módulo contiene la lógica de negocio:

* **Base simulada de placas registradas**:

  ```python
  registered_plates = {"ITR192", "XYZ789", "MNO456"}
  ```
* **Estado dinámico** de vehículos dentro (`inside`).
* Función `process_plate(plate_text)` que devuelve:

  * `status`: "Registrado" o "Visitante".
  * `action`: "Ingreso" o "Salida".

---

## 📌 Ejemplo de flujo

1. Se detecta la placa **ITR192**.

   * Está en la base → `Registrado`.
   * No estaba en `inside` → se marca como `Ingreso`.

2. Se detecta la placa **ABC111**.

   * No está en la base → `Visitante`.
   * No estaba en `inside` → se marca como `Ingreso`.

3. Se detecta de nuevo **ITR192**.

   * Estaba en `inside` → se marca como `Salida`.

---


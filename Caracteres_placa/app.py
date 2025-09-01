# ===============================
# PROGRAMA DE DETECCIÓN DE PLACAS
# ===============================
# Este script utiliza un modelo YOLOv8 entrenado para detectar placas vehiculares
# y la librería PaddleOCR para reconocer los caracteres en la placa detectada.
# Luego, con la lógica de negocio importada desde "logic.py", determina
# si el vehículo corresponde a un ingreso/salida y si es visitante o registrado.

# -------------------------------
# Importar librerías necesarias
# -------------------------------
from ultralytics import YOLO           # Para detección de placas
from paddleocr import PaddleOCR        # Para reconocimiento de caracteres en placas
import cv2                             # Para procesamiento de imágenes
import imutils                         # Para redimensionar imágenes en visualización
import re                              # Para expresiones regulares (validación de caracteres)
from logic import process_plate        # Lógica de negocio: visitante/registrado + ingreso/salida

# -------------------------------
# Cargar imagen de entrada
# -------------------------------
# La imagen sobre la cual se va a realizar la detección de placa
image = cv2.imread("/Users/pipepatino/Desktop/Portafolio/Pruebas_Tecnicas/Yamaha_v1/YOLO/dataset_yolo/test/images/2665823596_47018de3b1_w_jpg.rf.9501105d67596192fbe463d57012c7a6.jpg")

# -------------------------------
# Inicializar modelos
# -------------------------------
# Modelo YOLOv8 entrenado para detectar placas vehiculares
model = YOLO("/Users/pipepatino/Desktop/Portafolio/Pruebas_Tecnicas/Yamaha_v1/YOLO/runs/weights/best.pt")
# PaddleOCR configurado en inglés con corrección de inclinación de texto
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# -------------------------------
# Detección de placas con YOLO
# -------------------------------
results = model(image)  # Ejecutar YOLO sobre la imagen

# Iterar sobre los resultados obtenidos por YOLO
for result in results:
    # Filtrar detecciones que correspondan a la clase "placa" (cls == 0)
    index_plates = (result.boxes.cls == 0).nonzero(as_tuple=True)[0]

    # Procesar cada placa detectada
    for idx in index_plates:
        # Obtener nivel de confianza de la detección
        conf = result.boxes.conf[idx].item()
        if conf > 0.4:  # Solo considerar detecciones con confianza > 40%

            # Extraer coordenadas de la caja delimitadora (bounding box)
            xyxy = result.boxes.xyxy[idx].squeeze().tolist()
            x1, y1 = int(xyxy[0]), int(xyxy[1])
            x2, y2 = int(xyxy[2]), int(xyxy[3])
            
            # Recortar la región de la placa con un padding adicional
            plate_image = image[y1-15:y2+15, x1-15:x2+15]

            # -------------------------------
            # Reconocimiento de caracteres con OCR
            # -------------------------------
            result_ocr = ocr.predict(cv2.cvtColor(plate_image, cv2.COLOR_BGR2RGB))

            # Ordenar los caracteres detectados de izquierda a derecha
            boxes = result_ocr[0]['rec_boxes']
            texts = result_ocr[0]['rec_texts']
            left_to_right = sorted(zip(boxes, texts), key=lambda x: min(x[0][::2]))
            print(f"left_to_right:", left_to_right)
            
            # -------------------------------
            # Filtrado de caracteres válidos
            # -------------------------------
            # Solo se aceptan letras mayúsculas y números
            whitelist_pattern = re.compile(r'^[A-Z0-9]+$')
            left_to_right = ''.join([t for _, t in left_to_right])
            output_text = ''.join([t for t in left_to_right if whitelist_pattern.fullmatch(t)])
            output_text = output_text[:6]  # Limitar a 6 caracteres (formato placa)
            print(f"output_text: {output_text}")
            
            # -------------------------------
            # Lógica de negocio: ingreso/salida + visitante/registrado
            # -------------------------------
            if output_text:
                status, action = process_plate(output_text)
                print(f"Placa: {output_text} | {status} | {action}")

                # Dibujar el texto en la imagen con la información extra
                cv2.putText(image, f"{output_text} - {status} - {action}",
                            (x1-7, y1-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

            # -------------------------------
            # Visualización de resultados
            # -------------------------------
            cv2.imshow("plate_image", plate_image)  # Mostrar solo la placa recortada
            # Dibujar caja y texto sobre la imagen completa
            cv2.rectangle(image, (x1 - 10, y1 - 35), (x2 + 10, y2-(y2 -y1)), (0, 255, 0), -1)
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, output_text, (x1-7, y1-5), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 2)
            
# -------------------------------
# Mostrar la imagen final con resultados
# -------------------------------
cv2.imshow("Image", imutils.resize(image, width=720))
cv2.waitKey(0)
cv2.destroyAllWindows()

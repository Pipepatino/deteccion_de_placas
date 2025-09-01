"""
Módulo de lógica para identificar el estado de un vehículo detectado:
- Determina si la placa pertenece a un vehículo registrado o a un visitante.
- Determina si el vehículo está ingresando o saliendo de las instalaciones.

Este módulo utiliza una base de datos simulada de placas registradas
y un conjunto dinámico que guarda el estado actual de los vehículos
que están dentro.
"""

# ----------------------------------------
# Placas registradas (simulación o base sintética)
# ----------------------------------------
# En un sistema real estas placas podrían provenir de una base de datos,
# aquí se definen manualmente como un conjunto de ejemplo.
registered_plates = {"ITR192", "XYZ789", "MNO456"}

# ----------------------------------------
# Estado de vehículos que están dentro
# ----------------------------------------
# Este conjunto mantiene un registro dinámico de las placas de vehículos
# que ya ingresaron y no han salido todavía.
inside = set()

# ----------------------------------------
# Función principal de procesamiento
# ----------------------------------------
def process_plate(plate_text: str):
    """
    Procesa la placa detectada por el sistema de OCR.

    Determina si el vehículo es un visitante o un registrado
    y define si la detección corresponde a un ingreso o a una salida.

    Args:
        plate_text (str): texto de la placa detectada por OCR.

    Returns:
        tuple: (status, action)
            - status: "Registrado" si la placa está en la base de datos
                      o "Visitante" en caso contrario.
            - action: "Ingreso" si la placa no estaba previamente en el conjunto
                      de vehículos dentro, o "Salida" si ya estaba registrada
                      y se retira del conjunto.
    """
    # Determinar si es un vehículo registrado o visitante
    status = "Registrado" if plate_text in registered_plates else "Visitante"

    # Determinar si corresponde a un ingreso o a una salida
    if plate_text not in inside:
        inside.add(plate_text)   # Guardar que el vehículo entró
        action = "Ingreso"
    else:
        inside.remove(plate_text)  # Retirar el vehículo que salió
        action = "Salida"

    return status, action

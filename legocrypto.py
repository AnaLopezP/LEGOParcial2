import cv2
import numpy as np

# Definir rangos de colores en HSV para identificar colores específicos de LEGO
color_ranges = {
    'rojo': ([0, 120, 70], [10, 255, 255]),
    'azul': ([100, 150, 0], [140, 255, 255]),
    'verde': ([40, 70, 70], [80, 255, 255]),
    'amarillo': ([20, 100, 100], [30, 255, 255]),
    'naranja': ([10, 100, 100], [20, 255, 255])
}

# Valores de desplazamiento asociados a cada color
desplazamientos = {
    'rojo': 3,
    'azul': 5,
    'verde': 2,
    'amarillo': 4,
    'naranja': 7
}

def procesar_imagen(image_path):
    """Procesa una imagen y calcula el desplazamiento total basado en los colores de las piezas de LEGO."""
    image = cv2.imread(image_path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    total_desplazamiento = 0

    for color, (lower, upper) in color_ranges.items():
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        mask = cv2.inRange(hsv, lower, upper)
        if np.sum(mask) > 0:  # Si hay píxeles del color presente
            total_desplazamiento += desplazamientos[color]
            print(f"Detectado color {color} con desplazamiento de {desplazamientos[color]}")

    return total_desplazamiento

def cifrar(texto, image_path):
    desplazamiento = procesar_imagen(image_path)
    cifrado = ""
    for char in texto:
        if char.isalpha():
            shift = (ord(char.lower()) - ord('a') + desplazamiento) % 26 + ord('a')
            cifrado += chr(shift) if char.islower() else chr(shift).upper()
        else:
            cifrado += char
    return cifrado

def descifrar(texto, image_path):
    desplazamiento = procesar_imagen(image_path)
    descifrado = ""
    for char in texto:
        if char.isalpha():
            shift = (ord(char.lower()) - ord('a') - desplazamiento) % 26 + ord('a')
            descifrado += chr(shift) if char.islower() else chr(shift).upper()
        else:
            descifrado += char
    return descifrado

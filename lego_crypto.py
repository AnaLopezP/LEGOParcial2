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

# Asociar cada letra a un color y su respectivo desplazamiento
asociaciones_letra_color = {
    'a': ('rojo', 3),
    'b': ('azul', 5),
    'c': ('verde', 2),
    'd': ('amarillo', 4),
    'e': ('naranja', 7)
}

def procesar_imagen(image_path):
    """Procesa una imagen y devuelve las letras asociadas a cada color."""
    image = cv2.imread(image_path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    letras_detectadas = []

    for color, (lower, upper) in color_ranges.items():
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        mask = cv2.inRange(hsv, lower, upper)
        if np.sum(mask) > 0:  # Si hay píxeles del color presente
            letras_detectadas.append(color[0].lower())  # Tomamos la primera letra del color como identificador

    return letras_detectadas

def cifrar(texto, image_path):
    letras_detectadas = procesar_imagen(image_path)
    cifrado = ""
    for char, letra_color in zip(texto, letras_detectadas):
        if char.isalpha():
            color, desplazamiento = asociaciones_letra_color[char.lower()]
            shift = (ord(char.lower()) - ord('a') + desplazamiento) % 26 + ord('a')
            cifrado += chr(shift) if char.islower() else chr(shift).upper()
        else:
            cifrado += char
    return cifrado

def descifrar(texto, image_path):
    letras_detectadas = procesar_imagen(image_path)
    descifrado = ""
    for char, letra_color in zip(texto, letras_detectadas):
        if char.isalpha():
            color, desplazamiento = asociaciones_letra_color[char.lower()]
            shift = (ord(char.lower()) - ord('a') - desplazamiento) % 26 + ord('a')
            descifrado += chr(shift) if char.islower() else chr(shift).upper()
        else:
            descifrado += char
    return descifrado

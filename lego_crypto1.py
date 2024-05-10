import cv2
import numpy as np
import gradio as gr
'''
Según los colores de la imagen desplaza las letras del mensaje. 
Ejemplo: Si solo ponemos el azul y la palabra baca pues cambia a Gaca. Si le añadimos más colores, nos cambia más letras.
'''

# Definir rangos de colores en HSV para identificar colores específicos de LEGO
color_ranges = {
    'rojo': ([0, 120, 70], [10, 255, 255]),
    'azul': ([100, 150, 0], [140, 255, 255]),
    'verde': ([40, 70, 70], [80, 255, 255]),
    'amarillo': ([20, 100, 100], [30, 255, 255]),
    'naranja': ([10, 100, 100], [20, 255, 255])
}

# Mapeo de colores a números de cifrado de César y letras
colores_info = {
    'rojo': {'letra': 'a', 'cesar': 3},
    'azul': {'letra': 'b', 'cesar': 5},
    'verde': {'letra': 'c', 'cesar': 2},
    'amarillo': {'letra': 'd', 'cesar': 4},
    'naranja': {'letra': 'e', 'cesar': 7}
}

def procesar_imagen(image_path):
    """Procesa una imagen y detecta los colores de las piezas de LEGO."""
    image = cv2.imread(image_path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    colores_detectados = {}

    for color, (lower, upper) in color_ranges.items():
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        mask = cv2.inRange(hsv, lower, upper)
        if np.sum(mask) > 0:  # Si hay píxeles del color presente
            colores_detectados[colores_info[color]['letra']] = color
            print(f"Detectado color {color} correspondiente a la letra {colores_info[color]['letra']}")

    return colores_detectados

def cifrar(texto, image_path):
    colores_detectados = procesar_imagen(image_path)
    cifrado = ""
    for char in texto:
        if char.isalpha():
            color = colores_detectados.get(char.upper())
            if color:
                shift = colores_info[color]['cesar'] if 'cesar' in colores_info[color] else 0
                cifrado += chr((ord(char.upper()) - ord('A') + shift) % 26 + ord('A'))
            else:
                cifrado += char
        else:
            cifrado += char
    return cifrado

def descifrar(texto, image_path):
    colores_detectados = procesar_imagen(image_path)
    descifrado = ""
    for char in texto:
        if char.isalpha():
            color = colores_detectados.get(char.upper())
            if color:
                shift = colores_info[color]['cesar'] if 'cesar' in colores_info[color] else 0
                descifrado += chr((ord(char.upper()) - ord('A') - shift) % 26 + ord('A'))
            else:
                descifrado += char
        else:
            descifrado += char
    return descifrado
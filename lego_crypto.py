import cv2
import numpy as np
import gradio as gr

# Definir los rangos de colores en HSV para identificar colores específicos de LEGO
color_ranges = {
    'rojo': ([0, 120, 70], [10, 255, 255]),
    'azul': ([100, 150, 0], [140, 255, 255])
}

# Valores de desplazamiento asociados a cada color
desplazamientos = {
    'rojo': 3,
    'azul': 5
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
    return cifrar(texto, -desplazamiento)

# Configuración de Gradio UI para cifrar
cifrar_interface = gr.Interface(
    fn=cifrar,
    inputs=[gr.Textbox(lines=2, placeholder="Introduce tu mensaje aquí..."), gr.Image(type="filepath")],
    outputs="text",
    title="Cifrado César con LEGO",
    description="Sube una imagen de tus piezas de LEGO para determinar el desplazamiento y luego cifra tu mensaje."
)

# Configuración de Gradio UI para descifrar
descifrar_interface = gr.Interface(
    fn=descifrar,
    inputs=[gr.Textbox(lines=2, placeholder="Introduce tu mensaje aquí..."), gr.Image(type="filepath")],
    outputs="text",
    title="Descifrado César con LEGO",
    description="Sube una imagen de tus piezas de LEGO para determinar el desplazamiento y luego descifra tu mensaje."
)

# Configuración de la demo
demo = gr.TabbedInterface(
    [cifrar_interface, descifrar_interface],
    ["Cifrar", "Descifrar"]
)

if __name__ == "__main__":
    demo.launch()

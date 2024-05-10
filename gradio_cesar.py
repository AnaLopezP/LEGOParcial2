# CIFRADO Y DESCIFRADO CESAR
import gradio as gr

def cifrar(texto, desplazamiento):
    resultado = ""
    for i in range(len(texto)):
        char = texto[i]
        if char.isalpha():
            shift = desplazamiento % 26
            if char.isupper():
                resultado += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                resultado += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            resultado += char
    return resultado

def descifrar(texto, desplazamiento):
    return cifrar(texto, -desplazamiento)

iface = gr.Interface(
    fn={"Cifrar": cifrar, "Descifrar": descifrar},
    inputs=[gr.Textbox(label="Texto"), gr.Slider(1, 25, label="Desplazamiento")],
    outputs="text",
    title="Taller de Criptografía con LEGO",
    description="Utiliza este herramienta para cifrar o descifrar mensajes usando el cifrado César."
)

iface.launch()
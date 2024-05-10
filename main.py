import gradio as gr
from lego_crypto import cifrar, descifrar

def main():
    # Interfaz Gradio para cifrar
    cifrar_interface = gr.Interface(
        fn=cifrar,
        inputs=[gr.Textbox(lines=2, placeholder="Introduce tu mensaje aquí..."), gr.Image(type="filepath")],
        outputs="text",
        title="Cifrado César con LEGO",
        description="Sube una imagen de tus piezas de LEGO para determinar el desplazamiento y luego cifra tu mensaje."
    )

    # Interfaz Gradio para descifrar
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

    demo.launch()

if __name__ == "__main__":
    main()

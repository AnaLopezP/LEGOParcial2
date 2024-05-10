# LEGOParcial2
https://github.com/AnaLopezP/LEGOParcial2.git

# Integrantes del Grupo
Ana Lopez
Andrea Manuel
Paula Naranjo

# ¿Qué hay que hacer?

Enunciado del Taller: "Descifrando Secretos con LEGO"
¡Bienvenidos, jóvenes criptógrafos! Hoy, vamos a embarcarnos en una aventura donde usaremos piezas de LEGO para desbloquear los secretos de la criptografía. Vamos a aprender cómo podemos proteger mensajes secretos usando diferentes claves y cómo podemos descifrar mensajes que alguien más ha cifrado. ¡Presten atención y prepárense para poner a prueba su ingenio y creatividad!

Parte 1: Construcción de Claves de Cifrado con LEGO
Objetivo: Crear una clave de cifrado utilizando piezas de LEGO que representarán diferentes valores de desplazamiento en un cifrado César.

Materiales:

Piezas de LEGO de varios colores.
Tabla de colores y valores asignados (por ejemplo, rojo = 3, azul = 5).
Pasos:

Entender el Cifrado César:

Un cifrado César es un tipo de cifrado por sustitución en el que cada letra del texto se reemplaza por otra que se encuentra un número fijo de posiciones más adelante en el alfabeto.
Ejemplo: Si usamos un desplazamiento de 3, 'A' se convierte en 'D', 'B' se convierte en 'E', etc.
Construye tu Clave:

Selecciona diferentes piezas de LEGO para construir tu clave de cifrado. El color de cada pieza determinará el valor de desplazamiento.
Ejemplo: Si eliges tres piezas rojas, tu desplazamiento será 9 (3 piezas x 3 de desplazamiento cada una).
Registra tu Clave:

Anota la combinación de colores que has elegido y calcula el desplazamiento total.
Ejemplo: Rojo, Rojo, Azul = 3 + 3 + 5 = 11.
Parte 2: Cifrar y Descifrar Mensajes
Objetivo: Usar la aplicación Gradio para cifrar y descifrar mensajes utilizando las claves de LEGO que has construido.

Pasos:

Cifra un Mensaje:

Ingresa un mensaje corto en la aplicación.
Aplica tu desplazamiento para cifrar el mensaje.
Ejemplo: Mensaje: "HOLA". Desplazamiento: 11. Mensaje cifrado: "SZWE".
Intercambia Mensajes Cifrados:

Intercambia tu mensaje cifrado con otro grupo.
Intenta descifrar el mensaje que recibiste usando diferentes desplazamientos.
Descifra el Mensaje:

Usa la aplicación para probar diferentes desplazamientos hasta que el mensaje tenga sentido.
Ejemplo: Mensaje cifrado: "SZWE". Desplazamientos probados: 5, 8, 11. Mensaje descifrado con 11: "HOLA".
Parte 3: Desafío de Criptografía
Objetivo: Descifrar un mensaje dado sin conocer la clave, utilizando diferentes combinaciones de piezas de LEGO.

Pasos:

Recibe un Mensaje Cifrado:

Cada grupo recibirá un mensaje cifrado de otro grupo sin saber el desplazamiento usado.
Descifra el Mensaje:

Prueba diferentes combinaciones de piezas de LEGO para cambiar el desplazamiento y descifrar el mensaje.
Ejemplo: Mensaje cifrado: "QTI". Desplazamientos probados: 2, 4, 7, etc., hasta descifrarlo correctamente.
Comparte tu Solución:

Una vez descifrado, comparte cómo lo lograste y qué desplazamiento resultó ser el correcto.
Descripción del Taller
Este taller está diseñado para introducir a los estudiantes en los fundamentos de la criptografía y la seguridad digital de una manera divertida y accesible. Utilizando una aplicación desarrollada en Gradio, que se integra con modelos de Hugging Face, los estudiantes aprenderán sobre cifrado y descifrado, mientras utilizan piezas de LEGO para representar visualmente los datos y las claves de cifrado.

Objetivos
Entender los principios básicos del cifrado y el descifrado.
Aprender sobre la importancia de la seguridad digital.
Desarrollar habilidades de pensamiento crítico y resolución de problemas.
Materiales Necesarios
Piezas de LEGO de varios colores y formas.
Ordenadores o tablets con acceso a internet.
Proyector para demostraciones grupales.
Para incorporar la funcionalidad de interpretar fotos de piezas de LEGO y determinar el desplazamiento para el cifrado César a partir de ellas, necesitaremos integrar técnicas de visión por computadora. Esto puede hacerse utilizando una biblioteca de Python como OpenCV para procesar las imágenes y luego aplicar un modelo de aprendizaje automático para clasificar las piezas por color. Aquí te explico cómo puedes configurar este sistema:

1. Instalación de Bibliotecas Necesarias
Para comenzar, necesitarás instalar algunas bibliotecas si aún no las tienes. Puedes hacerlo mediante los siguientes comandos:

pip install gradio
pip install opencv-python-headless
pip install numpy
2. Configuración del Código de Python
Vamos a escribir un código que utilice OpenCV para detectar colores de las piezas de LEGO en una imagen y determinar el desplazamiento basado en esos colores. Aquí tienes un ejemplo básico de cómo podrías configurar esto:

import cv2
import numpy as np
import gradio as gr

#Definir los rangos de colores en HSV para identificar colores específicos de LEGO
color_ranges = {
    'rojo': ([0, 120, 70], [10, 255, 255]),
    'azul': ([100, 150, 0], [140, 255, 255])
}

#Valores de desplazamiento asociados a cada color
desplazamientos = {
    'rojo': 3,
    'azul': 5
}

def procesar_imagen(image_path):
    # Leer la imagen
    image = cv2.imread(image_path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    total_desplazamiento = 0

    # Procesar cada color definido
    for color, (lower, upper) in color_ranges.items():
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        # Crear máscara para el color actual y calcular el desplazamiento
        mask = cv2.inRange(hsv, lower, upper)
        if np.sum(mask) > 0:  # Si hay píxeles del color presente
            total_desplazamiento += desplazamientos[color]

    return total_desplazamiento

def cifrar(texto, image):
    desplazamiento = procesar_imagen(image.name)
    cifrado = ""
    for char in texto:
        if char.isalpha():
            shift = (ord(char.lower()) - ord('a') + desplazamiento) % 26 + ord('a')
            cifrado += chr(shift) if char.islower() else chr(shift).upper()
        else:
            cifrado += char
    return cifrado

def descifrar(texto, image):
    desplazamiento = procesar_imagen(image.name)
    return cifrar(texto, -desplazamiento)

#Configuración de Gradio UI
iface = gr.Interface(
    fn={"Cifrar": cifrar, "Descifrar": descifrar},
    inputs=[gr.Textbox(lines=2, placeholder="Introduce tu mensaje aquí..."), gr.Image(type="file")],
    outputs="text",
    title="Cifrado César con LEGO",
    description="Sube una imagen de tus piezas de LEGO para determinar el desplazamiento y luego cifra o descifra tu mensaje."
)

if __name__ == "__main__":
    iface.launch()
3. Uso de la Aplicación
Ejecutar el Script: Lanza el script en tu terminal con python lego_crypto.py.
Interactuar con la Aplicación: La aplicación se abrirá en el navegador. Los usuarios pueden subir una foto de sus piezas de LEGO y la aplicación determinará automáticamente el desplazamiento basado en los colores detectados. Después, pueden cifrar o descifrar mensajes utilizando este desplazamiento.
Consideraciones
Ajuste de Rangos de Color: Los rangos de color en el código son solo ejemplos y pueden necesitar ajustes precisos para funcionar correctamente con las piezas de LEGO que uses en tu taller.
Iluminación y Calidad de la Imagen: El rendimiento de la detección de color puede verse afectado por la iluminación y la calidad de la imagen, por lo que es recomendable tomar fotos en condiciones de iluminación consistentes y buenas.
Este sistema permite a los estudiantes experimentar con criptografía de una manera interactiva y visual, utilizando tecnología avanzada en un contexto educativo divertido y accesible.

Paso 1: Preparación de Materiales
Antes de comenzar la actividad, asegúrate de que cada grupo de estudiantes tenga los siguientes materiales:

Piezas de LEGO en varios colores.
Una cámara digital o un smartphone para tomar fotos de las configuraciones de LEGO.
Acceso a un ordenador con la aplicación Gradio instalada y lista para usar.
Paso 2: Introducción y Teoría
2.1 Explicación del Cifrado César
Objetivo: Introducir a los estudiantes al concepto de cifrado César y cómo se puede utilizar para cifrar y descifrar mensajes.

Procedimiento:

Definición y Contexto:

Explica que el cifrado César es un tipo de cifrado por sustitución en el que cada letra en el texto es reemplazada por otra letra que se encuentra un número fijo de posiciones más adelante en el alfabeto.
Menciona que este método fue nombrado así debido a Julio César, quien lo utilizaba para comunicarse con sus generales.
Ejemplo Visual:

Utiliza una pizarra o un proyector para mostrar el alfabeto en una línea horizontal.
Dibuja un segundo alfabeto debajo del primero, pero comenzando desde la letra "D" para ilustrar un desplazamiento de tres posiciones (A -> D, B -> E, C -> F, etc.).
Explica que este desplazamiento se aplica a cada letra del mensaje original para obtener el mensaje cifrado.
Ejemplo Práctico:

Escribe un mensaje corto, como "HOLA", en la pizarra.
Aplica el cifrado César con un desplazamiento de tres y escribe el mensaje cifrado resultante, "KROD", mostrando cada paso del proceso.
2.2 Demostración
Objetivo: Mostrar cómo el cifrado César se aplica a un mensaje real.

Procedimiento:

Selecciona un mensaje simple y escribe en la pizarra.
Cifra el mensaje paso a paso:
Apunta a cada letra del mensaje original y cuenta tres posiciones hacia adelante en el alfabeto mostrado.
Reemplaza cada letra por la correspondiente en el alfabeto desplazado y escribe el resultado.
Discute cómo diferentes desplazamientos (por ejemplo, 1, 5, o 10) cambiarían el mensaje cifrado.
Paso 3: Construcción de Claves de Cifrado
3.1 Selección de Piezas
Objetivo: Permitir que los estudiantes elijan piezas de LEGO para crear claves de cifrado basadas en colores específicos.

Procedimiento:

Explica que cada color de LEGO representará un número específico de desplazamientos en el cifrado César.
Asigna un valor a cada color de pieza de LEGO disponible (por ejemplo, rojo = 3, azul = 5, verde = 2).
Invita a los estudiantes a seleccionar varias piezas de LEGO de diferentes colores según la clave de cifrado que deseen crear.
3.2 Construcción de la Clave
Objetivo: Construir una clave de cifrado utilizando las piezas de LEGO seleccionadas.

Procedimiento:

Instructa a los estudiantes a apilar o alinear sus piezas de LEGO seleccionadas para visualizar su clave.
Calcula el desplazamiento total sumando los valores de todas las piezas de LEGO en la pila.
Ejemplo: Si un estudiante selecciona dos piezas rojas y una azul, el desplazamiento total sería 3 (rojo) + 3 (rojo) + 5 (azul) = 11.
Anima a los estudiantes a experimentar con diferentes combinaciones para ver cómo cambian los desplazamientos.
3.3 Registro de la Clave
Objetivo: Registrar la clave de cifrado creada para su uso en la actividad de cifrado y descifrado.

Procedimiento:

Proporciona hojas de papel y bolígrafos/lápices.
Pide a los estudiantes que escriban la combinación de colores de sus piezas de LEGO y el desplazamiento total calculado.
Guarda esta información, ya que será usada para cifrar y descifrar mensajes en los pasos siguientes de la actividad.
Paso 4: Fotografiar las Claves
Tomar Fotos: Cada grupo toma una foto clara de su configuración de LEGO desde una vista superior para asegurarse de que los colores sean claramente visibles.

Cargar Fotos: Los estudiantes cargan la foto en la aplicación Gradio a través de la interfaz de usuario en la computadora.

Paso 5: Cifrar y Descifrar Mensajes
Ingreso del Mensaje: Los estudiantes ingresan un mensaje que desean cifrar en la aplicación.

Aplicación del Cifrado: Usan la función de cifrado de la aplicación, que automáticamente calcula el desplazamiento basado en la imagen de las piezas de LEGO y muestra el mensaje cifrado.

Intercambio de Mensajes Cifrados: Los grupos intercambian sus mensajes cifrados con otros grupos.

Descifrado de Mensajes: Cada grupo intenta descifrar el mensaje que recibieron utilizando la aplicación, ajustando los desplazamientos si es necesario o utilizando la clave proporcionada por el otro grupo para verificar el resultado.

Actividades del Taller
Introducción Teórica (15 minutos):

Breve explicación sobre qué es la criptografía y por qué es importante.
Introducción a los conceptos de cifrado y descifrado.
Demostración de la Aplicación Gradio (15 minutos):

Demostración de cómo usar la aplicación desarrollada en Gradio.
Ejemplos de cómo cifrar y descifrar mensajes utilizando modelos de Hugging Face.
Actividad Práctica con LEGO (30 minutos):

Los estudiantes usan piezas de LEGO para construir 'claves' que representan diferentes métodos de cifrado (por ejemplo, desplazamiento de cifrado César).
Utilizan la aplicación para cifrar y descifrar mensajes simples usando las 'claves' de LEGO.
Desafío de Criptografía (20 minutos):

Los estudiantes intentan descifrar un mensaje dado sin conocer la clave, usando piezas de LEGO para probar diferentes posibilidades.
Discusión sobre cómo diferentes métodos de cifrado pueden ser más seguros que otros.
Discusión y Reflexión Final (10 minutos):

Reflexión sobre lo que aprendieron y cómo la criptografía afecta la seguridad en la vida diaria.
Discusión sobre cómo la tecnología puede ayudar a mejorar la seguridad digital.
Implementación Técnica
La aplicación Gradio se integrará con modelos de procesamiento de lenguaje natural de Hugging Face para simular el cifrado y descifrado. La interfaz permitirá a los usuarios ingresar mensajes y seleccionar diferentes métodos de cifrado, con una representación visual de cómo cambia el mensaje cifrado.

Esta combinación de actividades prácticas con tecnología avanzada ofrece una manera atractiva y educativa de enseñar principios importantes de la informática y la criptografía, fomentando a la vez el uso creativo de las piezas de LEGO.

1. Preparar el Entorno de Desarrollo
Necesitarás tener Python instalado en tu sistema. Puedes descargarlo desde python.org.

2. Instalación de Bibliotecas Necesarias
Abre tu terminal y ejecuta los siguientes comandos para instalar las bibliotecas necesarias:


pip install gradio
pip install transformers
3. Crear el Script de Python
Aquí tienes un ejemplo básico de cómo podrías configurar una aplicación Gradio que utiliza un modelo simple de cifrado y descifrado (por ejemplo, cifrado César para simplicidad):


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
4. Ejecutar el Script y Acceder a la Aplicación
Una vez que hayas guardado tu script, puedes ejecutarlo desde la terminal. Esto abrirá una interfaz en tu navegador donde puedes interactuar con las funciones de cifrado y descifrado.

5. Desarrollo de Actividades Complementarias
Para que el taller sea interactivo y práctico, puedes integrar actividades donde los estudiantes usen las piezas de LEGO para representar las claves de cifrado de forma física y luego aplicarlas en la aplicación.

Enlaces Útiles
Documentación de Gradio
Transformers Library de Hugging Face
Python.org para descargas de Python
Notas Adicionales
Asegúrate de probar la aplicación en diferentes dispositivos que se usarán durante el taller para asegurar la compatibilidad.
Considera la posibilidad de agregar funcionalidades adicionales o complejidad a medida que los estudiantes se familiaricen con los conceptos básicos.
Con este setup, podrás llevar a cabo un taller que no solo enseña criptografía de manera práctica y visual, sino que también introduce a los estudiantes en el desarrollo de aplicaciones con Python y el uso de bibliotecas modernas de IA.


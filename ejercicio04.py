import pyfiglet
import random

def obtener_fuentes_disponibles():
    return pyfiglet.FigletFont.getFonts()

def generar_texto_ascii(texto, fuente):
    return pyfiglet.figlet_format(texto, font=fuente)

fuentes_disponibles = obtener_fuentes_disponibles()

print("Generador de texto ASCII con pyfiglet")
print(f"Fuentes disponibles: {len(fuentes_disponibles)}")

fuente_usuario = input("Ingrese el nombre de la fuente (presione Enter para selección aleatoria): ").strip()

if not fuente_usuario:
    fuente_seleccionada = random.choice(fuentes_disponibles)
    print(f"Fuente seleccionada aleatoriamente: {fuente_seleccionada}")
else:
    if fuente_usuario in fuentes_disponibles:
        fuente_seleccionada = fuente_usuario
        print(f"Fuente seleccionada: {fuente_seleccionada}")
    else:
        print(f"Fuente '{fuente_usuario}' no encontrada. Seleccionando aleatoriamente...")
        fuente_seleccionada = random.choice(fuentes_disponibles)
        print(f"Fuente seleccionada: {fuente_seleccionada}")

texto_usuario = input("Ingrese el texto a convertir: ")

try:
    resultado = generar_texto_ascii(texto_usuario, fuente_seleccionada)
    print("\nTexto generado:")
    print(resultado)
except:
    print("Error al generar el texto. Usando fuente por defecto...")
    resultado = generar_texto_ascii(texto_usuario, 'standard')
    print("\nTexto generado:")
    print(resultado)
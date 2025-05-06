import pandas as pd
import xml.etree.ElementTree as ET
import sys
import os

# Verifica que se pasó un argumento
if len(sys.argv) < 2:
    print("Uso: python cargar_dataset.py ruta/al/archivo.xml")
    sys.exit(1)

# Obtener la ruta del archivo XML desde los argumentos
ruta_xml = sys.argv[1]

# Obtener nombre base del archivo (sin extensión)
nombre_sin_extension = os.path.splitext(os.path.basename(ruta_xml))[0]

# Parsear el archivo XML
tree = ET.parse(ruta_xml)
root = tree.getroot()

# Extraer mensajes del XML (esto dependerá de la estructura real del XML)
datos = []

for conversation in root.findall("conversation"):  # Ajusta si la etiqueta es diferente
    for message in conversation.findall("message"):
        autor = message.find("author").text if message.find("author") is not None else ""
        texto = message.find("text").text if message.find("text") is not None else ""
        timestamp = message.find("time").text if message.find("time") is not None else ""
        datos.append({"autor": autor, "mensaje": texto, "timestamp": timestamp})

# Crear DataFrame y guardar como CSV
df = pd.DataFrame(datos)
csv_salida = f"{nombre_sin_extension}.csv"
df.to_csv(csv_salida, index=False, encoding="utf-8")

print(f"✅ Dataset guardado como: {csv_salida}")
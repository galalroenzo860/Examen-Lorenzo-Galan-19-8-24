from PIL import Image
import os

nombre_imagen = input("Ingrese el nombre de la imagen (incluyendo la extensión): ")
   

if not os.path.exists(nombre_imagen):
    print("Error: La imagen especificada no existe.")
   


imagen = Image.open(nombre_imagen)

ancho_original, alto_original = imagen.size
x = int(input("Ingrese la coordenada X inicial para el recorte: "))
y = int(input("Ingrese la coordenada Y inicial para el recorte: "))
ancho = int(input("Ingrese el ancho del recorte: "))
alto = int(input("Ingrese el alto del recorte: "))
       

if x < 0 or y < 0 or x + ancho > ancho_original or y + alto > alto_original:
    print("Error: Los parámetros de recorte exceden los límites de la imagen original.")

imagen_recortada = imagen.crop((x, y, x + ancho, y + alto))
       
nombre_base, extension = os.path.splitext(nombre_imagen)
nombre_recorte = f"{nombre_base}_recortada{extension}"
       
imagen_recortada.save(nombre_recorte)
print(f"La imagen recortada se guardo como: {nombre_recorte}")
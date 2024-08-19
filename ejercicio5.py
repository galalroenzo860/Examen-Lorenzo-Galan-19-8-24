from PIL import Image
import os

print("ingrese la ubicacion del archivo")
url = input()
img = Image.open(url).convert("RGBA")
print("Ingrese la marca de agua")

urlMarca = input()
waterMark = Image.open(urlMarca).convert("RGBA")

print("""
    Ingrese el numero de opcion que desea colocar la marca de agua
    [1] Superior Izquierda
    [2] Superior Derecha
    [3] Inferior Izquierda
    [4] Inferior Derecha
    """)
opElig = int(input())

img_ancho, img_altura = img.size
waterMark_ancho, waterMark_altura = waterMark.size
margen = 50
if opElig == 1 :
    posicion = (margen, margen)
elif opElig == 2 :
    posicion = (img_ancho - waterMark_ancho - margen, margen)
elif opElig == 3 :
    posicion = (margen, img_altura - img_altura - margen)
elif opElig == 4:
    posicion = (img_ancho - waterMark_ancho - margen, img_altura - waterMark_altura - margen)
else:
    print("Ubicación no válida. Debe ser una de las opciones especificadas.")

img.paste(waterMark, posicion, waterMark)
img.show()
nombre_archivo, extension = os.path.splitext(os.path.basename(url))
nuevo_nombre = f"{nombre_archivo}_con_marca{extension}"
nuevo_archivo = os.path.join(os.path.dirname(url), nuevo_nombre)
img.save(nuevo_archivo)
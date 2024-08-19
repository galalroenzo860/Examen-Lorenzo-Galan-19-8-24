from PIL import Image
import os

print("ingrese la ubicacion del archivo")
url = input()
img = Image.open(url)

print("Ingrese el angulo de rotacion que desea aplicar en la Imagen")
rot = int(input())
imagen_rotada = img.rotate(rot, expand=True)
imagen_rotada.show()
nombre_archivo, extension = os.path.splitext(os.path.basename(url))
nuevo_nombre = f"{nombre_archivo}Rot{extension}"
nuevo_archivo = os.path.join(os.path.dirname(url), nuevo_nombre)
imagen_rotada.save(nuevo_archivo)

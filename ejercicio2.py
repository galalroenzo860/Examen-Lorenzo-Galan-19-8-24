from PIL import Image
import os

print("ingrese la ubicacion del archivo")
url = input()
img = Image.open(url) 
img.show()
_, extension = os.path.splitext(url)
copiaImg = os.path.join(os.path.dirname(url), "Copia de imagen" + extension)
img.save(copiaImg)
print(f"Se creo la copia de la imagen con el nombre de Copia de Imagen.{extension}")
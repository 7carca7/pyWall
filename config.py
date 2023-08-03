"Configuración"


from datetime import date
import io
from tkinter.filedialog import asksaveasfilename
import requests
from PIL import Image


class Wallpaper:
    def __init__(self):
        self.url = "https://bing.biturl.top/?resolution=3840&format=json&index=0&mkt=en-US"

    def bing_wallpaper_url(self):
        "Obtiene la url de la imagen"

        response = requests.get(self.url, timeout=20)
        data = response.json()
        image_url = data["url"]
        image_descripcion = data["copyright"]
        descrip_limpia = image_descripcion.split(',')[0].split('(')[0]
        return image_url, descrip_limpia


class WallpaperDownload(Wallpaper):
    def __init__(self):
        super().__init__()

    def obtener_imagen(self):
        "Obtiene la imagen desde la URL"

        response = requests.get(self.bing_wallpaper_url()[0], timeout=20)
        raw_data = response.content
        imagen = Image.open(io.BytesIO(raw_data))
        return imagen

    def descargar_imagen(self):
        "Descarga la imagen"

        response = requests.get(self.bing_wallpaper_url()[0], timeout=20)

        fecha_actual = date.today()
        nombre = str(fecha_actual)+".jpg"

        guardado = asksaveasfilename(initialfile=nombre)
        if guardado:
            with open(guardado, "wb") as archivo:
                archivo.write(response.content)

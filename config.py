"Configuración"


from datetime import date
import io
from tkinter.filedialog import asksaveasfilename
import requests
from PIL import Image
import customtkinter as ctk


fecha_actual = date.today()
NOMBRE = str(fecha_actual)+".jpg"


def bing_wallpaper_url():
    "Obtiene la url de la imagen"

    api_url = "https://bing.biturl.top/?resolution=3840&format=json&index=0&mkt=en-US"
    response = requests.get(api_url, timeout=20)

    if response.status_code == 200:
        data = response.json()
        image_url = data["url"]
        image_descripcion = data["copyright"]
        return image_url, image_descripcion
    return None


url, descripcion = bing_wallpaper_url()


def descargar_imagen():
    "Descarga la imagen"

    resp = requests.get(url, timeout=20)
    resp.raise_for_status()

    guardado = asksaveasfilename(initialfile=NOMBRE)
    if guardado:
        with open(guardado, "wb") as archivo:
            archivo.write(resp.content)


respons = requests.get(url, timeout=10)
raw_data = respons.content


imagen = Image.open(io.BytesIO(raw_data))
photo = ctk.CTkImage(imagen, size=(500, 281))


descrip_limpia = descripcion.split(',')[0]
descrip_limpia = descripcion.split('(')[0]

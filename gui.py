"Interfaz gráfica"

import customtkinter as ctk
from config import Wallpaper, WallpaperDownload

wallpaper = Wallpaper()
wallpaper_download = WallpaperDownload()
photo = ctk.CTkImage(wallpaper_download.obtener_imagen(), size=(500, 281))

ventana = ctk.CTk()
ventana.configure()
ventana.geometry("520x340")
ventana.resizable(False, False)
ventana.title("pyWall")
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)


frame_principal = ctk.CTkFrame(ventana, fg_color="transparent")
frame_principal.grid(row=0, column=0, pady=0, sticky="nswe")
frame_principal.grid_rowconfigure(0, weight=4)
frame_principal.grid_rowconfigure(1, weight=0)
frame_principal.grid_columnconfigure(0, weight=1)


frame_imagen = ctk.CTkFrame(frame_principal, fg_color="transparent")
frame_imagen.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nswe")


label_imagen = ctk.CTkLabel(frame_imagen, image=photo, text="")
label_imagen.grid(row=0, column=0, sticky="nswe")


frame_botones = ctk.CTkFrame(frame_principal, fg_color="transparent")
frame_botones.grid(row=1, column=0, padx=10, pady=10, sticky="we")
frame_botones.grid_columnconfigure(0, weight=4)
frame_botones.grid_columnconfigure(1, weight=1)


descrip_imagen = ctk.CTkLabel(
    frame_botones, text=wallpaper.bing_wallpaper_url()[1], text_color="#e9967a", anchor="w")
descrip_imagen.grid(row=0, column=0, padx=0, sticky="we")


boton_descargar_imagen = ctk.CTkButton(
    frame_botones, text="Descargar", text_color=("#F6F6F6", "#242424"),
    command=wallpaper_download.descargar_imagen)
boton_descargar_imagen.grid(row=0, column=1, padx=0, sticky="e")
boton_descargar_imagen.configure(
    width=0, fg_color="#e9967a", hover_color="#C68068")


ventana.mainloop()

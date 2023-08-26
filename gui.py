"User interface"

import customtkinter as ctk
from config import Wallpaper, WallpaperDownload

wallpaper = Wallpaper()
wallpaper_download = WallpaperDownload()
photo = ctk.CTkImage(wallpaper_download.get_image(), size=(500, 281))

# MAIN APP
window = ctk.CTk()
window.configure()
window.geometry("520x340")
window.resizable(False, False)
window.title("pyWall")
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)


frame_main = ctk.CTkFrame(window, fg_color="transparent")
frame_main.grid(row=0, column=0, pady=0, sticky="nswe")
frame_main.grid_rowconfigure(0, weight=4)
frame_main.grid_rowconfigure(1, weight=0)
frame_main.grid_columnconfigure(0, weight=1)


frame_image = ctk.CTkFrame(frame_main, fg_color="transparent")
frame_image.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nswe")


label_image = ctk.CTkLabel(frame_image, image=photo, text="")
label_image.grid(row=0, column=0, sticky="nswe")


frame_buttons = ctk.CTkFrame(frame_main, fg_color="transparent")
frame_buttons.grid(row=1, column=0, padx=10, pady=10, sticky="we")
frame_buttons.grid_columnconfigure(0, weight=4)
frame_buttons.grid_columnconfigure(1, weight=1)


image_descrip = ctk.CTkLabel(
    frame_buttons, text=wallpaper.bing_wallpaper_url()[1], text_color="#e9967a", anchor="w")
image_descrip.grid(row=0, column=0, padx=0, sticky="we")

# DOWNLOAD BUTTON
button_download_image = ctk.CTkButton(
    frame_buttons, text="Download", text_color=("#F6F6F6", "#242424"),
    command=wallpaper_download.download_image)
button_download_image.grid(row=0, column=1, padx=0, sticky="e")
button_download_image.configure(
    width=0, fg_color="#e9967a", hover_color="#C68068")

# RUN APP
window.mainloop()

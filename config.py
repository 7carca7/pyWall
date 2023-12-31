"Configuration"

import io
from tkinter.filedialog import asksaveasfilename
import requests
from PIL import Image

API_URL = "https://bing.biturl.top/?resolution=3840&format=json&index=0&mkt=en-US"


class Wallpaper:
    "This class is used to fetch the URL of the Bing's wallpaper of the day"

    def __init__(self):
        self.url = API_URL

    def bing_wallpaper_url(self):
        "Gets the image url and the image cleaned description"

        try:
            response = requests.get(self.url, timeout=20)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            print(f"An error occurred while getting the wallpaper URL: {err}")
            return None, "No URL information received"

        data = response.json()
        image_url = data["url"]
        image_description = data["copyright"]
        cleaned_description = image_description.split(',')[0].split('(')[0]
        return image_url, cleaned_description


class WallpaperDownload(Wallpaper):
    "This class is used to download the Bing's wallpaper of the day"

    def get_response_content(self):
        "This method fetches response content from the URL obtained from the bing_wallpaper_url"

        url_info = self.bing_wallpaper_url()
        if url_info is None or url_info[0] is None:
            print("No URL information received")
            return None

        try:
            response = requests.get(url_info[0], timeout=20)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            print(
                f"An error occurred while getting the response content: {err}")
            return None

        return response.content

    def get_image(self):
        "This method fetches the image from the URL obtained from the bing_wallpaper_url method."

        raw_data = self.get_response_content()
        if raw_data is None:
            # Create and return a transparent image
            return Image.new('RGBA', (500, 500), (0, 0, 0, 0))

        image = Image.open(io.BytesIO(raw_data))
        return image

    def download_image(self):
        "This method downloads the image fetched and saves it to the selected location"

        raw_data = self.get_response_content()
        if raw_data is None:
            return None

        url_info = self.bing_wallpaper_url()
        if url_info is None:
            print("No URL information received")
            return None

        cleaned_description = url_info[1]
        name = cleaned_description + ".jpg"

        saved_file = asksaveasfilename(initialfile=name)
        if saved_file:
            try:
                with open(saved_file, "wb") as file:
                    file.write(raw_data)
            except IOError as err:
                print(f"An error occurred while saving the image: {err}")

import requests
from PIL import Image, ImageTk
import tkinter as tk
from io import BytesIO

ulr = "http://localhost:3000/api/screenshot?session=default"


def main(url):
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))

        tk_image = ImageTk.PhotoImage(image)

        label.config(image=tk_image)
        label.image = tk_image

        root.update()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("WhatsApp HTTP API")
    label = tk.Label(root)
    label.pack()
    ulr = "http://localhost:3000/api/screenshot?session=default"
    while True:
        main(ulr)
        root.after(300)
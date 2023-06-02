import tkinter as tk
from PIL import ImageTk, Image

class builder(tk.Label):
    def __init__(self,parent,img_path):
        super().__init__(parent)

        # Load the image
        image = Image.open(img_path)

        # Resize the image if needed
        # image = image.resize((width, height))

        # Create a PhotoImage from the image
        photo = ImageTk.PhotoImage(image)

        # Set the PhotoImage as the label's image
        self.configure(image=photo)
        self.image = photo  # Store a reference to prevent the image from being garbage collected

        # Adjust the label size to fit the image
        self.configure(width=500, height=500)
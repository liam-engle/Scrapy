import tkinter as tk
from tkinter import filedialog
import requests

class FileRequest(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        # Create the file entry
        self.file_entry = tk.Entry(self)
        self.file_entry.pack()

        # Create the browse button
        browse_button = tk.Button(self, text="Browse", command=self.browse_file)
        browse_button.pack(side="left")

        # Create the submit button
        submit_button = tk.Button(self, text="Submit", command=self.process_file)
        submit_button.pack(side="right")

    def browse_file(self):
        # Open a file dialog to select a file
        file_path = filedialog.askopenfilename()
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(tk.END, file_path)

    def process_file(self):
        file_path = self.file_entry.get()
        try:
            with open(file_path, 'r') as file:
                data_list = file.read().splitlines()
                for data in data_list:
                    response = requests.get(data)
                    print(f"GET request for: {data}")
                    print(f"Response: {response.text}")
        except FileNotFoundError:
            print("File not found.")
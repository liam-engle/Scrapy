import tkinter as tk

class RadioButtonFrame(tk.Frame):
    def __init__(self, parent, options):
        super().__init__(parent)

        self.var = tk.StringVar()

        for key, value in options.items():
            rb = tk.Radiobutton(self, text=key, variable=self.var, value=value)
            rb.pack()
        

    def get_selected_value(self):
        return self.var.get()
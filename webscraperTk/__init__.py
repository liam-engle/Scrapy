import tkinter as tk
import threading
import time
from views import single_target as st
from views import selection
from views import multi_target

# Create the main window
window = tk.Tk()
window.title("Scrapy: Scrape The Net")
# Add a Selection here
radio = selection.RadioButtonFrame(window,{"Single Target":"single","Multi Target":"multi"})
radio.pack()
def display_mode_toggle():
    try:
        if radio.get_selected_value() == "single":
            # Create an instance of the single_target class
            target_frame = st.single_target(window)
            target_frame.pack()
            radio.pack_forget()
            mode_button.pack_forget()
        elif radio.get_selected_value() == "multi":
            target_frame = multi_target.FileRequest(window)
            target_frame.pack()
    except:
        print(f"Error occured while processing selected mode!")
# mode selection toggle button
mode_button = tk.Button(window,text="Next >>",command=display_mode_toggle)
mode_button.pack()
# Run the main loop
window.mainloop()

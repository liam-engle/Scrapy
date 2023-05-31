import tkinter as tk

def submit_form():
    target = target_entry.get()
    interval = int(interval_entry.get())
    print(f"Target: {target}")
    print(f"Interval: {interval}")

# Create the main window
window = tk.Tk()
window.title("Form")

# Create the target entry
target_label = tk.Label(window, text="Target:")
target_label.pack()
target_entry = tk.Entry(window)
target_entry.pack()

# Create the interval entry
interval_label = tk.Label(window, text="Interval:")
interval_label.pack()
interval_entry = tk.Entry(window)
interval_entry.pack()

# Create the submit button
submit_button = tk.Button(window, text="Submit", command=submit_form)
submit_button.pack()

# Run the main loop
window.mainloop()
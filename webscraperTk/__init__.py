import tkinter as tk
import requests, time
def submit_form():
    target = target_entry.get()
    interval = int(interval_entry.get())
    print(f"Target: {target}")
    print(f"Interval: {interval}")

   # Make the GET request every interval milliseconds
    while True:
        response = requests.get(target)
        print(f"Response: {response.text}")
        time.sleep(interval / 1000)  # Convert interval to seconds

# Create the main window
window = tk.Tk()
window.title("Form")

# Create a frame
frame = tk.Frame(window)
frame.pack()

# Create the target entry
target_label = tk.Label(frame, text="Target:")
target_label.pack()
target_entry = tk.Entry(frame)
target_entry.pack()

# Create the interval entry
interval_label = tk.Label(frame, text="Interval:")
interval_label.pack()
interval_entry = tk.Entry(frame)
interval_entry.pack()

# Create the submit button
submit_button = tk.Button(frame, text="Submit", command=submit_form)
submit_button.pack()

# Run the main loop
window.mainloop()
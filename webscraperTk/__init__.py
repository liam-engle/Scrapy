import tkinter as tk
import requests
import threading
import time

def submit_form():
    target = target_entry.get()
    interval = int(interval_entry.get())
    max_requests = int(max_requests_entry.get())
    print(f"Target: {target}")
    print(f"Interval: {interval} milliseconds")
    print(f"Max Requests: {max_requests}")

    # Set a minimum interval of 10 seconds (10,000 milliseconds)
    if interval < 10000:
        interval = 10000
        print("Interval set to minimum value of 10 seconds (10,000 milliseconds)")

    # Start the loop in a separate thread
    thread = threading.Thread(target=loop_request, args=(target, interval, max_requests))
    thread.start()

def loop_request(target, interval, max_requests):
    count = 0
    while count < max_requests:
        response = requests.get(target)
        print(f"Response {count}:\n {response.text}")
        count += 1
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
interval_label = tk.Label(frame, text="Interval (ms):")
interval_label.pack()
interval_entry = tk.Entry(frame)
interval_entry.pack()

# Create the max requests entry
max_requests_label = tk.Label(frame, text="Max Requests:")
max_requests_label.pack()
max_requests_entry = tk.Entry(frame)
max_requests_entry.pack()

# Set default values
interval_entry.insert(tk.END, "10000")
max_requests_entry.insert(tk.END, "10")

# Create the submit button
submit_button = tk.Button(frame, text="Submit", command=submit_form)
submit_button.pack()

# Run the main loop
window.mainloop()

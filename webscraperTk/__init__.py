import tkinter as tk
import requests
import threading
import time

def submit_form():
    target = target_entry.get()
    interval = int(interval_entry.get())
    max_requests = int(max_requests_entry.get())
    identifier = identifier_entry.get()
    print(f"Target: {target}")
    print(f"Interval: {interval} milliseconds")
    print(f"Max Requests: {max_requests}")
    print(f"Identifier: {identifier}")

    # Set a minimum interval of 10 seconds (10,000 milliseconds)
    if interval < 10000:
        interval = 10000
        print("Interval set to minimum value of 10 seconds (10,000 milliseconds)")

    # Start the loop in a separate thread
    thread = threading.Thread(target=loop_request, args=(target, interval, max_requests, identifier))
    thread.start()

def loop_request(target, interval, max_requests, identifier):
    count = 0
    while count < max_requests:
        response = requests.get(target)
        print(f"Response: {response.text}")
        count += 1
        save_response(response.text, identifier, count)
        time.sleep(interval / 1000)  # Convert interval to seconds

    reset_defaults()

def save_response(response, identifier, count):
    file_name = f"./webscraperTk/log/{identifier}_{count}.txt"
    with open(file_name, 'w') as file:
        file.write(response)
    print(f"Response saved as {file_name}")

def reset_defaults():
    interval_entry.delete(0, tk.END)
    max_requests_entry.delete(0, tk.END)
    identifier_entry.delete(0, tk.END)
    interval_entry.insert(tk.END, "10000")
    max_requests_entry.insert(tk.END, "10")
    identifier_entry.insert(tk.END, "")

# Create the main window
window = tk.Tk()
window.title("Scrapy: Scrape The Net")
window.iconbitmap("./webscraperTk/network-tower.ico")
# Create a frame
form = tk.Frame(window)
form.pack(expand=True,side='left')

#Create a second frame
logo_frame = tk.Frame(window)
logo_frame.pack(expand=True,side='top')

# Create the logo label
logo_image = tk.PhotoImage(file="./webscraperTk/logo.png")
logo_label = tk.Label(logo_frame, image=logo_image)
logo_label.pack(expand=True,side='top',fill='both')

# Create the target entry
target_label = tk.Label(form, text="Target:")
target_label.pack()
target_entry = tk.Entry(form)
target_entry.pack()

# Set default value for target_entry
target_entry.insert(tk.END, "http://")

# Create the interval entry
interval_label = tk.Label(form, text="Interval (ms):")
interval_label.pack()
interval_entry = tk.Entry(form)
interval_entry.pack()

# Create the max requests entry
max_requests_label = tk.Label(form, text="Max Requests:")
max_requests_label.pack()
max_requests_entry = tk.Entry(form)
max_requests_entry.pack()

# Create the identifier entry
identifier_label = tk.Label(form, text="Identifier:")
identifier_label.pack()
identifier_entry = tk.Entry(form)
identifier_entry.pack()

# Set default values
interval_entry.insert(tk.END, "10000")
max_requests_entry.insert(tk.END, "10")

# Create the submit button
submit_button = tk.Button(form, text="Submit", command=submit_form)
submit_button.pack()

# Run the main loop
window.mainloop()

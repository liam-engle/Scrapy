import tkinter as tk
import threading
import time
import requests

class single_target(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        # Create the target entry
        target_label = tk.Label(self, text="Target:")
        target_label.pack()
        self.target_entry = tk.Entry(self)
        self.target_entry.pack()

        # Set default value for target_entry
        self.target_entry.insert(tk.END, "http://")

        # Create the interval entry
        interval_label = tk.Label(self, text="Interval (ms):")
        interval_label.pack()
        self.interval_entry = tk.Entry(self)
        self.interval_entry.pack()

        # Create the max requests entry
        max_requests_label = tk.Label(self, text="Max Requests:")
        max_requests_label.pack()
        self.max_requests_entry = tk.Entry(self)
        self.max_requests_entry.pack()

        # Create the identifier entry
        identifier_label = tk.Label(self, text="Identifier:")
        identifier_label.pack()
        self.identifier_entry = tk.Entry(self)
        self.identifier_entry.pack()

        # Set default values
        self.interval_entry.insert(tk.END, "10000")
        self.max_requests_entry.insert(tk.END, "10")

        # Create the submit button
        submit_button = tk.Button(self, text="Submit", command=self.submit_form)
        submit_button.pack()
        
    def submit_form(self):
        target = self.target_entry.get()
        interval = int(self.interval_entry.get())
        max_requests = int(self.max_requests_entry.get())
        identifier = self.identifier_entry.get()
        print(f"Target: {target}")
        print(f"Interval: {interval} milliseconds")
        print(f"Max Requests: {max_requests}")
        print(f"Identifier: {identifier}")

        # Set a minimum interval of 10 seconds (10,000 milliseconds)
        if interval < 10000:
            interval = 10000
            print("Interval set to minimum value of 10 seconds (10,000 milliseconds)")

        # Start the loop in a separate thread
        thread = threading.Thread(target=self.loop_request, args=(target, interval, max_requests, identifier))
        thread.start()


    def save_response(self, response, identifier, count):
        file_name = f"./webscraperTk/log/{identifier}_{count}.txt"
        with open(file_name, 'w') as file:
            file.write(response)
        print(f"Response saved as {file_name}")

    def reset_defaults(self):
        self.interval_entry.delete(0, tk.END)
        self.max_requests_entry.delete(0, tk.END)
        self.identifier_entry.delete(0, tk.END)
        self.interval_entry.insert(tk.END, "10000")
        self.max_requests_entry.insert(tk.END, "10")
        self.identifier_entry.insert(tk.END, "")

    def loop_request(self, target, interval, max_requests, identifier):
        count = 0
        while count < max_requests:
            response = requests.get(target)
            print(f"Response: {response.text}")
            count += 1
            self.save_response(response.text, identifier, count)
            time.sleep(interval / 1000)  # Convert interval to seconds

        self.reset_defaults()
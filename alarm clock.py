import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import threading
import time

class AlarmClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock App")

        self.label = tk.Label(root, text="Set Alarm Time (HH:MM:SS):")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.set_button = tk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.set_button.pack(pady=10)

    def set_alarm(self):
        alarm_time_str = self.entry.get()
        try:
            alarm_time = datetime.strptime(alarm_time_str, "%H:%M:%S").time()
        except ValueError:
            messagebox.showerror("Error", "Invalid time format. Please use HH:MM:SS.")
            return

        current_time = datetime.now().time()
        alarm_datetime = datetime.combine(datetime.today(), alarm_time)

        if alarm_datetime <= datetime.now():
            messagebox.showerror("Error", "Invalid time. Please set a future time.")
            return

        time_diff_seconds = (alarm_datetime - datetime.combine(datetime.today(), current_time)).total_seconds()

        # Start a separate thread for waiting to avoid freezing the GUI
        threading.Thread(target=self.wait_and_alert, args=(time_diff_seconds,)).start()

    def wait_and_alert(self, seconds):
        time.sleep(seconds)
        self.show_alarm_alert()

    def show_alarm_alert(self):
        messagebox.showinfo("Alarm", "Time to wake up!")

if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClockApp(root)
    root.mainloop()
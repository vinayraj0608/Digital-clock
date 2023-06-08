import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

window = tk.Tk()
window.title("Digital Clock")
window.geometry("600x100")

time_label = tk.Label(window, font=("Arial", 30), bg = "cyan", fg="black")
time_label.pack(pady=20)

update_time()
window.mainloop()


import tkinter as tk
from tkinter import messagebox
from core import adaptive_download
import threading

def run_download():
    url = url_entry.get()
    out = out_entry.get()
    crisis = crisis_var.get()

    if not url or not out:
        messagebox.showerror("Error", "Please fill all fields")
        return

    delay = 1.5 if crisis else 0.3

    def task():
        try:
            adaptive_download(url, out, delay=delay)
            messagebox.showinfo("Done", "Download finished successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    threading.Thread(target=task).start()

root = tk.Tk()
root.title("CrisisNet Downloader")
root.geometry("420x260")
root.resizable(False, False)

tk.Label(root, text="URL:").pack(pady=(15, 0))
url_entry = tk.Entry(root, width=55)
url_entry.pack()

tk.Label(root, text="Output file path:").pack(pady=(10, 0))
out_entry = tk.Entry(root, width=55)
out_entry.pack()

crisis_var = tk.BooleanVar()
tk.Checkbutton(root, text="Crisis mode (slow & safe)", variable=crisis_var).pack(pady=10)

tk.Button(root, text="Start Download", command=run_download, height=2).pack(pady=15)

root.mainloop()

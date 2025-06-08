import tkinter as tk

window = tk.Tk()
window.title("My Journal")
window.geometry("400x300")

entry_box = tk.Text(window, height=10, width=40)
entry_box.pack(pady=20)

window.mainloop()
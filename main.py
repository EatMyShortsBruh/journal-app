import tkinter as tk
from journal import save_to_file, read_from_file  

# main window 
window = tk.Tk()
window.title("My Journal")
window.geometry("400x550")

# journal entry box
entry_box = tk.Text(window, height=15, width=40)
entry_box.pack(pady=10)

# saved entry output
output_box = tk.Text(window, height=5, width=40)
output_box.pack(pady=10)

def save_entry():
    content = entry_box.get("1.0", tk.END).strip()
    save_to_file(content)
    entry_box.delete("1.0", tk.END)  

def view_entries():
    contents = read_from_file()
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, contents)



save_button = tk.Button(window, text="Save Entry", command=save_entry)
save_button.pack(pady=10)

view_button = tk.Button(window, text="View Entries", command=view_entries)
view_button.pack(pady=5)  

window.mainloop()
import tkinter as tk

window = tk.Tk()
window.title("My Journal")
window.geometry("400x300")

entry_box = tk.Text(window, height=10, width=40)
entry_box.pack(pady=20)

def save_entry():
    content = entry_box.get("1.0", tk.END).strip() #Get all text
    if content:
        with open("journal.txt", "a") as f:        # append to file
            f.write(content + "\n\n")
        entry_box.delete("1.0", tk.END)            # clear the box

save_button = tk.Button(window, text="Save Entry", command=save_entry)
save_button.pack(pady=10)

window.mainloop()
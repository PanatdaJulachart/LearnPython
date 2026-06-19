import tkinter as tk
from tkinter import messagebox
import datetime

def save_diary() :
    content = text_box.get("1.0", "end-1c")
    if content == "" :
        messagebox.showwarning("Warning", "Please type something before saving!")
        return
    
    now = datetime.datetime.now()
    time_str = now.strftime("%d%m%y %H:%M")

    with open("diary.txt", "a", encoding="UTF-8") as file:
        file.write(f"[{time_str}]\n{content}\n")
        file.write("-" * 40 + "\n")

        text_box.delete("1.0", tk.END)

        messagebox.showinfo("Success", "Save to your digital diary 📖 ")

root = tk.Tk()
root.title("My Digital Diary")
root.geometry("400x500")
        
tital_label = tk.Label(root, text="My memory", font=("Promt", 18, "bold"))
tital_label.pack(pady=10)

text_box = tk.Text(root, height=10, width=40, font=("promt", 14))
text_box.pack(pady=10)

save_button = tk.Button(root, text="Save!", font=("promt",16) , command=save_diary)
save_button.pack(pady=10)
root.mainloop()

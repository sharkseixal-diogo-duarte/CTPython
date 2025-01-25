import tkinter as tk
from tkinter import Text, filedialog

root = tk.Tk()
root.title("OCR")
root.geometry("400x600")

button_coverter=tk.Button(root, font="Arial", text="Converter", bg="blue")
button_coverter.pack(pady=10)

texto = Text(root, wrap=tk.WORD, font=("Arial",12))
texto.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
root.mainloop()

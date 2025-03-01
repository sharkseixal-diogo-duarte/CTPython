import tkinter
from tkinter import filedialog
import cv2

def select_files():
    files = filedialog.askopenfilenames(filetypes=[("Image", "*.jpg")])
    for file in files:
        file_listbox.insert(tkinter.END, file)

root = tkinter.Tk()
root.title("editor de imagem")
root.geometry("600x400")
Button1=tkinter.Button(root,text="Open image", command =select_files)
Button1.pack(pady=10)
Button2=tkinter.Button(root,text="Grayscale",command = cv2.imread("assets/image.jpg", 0))
Button2.pack(pady=10)
Button_direita=tkinter.Button(root,text="<", command= "cv2.ROTATE_90_CLOCKWISE")
Button_direita.pack(pady=10)
Button_esquerda=tkinter.Button(root,text=">", command= "cv2.ROTATE_240_CLOCKWISE")
Button_esquerda.pack(pady=10)
file_listbox = tkinter.Listbox(root, width=80, height=10)
file_listbox.pack(pady=10)

root.mainloop()


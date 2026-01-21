import tkinter
import time

def atualizar():
    hora = time.strftime("%H:%M:%S")
    texto.config(text=hora)
    janela.after(1000, atualizar)

janela = tkinter.Tk()
janela.title("Relogio")
janela.geometry("200x100")
janela.configure(background="black")

texto= tkinter.Label(janela, font=("Arial", 25),bg="black", fg="white", text="Relogio")
texto.pack(anchor="center")

atualizar()
janela.mainloop()
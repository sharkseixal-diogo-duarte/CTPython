import tkinter as tk
from shutil import posix
from tkinter import messagebox
import os

def criar_pasta_arquivo():
    nome_pasta = entry_pasta.get()
    nome_arquivo = entry_arquivo.get()

    if not nome_pasta or not nome_arquivo:
        messagebox.showwarning("Aviso", "Por favor, preencha ambos os campos.")
        return

    if not os.path.exists(nome_pasta):
        os.makedirs(nome_pasta)

    caminho_arquivo = os.path.join(nome_pasta, nome_arquivo)

    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.write("Conteúdo do arquivo")

    messagebox.showinfo("Sucesso", f"Pasta e arquivo criados com sucesso:\n{caminho_arquivo}")

root = tk.Tk()
root.title("Criar Pasta e Arquivo")
root.geometry("900x400")
label_pasta = tk.Label(root, text="Nome da Pasta:",font="Arial,20")
label_pasta.pack(pady=5)
entry_pasta = tk.Entry(root, width=60)
entry_pasta.pack(pady=5)
label_arquivo = tk.Label(root, text="Nome do Ficheiro:",font="Arial,20")
label_arquivo.pack(pady=5)
entry_arquivo = tk.Entry(root, width=60)
entry_arquivo.pack(pady=5)
botao_criar = tk.Button(root,font="Arial", text="Criar Pasta e Ficheiro", command=criar_pasta_arquivo, bg="green")
botao_criar.pack(pady=20)
botao_criar = tk.Button(root,font="Arial", text="exit",width=10, command=lambda:root.quit())
botao_criar.pack(pady=20)
root.mainloop()

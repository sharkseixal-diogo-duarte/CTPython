import os
from tkinter import Tk, filedialog, Button, Label, Listbox, END
from pdf2image import convert_from_path
from pytesseract import image_to_string
from docx import Document
from tkinter import messagebox
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\CTPAI - DIOGO DUARTE\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def convert_pdf_to_word(pdf_paths, output_dir):
    for pdf_path in pdf_paths:
        try:

            images = convert_from_path(pdf_path)


            doc = Document()

            for i, image in enumerate(images):

                text = image_to_string(image, lang="por")  # Define o idioma para português


                doc.add_paragraph(text)


            pdf_name = os.path.basename(pdf_path)
            word_name = os.path.splitext(pdf_name)[0] + ".docx"
            output_path = os.path.join(output_dir, word_name)
            doc.save(output_path)

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao processar {pdf_path}: {e}")

    messagebox.showinfo("Concluído", f"Conversão concluída! Arquivos salvos em {output_dir}")


def select_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    for file_path in file_paths:
        file_listbox.insert(END, file_path)


def select_output_dir():
    directory = filedialog.askdirectory()
    if directory:
        output_dir_label.config(text=directory)


def start_conversion():
    pdf_paths = file_listbox.get(0, END)
    output_dir = output_dir_label.cget("text")

    if not pdf_paths:
        messagebox.showwarning("Aviso", "Por favor, selecione pelo menos um arquivo PDF.")
        return

    if not output_dir or output_dir == "Selecione a pasta de saída":
        messagebox.showwarning("Aviso", "Por favor, selecione uma pasta de saída.")
        return

    convert_pdf_to_word(pdf_paths, output_dir)

root = Tk()
root.title("PDF para Word (OCR)")
root.geometry("600x400")

Button(root, text="Selecionar PDFs", command=select_files).pack(pady=10)

file_listbox = Listbox(root, width=80, height=10)
file_listbox.pack(pady=10)

Button(root, text="Selecionar Pasta de Saída", command=select_output_dir).pack(pady=10)

output_dir_label = Label(root, text="Selecione a pasta de saída", fg="gray")
output_dir_label.pack(pady=5)

Button(root, text="Iniciar Conversão", command=start_conversion, bg="green", fg="white").pack(pady=20)

root.mainloop()

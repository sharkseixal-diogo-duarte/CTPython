import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
import pytesseract
from PyPDF2 import PdfReader
from PIL import Image

def convert_pdf_to_txt(pdf_files):
    for pdf_path in pdf_files:
        try:
            # Extract file name without extension
            file_name = os.path.splitext(os.path.basename(pdf_path))[0]
            output_txt = f"{file_name}.txt"

            # Open output file for writing
            with open(output_txt, "w", encoding="utf-8") as txt_file:
                reader = PdfReader(pdf_path)
                for page_number, page in enumerate(reader.pages):
                    # Extract text directly from the page
                    text = page.extract_text()

                    if text:
                        # Write the extracted text to the file
                        txt_file.write(f"Page {page_number + 1}:\n{text}\n\n")
                    else:
                        # If no text is found, use OCR (Tesseract)
                        messagebox.showinfo("OCR Necessário", f"Texto não encontrado na página {page_number + 1}. Usando OCR...")
                        images = page.images
                        for image_name, img_data in images.items():
                            image = Image.open(img_data)
                            ocr_text = pytesseract.image_to_string(image)
                            txt_file.write(f"OCR Text from {image_name}:\n{ocr_text}\n\n")

            messagebox.showinfo("Sucesso", f"Ficheiro convertido: {output_txt}")

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao processar {pdf_path}:\n{e}")

def select_pdfs():
    pdf_files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])

    if not pdf_files:
        messagebox.showwarning("Aviso", "Nenhum ficheiro selecionado.")
        return

    # Create and start a thread to avoid freezing the GUI
    thread = threading.Thread(target=convert_pdf_to_txt, args=(pdf_files,))
    thread.start()

# Create the GUI
root = tk.Tk()
root.title("Conversor OCR PDF → TXT")
root.geometry("400x200")

# Button to select PDF files
btn_select = tk.Button(root, text="Selecionar PDFs", command=select_pdfs, font=("Arial", 12))
btn_select.pack(pady=20)

# Informational label
label_info = tk.Label(root, text="Selecione ficheiros PDF para converter para TXT", font=("Arial", 10))
label_info.pack()

# Run the application
root.mainloop()

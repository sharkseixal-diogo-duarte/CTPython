import sys
import json
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
)

contactos = []
ficheiro_json = "contactos.json"

def carregar_contactos():
    try:
        with open(ficheiro_json, "r", encoding="utf-8") as file:
            contactos.extend(json.load(file))
    except FileNotFoundError:
        pass

def save_contactos():
        with open(ficheiro_json, "w", encoding="utf-8") as file:
            json.dump(contactos, file, indent=4, ensure_ascii=False)

def atualizar_tabela():
    tabela.setRowCount(len(contactos))
    for i , c in enumerate(contactos):
        tabela.setItem(i,0,QTableWidgetItem(c["nome"]))
        tabela.setItem(i,1,QTableWidgetItem(c["telefone"]))
        tabela.setItem(i,2,QTableWidgetItem(c["email"]))


def add_contact():
    nome = input_nome.text().strip()
    tel = input_telefone.text().strip()
    email = input_email.text().strip()

    if nome:
        contactos.append({"nome":nome,"telefone":tel,"email":email})
        atualizar_tabela()
        save_contactos()
        input_nome.clear()
        input_telefone.clear()
        input_email.clear()

def edit_contacto():
    line = tabela.currentRow()
    if line >=0:
        contactos[line] = {
            "nome": input_nome.text().strip(),
            "telefone": input_telefone.text().strip(),
            "email": input_email.text().strip()
        }
        atualizar_tabela()
        save_contactos()
        input_nome.clear()
        input_telefone.clear()
        input_email.clear()

def remove_contact():
    line = tabela.currentRow()
    if line >= 0:
        del contactos[line]
        atualizar_tabela()
        save_contactos()

def fill_input():
    line = tabela.currentRow()
    if line >=0:
        input_nome.setText(contactos[line]["nome"])
        input_telefone.setText(contactos[line]["telefone"])
        input_email.setText(contactos[line]["email"])


app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Contact Manage")
window.setGeometry(300,300,600,400)

central = QWidget()
layout = QVBoxLayout()

tabela = QTableWidget()
tabela.setColumnCount(3)
tabela.setHorizontalHeaderLabels(["nome", "telefone","email"])
tabela.cellClicked.connect(fill_input)
layout.addWidget(tabela)

input_nome = QLineEdit()
input_telefone = QLineEdit()
input_email = QLineEdit()
inputs_layout = QHBoxLayout()
inputs_layout.addWidget(input_nome)
inputs_layout.addWidget(input_telefone)
inputs_layout.addWidget(input_email)

layout.addLayout(inputs_layout)

butao_add = QPushButton("Adicionar")
butao_edit = QPushButton("Editar")
butao_rm = QPushButton("Remover")

butao_add.clicked.connect(add_contact)
butao_edit.clicked.connect(edit_contacto)
butao_rm.clicked.connect(remove_contact)

butao_layout = QHBoxLayout()
butao_layout.addWidget(butao_add)
butao_layout.addWidget(butao_edit)
butao_layout.addWidget(butao_rm)

layout.addLayout(butao_layout)

central.setLayout(layout)
window.setCentralWidget(central)

carregar_contactos()
atualizar_tabela()

window.show()
sys.exit(app.exec_())
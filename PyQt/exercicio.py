import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout

app = QApplication(sys.argv)

janela = QWidget()
janela.setWindowTitle("Saudação")
janela.setGeometry(800, 400, 400, 400)

entrada = QLineEdit()
botao = QPushButton("Saudar")
label = QLabel("")

def saudar():
    label.setText("Olá, " + entrada.text())

botao.clicked.connect(saudar)

layout = QVBoxLayout()
layout.addWidget(QLineEdit())
layout.addWidget(QPushButton("Saudar"))
layout.addWidget(QLabel(""))
janela.setLayout(layout)

janela.show()
sys.exit(app.exec())



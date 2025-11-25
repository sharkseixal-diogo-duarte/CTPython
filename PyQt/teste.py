from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QHBoxLayout
import sys
app = QApplication(sys.argv)
window = QWidget()

layout = QHBoxLayout()
layout.addWidget(QPushButton("botão 1"))
layout.addWidget(QPushButton("botão 2"))

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
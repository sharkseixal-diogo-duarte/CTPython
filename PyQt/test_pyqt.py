import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("PyQt TEST")
window.setGeometry(300, 300, 400, 400)

label = QLabel("<h1> Welcome to PyQt</h1>", parent=window)
label.move(100, 100)

window.show()
sys.exit(app.exec_())
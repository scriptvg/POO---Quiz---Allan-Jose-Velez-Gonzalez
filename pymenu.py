import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QMessageBox, QInputDialog
from game import Juego

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menú Principal")
        self.setGeometry(100, 100, 400, 300)

        self.nombre = None
        self.juego = None

        # Crear el layout principal
        layout = QVBoxLayout()

        # Etiqueta de bienvenida
        self.label = QLabel("Ingresa tu nombre para comenzar:")
        layout.addWidget(self.label)

        # Botones para las opciones del menú
        self.btn_iniciar_juego = QPushButton("Iniciar Juego")
        self.btn_iniciar_juego.clicked.connect(self.iniciar_juego)
        layout.addWidget(self.btn_iniciar_juego)

        self.btn_cifrado_cesar = QPushButton("Cifrado César")
        self.btn_cifrado_cesar.clicked.connect(self.cifrar_texto)
        layout.addWidget(self.btn_cifrado_cesar)

        self.btn_descifrado_cesar = QPushButton("Descifrado César")
        self.btn_descifrado_cesar.clicked.connect(self.descifrar_texto)
        layout.addWidget(self.btn_descifrado_cesar)

        self.btn_ordenamiento_burbuja = QPushButton("Ordenamiento Burbuja")
        self.btn_ordenamiento_burbuja.clicked.connect(self.ordenar_burbuja)
        layout.addWidget(self.btn_ordenamiento_burbuja)

        self.btn_salir = QPushButton("Salir")
        self.btn_salir.clicked.connect(self.salir)
        layout.addWidget(self.btn_salir)

        # Configurar el widget central
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def iniciar_juego(self):
        if not self.validar_nombre():
            return
        self.juego = Juego(self.nombre)
        self.juego.iniciar_juego()
        QMessageBox.information(self, "Iniciar Juego", "¡El juego ha comenzado!")

    def cifrar_texto(self):
        if not self.validar_nombre():
            return
        self.juego.cifrar_texto()
        QMessageBox.information(self, "Cifrado César", "Texto cifrado correctamente.")

    def descifrar_texto(self):
        if not self.validar_nombre():
            return
        self.juego.descifrar_texto()
        QMessageBox.information(self, "Descifrado César", "Texto descifrado correctamente.")

    def ordenar_burbuja(self):
        if not self.validar_nombre():
            return
        self.juego.ordenar_burbuja()
        QMessageBox.information(self, "Ordenamiento Burbuja", "Ordenamiento completado.")

    def salir(self):
        self.close()

    def validar_nombre(self):
        if not self.nombre:
            self.nombre, ok = QInputDialog.getText(self, "Nombre", "Por favor, ingresa tu nombre:")
            if not ok or not self.nombre.strip():
                QMessageBox.warning(self, "Error", "Debes ingresar un nombre válido.")
                return False
        return True

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
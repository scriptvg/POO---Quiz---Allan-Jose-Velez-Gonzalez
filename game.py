class Juego:
    def __init__(self, nombre):
        self.nombre = nombre
        self.texto = ""

    def iniciar_juego(self):
        # Lógica para iniciar el juego
        print(f"¡Bienvenido, {self.nombre}! El juego ha comenzado.")

    def cifrar_texto(self):
        # Ejemplo de cifrado César
        if not self.texto:
            self.texto = input("Ingresa el texto a cifrar: ")
        desplazamiento = 3
        texto_cifrado = "".join(
            chr((ord(char) - 65 + desplazamiento) % 26 + 65) if char.isupper() else
            chr((ord(char) - 97 + desplazamiento) % 26 + 97) if char.islower() else char
            for char in self.texto
        )
        self.texto = texto_cifrado
        print(f"Texto cifrado: {self.texto}")

    def descifrar_texto(self):
        # Ejemplo de descifrado César
        if not self.texto:
            print("No hay texto para descifrar.")
            return
        desplazamiento = 3
        texto_descifrado = "".join(
            chr((ord(char) - 65 - desplazamiento) % 26 + 65) if char.isupper() else
            chr((ord(char) - 97 - desplazamiento) % 26 + 97) if char.islower() else char
            for char in self.texto
        )
        self.texto = texto_descifrado
        print(f"Texto descifrado: {self.texto}")

    def ordenar_burbuja(self):
        # Ejemplo de ordenamiento burbuja
        if not self.texto:
            self.texto = input("Ingresa una lista de números separados por comas: ")
        try:
            numeros = list(map(int, self.texto.split(",")))
            for i in range(len(numeros)):
                for j in range(0, len(numeros) - i - 1):
                    if numeros[j] > numeros[j + 1]:
                        numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
            self.texto = ",".join(map(str, numeros))
            print(f"Números ordenados: {self.texto}")
        except ValueError:
            print("Por favor, ingresa una lista válida de números separados por comas.")
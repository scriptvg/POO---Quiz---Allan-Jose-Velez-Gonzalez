class Juego:
    def __init__(self, nombre_jugador):
        self.nombre_jugador = nombre_jugador
        self.jugando = False
        self.desplazamiento_cifrado = None

    def iniciar_juego(self):
        self.jugando = True
        print(f"\n¡Bienvenido al juego, {self.nombre_jugador}!")
        print("El juego ha comenzado..")
        self.cifrar_texto()
        self.ordenar_burbuja()
        print("¡Gracias por jugar!\n")
        
    def cifrar_texto(self):
        texto = input("Introduce el texto a cifrar: ")
        try:
            desplazamiento = int(input("Ingresa un número de desplazamiento (número entero): "))
            self.desplazamiento_cifrado = desplazamiento
        except ValueError:
            print("El número debe ser un número entero. Inténtalo de nuevo.")
            return
        
        texto_cifrado = self._cifrado_cesar(texto, desplazamiento)
        print(f"Texto cifrado: {texto_cifrado}\n")
        
    def _cifrado_cesar(self, texto, desplazamiento):
        resultado = ""
        for letra in texto:
            if letra.isalpha():
                base = ord('A') if letra.isupper() else ord('a')
                nueva_letra = chr((ord(letra) - base + desplazamiento) % 26 + base)
                resultado += nueva_letra
            else:
                resultado += letra
        return resultado
    
    def descifrar_texto(self):
        if self.desplazamiento_cifrado is None:
            print("No se ha cifrado ningún texto aún. Por favor, cifra un texto primero.\n")
            return
        
        texto = input("Introduce el texto a descifrar: ")
        desplazamiento = self.desplazamiento_cifrado
        texto_descifrado = self._descifrado_cesar(texto, desplazamiento)
        print(f"Texto descifrado: {texto_descifrado}\n")
    
    def _descifrado_cesar(self, texto, desplazamiento):
        resultado = ""
        for letra in texto:
            if letra.isalpha():
                base = ord('A') if letra.isupper() else ord('a')
                nueva_letra = chr((ord(letra) - base - desplazamiento) % 26 + base)
                resultado += nueva_letra
            else:
                resultado += letra
        return resultado
    
    def ordenar_burbuja(self):
        lista = [int(x) for x in input("Introduce una lista de números separados por espacios: ").split()]
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        print(f"Lista ordenada: {lista}\n")

    def salir(self):
        print(f"\nHasta luego, {self.nombre_jugador}. ¡Vuelve pronto!")

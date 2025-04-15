class Juego:
    def __init__(self, nombre_jugador):
      
        self.nombre_jugador = nombre_jugador
        self.jugando = False

    def iniciar_juego(self):
        self.jugando = True
        print(f"\n¡Bienvenido al juego, {self.nombre_jugador}!")
        print("El juego ha comenzado..")
        self.cifrar_texto()
        print("¡Gracias por jugar!\n")
        
    def cifrar_texto(self):
        texto = input("Introduce el texto a cifrar: ")
        try:
            desplazamiento = int(input("Ingresa un número de desplazamiento (numero entero): "))
        except ValueError:
            print("El numero debe ser un numero entero. Intentalo de nuevo.")
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

    def salir(self):
        print(f"\nHasta luego, {self.nombre_jugador}. ¡Vuelve pronto!")


  
    



class Juego:
    def __init__(self, nombre_jugador):
        # Constructor de la clase Juego. Inicializa el nombre del jugador y el estado del juego.
        self.nombre_jugador = nombre_jugador
        self.jugando = False

    def iniciar_juego(self):
        # Método para iniciar el juego. Cambia el estado a "jugando" y da la bienvenida al jugador.
        self.jugando = True
        print(f"\n¡Bienvenido al juego, {self.nombre_jugador}!")
        print("El juego ha comenzado..")
        self.cifrar_texto()  # Llama al método para cifrar texto como parte del flujo del juego.
        print("¡Gracias por jugar!\n")
        
    def cifrar_texto(self):
        # Método para solicitar un texto y un desplazamiento, y cifrarlo usando el cifrado César.
        texto = input("Introduce el texto a cifrar: ")
        try:
            desplazamiento = int(input("Ingresa un número de desplazamiento (numero entero): "))
        except ValueError:
            # Manejo de errores si el usuario no ingresa un número entero.
            print("El numero debe ser un numero entero. Intentalo de nuevo.")
            return
        
        texto_cifrado = self._cifrado_cesar(texto, desplazamiento)  # Llama al método privado para cifrar.
        print(f"Texto cifrado: {texto_cifrado}\n")
        
    def _cifrado_cesar(self, texto, desplazamiento):
        # Método que implementa el algoritmo de cifrado César.
        resultado = ""
        
        # Diccionario de sustitucion
        sustitucion = {
            'a' : '4', 'e' : '3', 'i' : '1', 'o' : '0', 's' : '5',
        }
        
        for letra in texto:
            if letra.isalpha():  # Verifica si el carácter es una letra.
                base = ord('A') if letra.isupper() else ord('a')  # Determina la base según mayúsculas/minúsculas.
                nueva_letra = chr((ord(letra) - base + desplazamiento) % 26 + base)  # Aplica el desplazamiento.
                """ resultado += nueva_letra """
                resultado += sustitucion.get(nueva_letra, nueva_letra)  # Reemplaza la letra si está en el diccionario.
            else:
                resultado += letra  # Si no es letra, lo agrega sin cambios.
        return resultado
    
    def ordenar_burbuja(self):
        # Método para ordenar una lista de números usando el algoritmo de burbuja.
        lista = [int(x) for x in input("Introduce una lista de números separados por espacios: ").split()]
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]:  # Intercambia si el elemento actual es mayor que el siguiente.
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        print(f"Lista ordenada: {lista}\n")

    def salir(self):
        # Método para finalizar el juego y despedirse del jugador.
        print(f"\nHasta luego, {self.nombre_jugador}. ¡Vuelve pronto!")

from Juego import Juego

def mostrar_menu():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Iniciar juego")
    print("2. Cifrado César")
    print("3. Descifrado César")
    print("4. Ordenamiento Burbuja")
    print("5. Salir")
    print("======================")

def main():
    
    nombre = input("Ingresa tu nombre para comenzar: ")
    juego = Juego(nombre)
    valor = True
    
    while valor:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            juego.iniciar_juego()
        elif opcion == "2":
            juego.cifrar_texto()
        elif opcion == "3":
            juego.descifrar_texto()
        elif opcion == "4":
            juego.ordenar_burbuja()
        elif opcion == "5":
            juego.salir()
            valor=False
        else:
            print("Opción inválida. Intenta de nuevo.\n")

if __name__ == "__main__":
    main()

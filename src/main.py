import utilidades, menu, juego


def main():
    seleccion: int = 0

    while seleccion != 2:
        utilidades.limpiar_consola()
        menu.mostrar_menu()

        seleccion = utilidades.pedir_entero("> ", 1, 2)

        # Opción: jugar
        if seleccion == "1":
            juego.jugar()


if __name__ == "__main__":
    main()
import utilidades, menu, juego


def main():
    seleccion: int = 0

    while seleccion != 2:
        menu.mostrar_menu()

        seleccion = utilidades.pedir_entero("> ", 1, 2)

        # Opción: jugar
        if seleccion == 1:
            cartas_crupier, cartas_jugador, resultado = juego.jugar()

            juego.acabar_partida(cartas_crupier, cartas_jugador, resultado)


if __name__ == "__main__":
    main()
import cartas, utilidades


def mostrar_menu():
    """ Muestra el menú principal """
    utilidades.limpiar_consola()

    print("=== BLACKJACK ===\n")

    print("1. Jugar")
    print("2. Salir")


def mostrar_partida(cartas_crupier: list[cartas.Carta], cartas_jugador: list[cartas.Carta], crupier_ocultar: bool = True):
    """
    Muestra el estado actual de la partida.

    Args:
        cartas_crupier: El mazo del crupier.
        cartas_jugador: El mazo del jugador.
        crupier_visibles: Si todas las cartas del crupier son visibles.
    """
    utilidades.limpiar_consola()
    
    print("=== BLACKJACK: JUGANDO ===\n")

    cadena_crupier: str = f"Cartas crupier: {cartas.visualizar_mazo(cartas_crupier, crupier_ocultar)}"
    cadena_jugador: str = f"Cartas jugador: {cartas.visualizar_mazo(cartas_jugador)}"

    puntuacion_crupier: int = cartas.obtener_suma(cartas_crupier)
    puntuacion_jugador: int = cartas.obtener_suma(cartas_jugador)

    print(cadena_crupier)
    if crupier_ocultar:
        print(f"Puntuación: {cartas.obtener_puntos(cartas_crupier[0])} + ???")
    else:
        print(f"Puntuación: {puntuacion_crupier}")

    print("")

    print(cadena_jugador)
    print(f"Puntuación: {puntuacion_jugador}")


def mostrar_acciones():
    """ Muestra todas las acciones disponibles durante la partida. """

    print("\n1. Pedir")
    print("2. Plantarse")
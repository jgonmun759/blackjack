import cartas, utilidades


def mostrar_menu():
    """ Muestra el menú principal """
    utilidades.limpiar_consola()

    print("=== BLACKJACK ===\n")

    print("1. Jugar")
    print("2. Salir")


def mostrar_partida(cartas_cupier: list[cartas.Carta], cartas_jugador: list[cartas.Carta], cupier_ocultar: bool = True):
    """
    Muestra el estado actual de la partida.

    Args:
        cartas_cupier: El mazo del cupier.
        cartas_jugador: El mazo del jugador.
        cupier_visibles: Si todas las cartas del cupier son visibles.
    """
    utilidades.limpiar_consola()
    
    print("=== BLACKJACK: JUGANDO ===\n")

    cadena_cupier: str = f"Cartas cupier: {cartas.visualizar_mazo(cartas_cupier, cupier_ocultar)}"
    cadena_jugador: str = f"Cartas jugador: {cartas.visualizar_mazo(cartas_jugador)}"

    puntuacion_cupier: int = cartas.obtener_suma(cartas_cupier)
    puntuacion_jugador: int = cartas.obtener_suma(cartas_jugador)

    print(cadena_cupier)
    if cupier_ocultar:
        print(f"Puntuación: {cartas.obtener_puntos(cartas_cupier[0])} + ???")
    else:
        print(f"Puntuación: {puntuacion_cupier}")

    print("")

    print(cadena_jugador)
    print(f"Puntuación: {puntuacion_jugador}")


def mostrar_acciones():
    """ Muestra todas las acciones disponibles durante la partida. """

    print("1. Pedir")
    print("2. Plantarse")
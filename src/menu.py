import cartas


def mostrar_menu():
    """ Muestra el menú principal """

    print("=== BLACKJACK ===\n")

    print("1. Jugar")
    print("2. Salir")


def mostrar_partida(cartas_cupier: list[cartas.Carta], cartas_jugador: list[cartas.Carta], cupier_ocultar: bool):
    """
    Muestra el estado actual de la partida.

    Args:
        cartas_cupier: El mazo del cupier.
        cartas_jugador: El mazo del jugador.
        cupier_visibles: Si todas las cartas del cupier son visibles.
    """
    print("=== BLACKJACK: JUGANDO ===\n")

    cadena_cupier: str = "Cartas cupier:", cartas.visualizar_mazo(cartas_cupier, cupier_ocultar)
    cadena_jugador: str = "Cartas jugador:", cartas.visualizar_mazo(cartas_jugador)
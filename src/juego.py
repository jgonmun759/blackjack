import cartas, menu, utilidades

def puede_pedir(puntos: int) -> bool:
    """ Comprueba si puede pedir o no """
    return puntos < 21


def jugar() -> tuple[list[cartas.Carta], list[cartas.Carta], str]:
    """
    Comienza el juego hasta terminar la partida.

    Returns:
        cartas: Las cartas del jugador y las del crupier al finalizar.
        str: Si empata, pierde o gana.
    """
    mazo: cartas.Baraja = cartas.obtener_baraja()

    cartas_crupier: list[cartas.Carta] = [cartas.siguiente_carta(mazo) for _ in range(2)]
    cartas_jugador: list[cartas.Carta] = [cartas.siguiente_carta(mazo) for _ in range(2)]

    puntos_crupier: int = cartas.obtener_suma(cartas_crupier)
    puntos_jugador: int = cartas.obtener_suma(cartas_jugador)
    
    eleccion: int = 0
    while puede_pedir(puntos_jugador) and eleccion != 2:
        menu.mostrar_partida(cartas_crupier, cartas_jugador)

        # Blackjack natural
        if (puntos_jugador == 21):
            return cartas_crupier, cartas_jugador, ("empata" if (puntos_crupier == puntos_jugador) else "gana")
        elif puntos_crupier == 21:
            return cartas_crupier, cartas_jugador, "pierde"

        menu.mostrar_acciones()

        eleccion = utilidades.pedir_entero("> ", 1, 2)

        if eleccion == 1:
            cartas_jugador.append(cartas.siguiente_carta(mazo))
            puntos_jugador = cartas.obtener_suma(cartas_jugador)

    if puntos_jugador > 21:
        return cartas_crupier, cartas_jugador, "pierde"

    menu.mostrar_partida(cartas_crupier, cartas_jugador, False)
    input("\n- Cartas del crupier visibles\n<ENTER> PARA CONTINUAR ")

    while puntos_crupier < 17:
        cartas_crupier.append(cartas.siguiente_carta(mazo))
        puntos_crupier = cartas.obtener_suma(cartas_crupier)

        menu.mostrar_partida(cartas_crupier, cartas_jugador, False)

        input(f"\n- El crupier roba una carta: {cartas.visualizar_carta(cartas_crupier[-1])}\n<ENTER> PARA CONTINUAR ")

    if (puntos_crupier > 21):

        return cartas_crupier, cartas_jugador, "gana"
    elif (puntos_jugador == puntos_crupier):

        return cartas_crupier, cartas_jugador, "empata"
    elif (puntos_jugador > puntos_crupier):

        return cartas_crupier, cartas_jugador, "gana"
    else:
        return cartas_crupier, cartas_jugador, "pierde"


def acabar_partida(cartas_crupier: list[cartas.Carta], cartas_jugador: list[cartas.Carta], resultado: str):
    """
    Muestra la pantalla final, con las cartas y el resultado final.
    """
    menu.mostrar_partida(cartas_crupier, cartas_jugador, False)

    mensaje: str = "HAS GANADO"
    if resultado == "empata":
        mensaje = "HAS EMPATADO"
    elif resultado == "pierde":
        mensaje = "HAS PERDIDO"

    print(f"\n- {mensaje}")
    input(f"<ENTER> PARA CONTINUAR ")
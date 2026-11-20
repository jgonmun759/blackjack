import cartas, menu, utilidades

def puede_pedir(puntos: int) -> bool:
    """ Comprueba si puede pedir o no """
    return puntos < 21


def jugar():
    """
    Comienza el juego hasta terminar la partida.
    """
    mazo: cartas.Baraja = cartas.obtener_baraja()

    cartas_cupier: list[cartas.Carta] = [cartas.siguiente_carta(mazo) for _ in range(2)]
    cartas_jugador: list[cartas.Carta] = [cartas.siguiente_carta(mazo) for _ in range(2)]

    puntos_cupier: int = cartas.obtener_suma(cartas_cupier)
    puntos_jugador: int = cartas.obtener_suma(cartas_jugador)

    
    eleccion: int = 0
    while puede_pedir(puntos_jugador) and eleccion != 2:
        menu.mostrar_partida(cartas_cupier, cartas_jugador)
        print("")
        menu.mostrar_acciones()

        eleccion = utilidades.pedir_entero("> ", 1, 2)

        if eleccion == 1:
            cartas_jugador.append(cartas.siguiente_carta(mazo))
            puntos_jugador = cartas.obtener_suma(cartas_jugador)

        
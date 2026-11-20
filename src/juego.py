import cartas


def obtener_suma(mazo: list[cartas.Carta]) -> int:
    """
    Obtiene la suma de un mazo de cartas.

    Args:
        cartas: Las cartas a sumar.
    Returns:
        int: La suma.
    """
    suma: int = 0
    numero_as: int = 0

    for carta in mazo:
        puntos: int = cartas.obtener_puntos(carta)

        if puntos == 11:
            numero_as += 1

        suma += puntos

    # Aplica la norma: los ases cuentan 11 excepto si te pasas de 21, entonces contarán 1. 
    while (numero_as > 0) and (suma > 21):
        suma -= 10
        numero_as -= 1

    return suma
    

def jugar():
    """
    Comienza el juego hasta terminar la partida.
    """
    mazo: cartas.Baraja = cartas.obtener_baraja()

    cartas_cupier: list[cartas.Carta] = [cartas.siguiente_carta(mazo) for _ in range(2)]
    cartas_jugador: list[cartas.Carta] = [cartas.siguiente_carta(mazo) for _ in range(2)]
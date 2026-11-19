import random


type Carta = tuple[str, str]
type Baraja = list[Carta]


VALORES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
PALOS = ('Corazones', 'Diamantes', 'Picas', 'Treboles')


def obtener_baraja() -> Baraja:
    """ 
    Obtiene una baraja completa de 52 cartas, cada una
    en una tupla con valor y palo, respectivamente.
    """
    baraja: Baraja = []

    for valor in VALORES:
        for palo in PALOS:
            carta: Carta = (valor, palo)

            baraja.append(carta)

    random.shuffle(baraja) # Desordena las cartas antes de obtener la baraja

    return baraja


def siguiente_carta(baraja: Baraja) -> tuple[Carta, Baraja]:
    """ 
    Obtiene la siguiente carta de la baraja y la elimina. 
    
    Returns:
        Carta: La carta sacada.
        Baraja: La baraja sin la carta.
    Raises:
        IndexError: Si la baraja no tiene cartas.
    """
    if len(baraja) < 1:
        raise IndexError("La baraja no tiene más cartas")

    carta: Carta = baraja[0]
    baraja.pop(0)
    
    return carta, baraja


def obtener_puntos(carta: Carta, as_especial: bool = False) -> int:
    """
    Obtiene el valor en puntos de la carta específica.

    Args:
        carta: La carta de la que se obtiene el valor.
        as_especial: Si se aplica el comportamiento especial del as.
    
    Returns:
        int: La puntuación de la carta.
    """


def jugar(baraja):
    pass
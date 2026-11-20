""" Modulo encargado de gestionar barajas y cartas """
import random


type Carta = tuple[str, str]
type Baraja = list[Carta]


VALORES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
PALOS = ('♥', '♦', '♠', '♣')


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


def siguiente_carta(baraja: Baraja) -> Carta:
    """ 
    Obtiene la siguiente carta de la baraja y la elimina. 
    
    Args:
        baraja: La baraja de la que se cogerá la carta.
    Returns:
        Carta: La carta sacada.
    Raises:
        IndexError: Si la baraja no tiene cartas.
    """
    if len(baraja) < 1:
        raise IndexError("La baraja no tiene más cartas")

    carta: Carta = baraja[0]
    baraja.pop(0)
    
    return carta


def obtener_puntos(carta: Carta) -> int:
    """
    Obtiene el valor en puntos de la carta específica.

    Args:
        carta: La carta de la que se obtiene el valor.
    
    Returns:
        int: La puntuación de la carta.

    Raises:
        IndexError: Si no se encuentra el valor de la carta.
    """
    valor: str = carta[0]
    puntos: int = 0

    if valor.isdigit():
        puntos = int(valor)
    elif valor != "A":
        puntos = 10
    else:
        puntos = 11

    return puntos


def visualizar_carta(carta: Carta) -> str:
    """ Obtiene una cadena con la carta de forma más visual. """
    return f"[{carta[0]} {carta[1]}]"


def visualizar_mazo(mano: list[Carta], ocultar: bool = False) -> str:
    """ Obtiene una cadena con la carta de forma más visual. """
    return ", ".join(
                    visualizar_carta(carta)
                    if (i > 0) and ocultar else "[???]" 
                    for i, carta in enumerate(mano)
                )
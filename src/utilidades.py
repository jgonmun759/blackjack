def pedir_entero(mensaje: str, min: int | None = None, max: int | None = None) -> int:
    """
    Pide un número entero dentro del rango especificado.

    Args:
        mensaje: El mensaje del input.
        min: Número mínimo.
        max: Número máximo.
    Returns:
        int: El número entero válido.
    """
    while True:
        try:
            num: int = int(input(mensaje))
        except ValueError:
            print("\nDebes introducir un número entero")

        if num < min:
            print(f"\nEl número debe ser mayor o igual que {min}")
        elif num > max:
            print(f"\nEl número debe ser menor o igual que {max}")
        else:
            return num
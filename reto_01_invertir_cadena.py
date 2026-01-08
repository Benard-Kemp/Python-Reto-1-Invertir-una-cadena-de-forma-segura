def invertir_cadena_segura(texto: str | None) -> str:
    """
    Invierte una cadena de forma segura.

    Reglas:
    - None -> "" (cadena vacía)
    - No str -> TypeError
    - str -> cadena invertida
    """
    if texto is None:
        return ""

    if not isinstance(texto, str):
        raise TypeError("El parámetro 'texto' debe ser una cadena (str) o None.")

    return texto[::-1]
